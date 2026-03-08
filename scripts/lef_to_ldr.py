import re
import sys
import os

# Constants based on modeling_guidelines.md
# 1 stud = 0.48 um
# 1 stud = 20 LDU
# 1 um = 20 / 0.48 = 41.6666... LDU
UM_TO_LDU = 20 / 0.48

# LEGO Part IDs (Standard orientations are usually X-aligned)
# Name: (width_studs, depth_studs, file)
PLATES = [
    (8, 2, "3034.dat"),
    (8, 1, "3460.dat"),
    (6, 1, "3666.dat"),
    (4, 2, "3020.dat"),
    (4, 1, "3710.dat"),
    (3, 1, "3623.dat"),
    (2, 1, "3023.dat"),
    (1, 1, "3024.dat"),
]

# LDraw Colors
COLOR_SUBSTRATE = 7      # Light Gray
COLOR_NWELL = 19         # Tan
COLOR_ACTIVE = 38        # Dark Orange
COLOR_POLY = 4           # Red
COLOR_METAL1 = 1         # Blue
COLOR_VDD = 14           # Yellow
COLOR_VSS = 0            # Black

# Y-Offsets (Negative is up in LDraw)
Y_SUBSTRATE = 0
Y_RAILS = -8
Y_ACTIVE = -8
Y_PINS = -16
Y_POLY = -16

def get_best_plate(width_ldu, depth_ldu):
    """Pick the best plate and rotation to fit the given area."""
    w_studs = round(width_ldu / 20)
    d_studs = round(depth_ldu / 20)

    if w_studs == 0: w_studs = 1
    if d_studs == 0: d_studs = 1

    # Try exact match first
    for pw, pd, pfile in PLATES:
        if (pw == w_studs and pd == d_studs):
            return pfile, False # No rotation needed
        if (pd == w_studs and pw == d_studs):
            return pfile, True # Rotation needed

    # Try to fit width-wise (greedy)
    for pw, pd, pfile in PLATES:
        if pw <= w_studs and pd <= d_studs:
            return pfile, False
        if pd <= w_studs and pw <= d_studs:
            return pfile, True

    return "3024.dat", False

def parse_lef_macro(lef_content, macro_name):
    pattern = rf"(?<!PROPERTYDEFINITIONS\n  )MACRO\s+{macro_name}(.*?)END\s+{macro_name}"
    match = re.search(pattern, lef_content, re.DOTALL)
    if not match:
        return None

    body = match.group(1)

    size_match = re.search(r"SIZE\s+([\d\.]+)\s+BY\s+([\d\.]+)\s*;", body)
    width_um = float(size_match.group(1)) if size_match else 0
    height_um = float(size_match.group(2)) if size_match else 0

    pins = []
    pin_matches = re.finditer(r"PIN\s+(\w+)(.*?)END\s+\1", body, re.DOTALL)
    for pin_match in pin_matches:
        pin_name = pin_match.group(1)
        pin_body = pin_match.group(2)

        rects = []
        port_matches = re.finditer(r"PORT\s+(.*?)END", pin_body, re.DOTALL)
        for port_match in port_matches:
            port_body = port_match.group(1)
            layer_matches = re.finditer(r"LAYER\s+(\w+)\s*;(.*?)(?=LAYER|END|$)", port_body, re.DOTALL)
            for layer_match in layer_matches:
                layer_name = layer_match.group(1)
                rect_content = layer_match.group(2)
                layer_rects = re.findall(r"RECT\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s*;", rect_content)
                for r in layer_rects:
                    rects.append({'layer': layer_name, 'coords': [float(x) for x in r]})

        pins.append({'name': pin_name, 'rects': rects})

    return {
        'name': macro_name,
        'width_um': width_um,
        'height_um': height_um,
        'pins': pins
    }

def um_to_ldu_coord(um):
    return round(um * UM_TO_LDU)

def generate_ldr(macro_data):
    ldr_lines = [
        f"0 {macro_data['name']}.ldr",
        f"0 Name: {macro_data['name']}.ldr",
        "0 Author: lef_to_ldr.py",
        "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt",
        ""
    ]

    width_ldu = um_to_ldu_coord(macro_data['width_um'])
    height_ldu = um_to_ldu_coord(macro_data['height_um'])

    # 1. Substrate
    ldr_lines.append("0 // Substrate")
    # Tiling substrate to avoid gaps
    current_x = 0
    z_center = height_ldu // 2
    while current_x < width_ldu:
        remaining_w = width_ldu - current_x
        if remaining_w >= 40:
            plate = "3034.dat" # 2x8
            pw = 40
        else:
            plate = "3460.dat" # 1x8
            pw = 20

        x_pos = current_x + pw // 2
        ldr_lines.append(f"1 {COLOR_SUBSTRATE} {x_pos} {Y_SUBSTRATE} {z_center} 1 0 0 0 1 0 0 0 1 {plate}")
        current_x += pw

    ldr_lines.append("")

    # 2. Pins and Rails
    for pin in macro_data['pins']:
        ldr_lines.append(f"0 // Pin {pin['name']}")
        color = COLOR_METAL1
        if pin['name'] == 'VDD': color = COLOR_VDD
        elif pin['name'] == 'VSS': color = COLOR_VSS

        for rect in pin['rects']:
            x1, y1, x2, y2 = rect['coords']
            x1_ldu, y1_ldu = um_to_ldu_coord(x1), um_to_ldu_coord(y1)
            x2_ldu, y2_ldu = um_to_ldu_coord(x2), um_to_ldu_coord(y2)

            w = abs(x2_ldu - x1_ldu)
            h = abs(y2_ldu - y1_ldu)
            x_mid = (x1_ldu + x2_ldu) // 2
            z_mid = (y1_ldu + y2_ldu) // 2

            plate, rotated = get_best_plate(w, h)
            y_off = Y_PINS if color == COLOR_METAL1 else Y_RAILS

            if rotated:
                # Vertical orientation: 0 0 1 0 1 0 -1 0 0
                ldr_lines.append(f"1 {color} {x_mid} {y_off} {z_mid} 0 0 1 0 1 0 -1 0 0 {plate}")
            else:
                # Horizontal orientation: 1 0 0 0 1 0 0 0 1
                ldr_lines.append(f"1 {color} {x_mid} {y_off} {z_mid} 1 0 0 0 1 0 0 0 1 {plate}")
        ldr_lines.append("")

    return "\n".join(ldr_lines)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python lef_to_ldr.py <lef_file> <macro_name>")
        sys.exit(1)

    lef_file = sys.argv[1]
    macro_name = sys.argv[2]

    with open(lef_file, 'r') as f:
        lef_content = f.read()

    macro_data = parse_lef_macro(lef_content, macro_name)
    if not macro_data:
        print(f"Error: Macro {macro_name} not found.")
        sys.exit(1)

    ldr_content = generate_ldr(macro_data)

    os.makedirs("models", exist_ok=True)
    output_file = f"models/{macro_name}.ldr"
    with open(output_file, 'w') as f:
        f.write(ldr_content)

    print(f"Generated {output_file}")
