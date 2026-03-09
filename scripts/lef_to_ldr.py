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
# Sorted by area (descending) to facilitate greedy tiling
PLATES = [
    (8, 2, "3034.dat"),
    (8, 1, "3460.dat"),
    (6, 1, "3666.dat"),
    (4, 2, "3020.dat"),
    (4, 1, "3710.dat"),
    (3, 1, "3623.dat"),
    (2, 2, "3022.dat"),
    (2, 1, "3023.dat"),
    (1, 1, "3024.dat"),
]

# LDraw Colors (V2)
COLOR_SUBSTRATE = 8      # Dark Gray
COLOR_NWELL = 7         # Light Gray
COLOR_ACTIVE_NMOS = 288 # Dark Green
COLOR_ACTIVE_PMOS = 38  # Dark Orange
COLOR_POLY = 4           # Red
COLOR_METAL1 = 1         # Blue
COLOR_VDD = 14           # Yellow
COLOR_VSS = 0            # Black

# Y-Offsets (Negative is up in LDraw)
Y_SUBSTRATE_LOW = 0
Y_SUBSTRATE_HIGH = -8
Y_RAILS = -8
Y_PINS = -16
Y_POLY = -24

def get_best_plates(width_ldu, depth_ldu):
    """
    Greedily tile the given area with standard LEGO plates.
    Returns a list of (plate_file, x_offset_ldu, z_offset_ldu, is_rotated).
    """
    w_studs = round(width_ldu / 20)
    d_studs = round(depth_ldu / 20)

    if w_studs == 0: w_studs = 1
    if d_studs == 0: d_studs = 1

    tiles = []
    covered = [[False for _ in range(d_studs)] for _ in range(w_studs)]

    for z in range(d_studs):
        for x in range(w_studs):
            if not covered[x][z]:
                best_p = None
                best_rotated = False

                # Search for the largest plate that can fit starting at (x, z)
                for pw, pd, pfile in PLATES:
                    # Try normal orientation
                    if x + pw <= w_studs and z + pd <= d_studs:
                        can_fit = True
                        for ix in range(x, x + pw):
                            for iz in range(z, z + pd):
                                if covered[ix][iz]: can_fit = False; break
                            if not can_fit: break
                        if can_fit:
                            best_p = (pw, pd, pfile)
                            best_rotated = False
                            break
                    # Try rotated orientation
                    if x + pd <= w_studs and z + pw <= d_studs:
                        can_fit = True
                        for ix in range(x, x + pd):
                            for iz in range(z, z + pw):
                                if covered[ix][iz]: can_fit = False; break
                            if not can_fit: break
                        if can_fit:
                            best_p = (pw, pd, pfile)
                            best_rotated = True
                            break

                if best_p:
                    pw, pd, pfile = best_p
                    rw = pd if best_rotated else pw
                    rd = pw if best_rotated else pd
                    for ix in range(x, x + rw):
                        for iz in range(z, z + rd):
                            covered[ix][iz] = True
                    x_off = x * 20 + (rw * 20) // 2
                    z_off = z * 20 + (rd * 20) // 2
                    tiles.append((pfile, x_off, z_off, best_rotated))
    return tiles

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

    obs = []
    obs_match = re.search(r"OBS\s+(.*?)END", body, re.DOTALL)
    if obs_match:
        obs_body = obs_match.group(1)
        layer_matches = re.finditer(r"LAYER\s+(\w+)\s*;(.*?)(?=LAYER|END|$)", obs_body, re.DOTALL)
        for layer_match in layer_matches:
            layer_name = layer_match.group(1)
            rect_content = layer_match.group(2)
            layer_rects = re.findall(r"RECT\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s*;", rect_content)
            for r in layer_rects:
                obs.append({'layer': layer_name, 'coords': [float(x) for x in r]})

    return {
        'name': macro_name,
        'width_um': width_um,
        'height_um': height_um,
        'pins': pins,
        'obs': obs
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

    # 1. Substrate low (V2)
    ldr_lines.append("0 // Substrate low (V2)")
    tiles = get_best_plates(width_ldu, height_ldu)
    for plate, x_off, z_off, rotated in tiles:
        if rotated:
            ldr_lines.append(f"1 {COLOR_SUBSTRATE} {x_off} {Y_SUBSTRATE_LOW} {z_off} 0 0 1 0 1 0 -1 0 0 {plate}")
        else:
            ldr_lines.append(f"1 {COLOR_SUBSTRATE} {x_off} {Y_SUBSTRATE_LOW} {z_off} 1 0 0 0 1 0 0 0 1 {plate}")

    # 2. Substrate high
    ldr_lines.append("0 // Substrate high")
    # Tile NMOS and PMOS regions separately to ensure correct N-Well (color 7) boundary
    nmos_height_ldu = height_ldu // 2
    pmos_height_ldu = height_ldu - nmos_height_ldu

    # NMOS Region (Dark Gray 8)
    nmos_tiles = get_best_plates(width_ldu, nmos_height_ldu)
    for plate, x_off, z_off, rotated in nmos_tiles:
        if rotated:
            ldr_lines.append(f"1 {COLOR_SUBSTRATE} {x_off} {Y_SUBSTRATE_HIGH} {z_off} 0 0 1 0 1 0 -1 0 0 {plate}")
        else:
            ldr_lines.append(f"1 {COLOR_SUBSTRATE} {x_off} {Y_SUBSTRATE_HIGH} {z_off} 1 0 0 0 1 0 0 0 1 {plate}")

    # PMOS Region (Light Gray 7)
    pmos_tiles = get_best_plates(width_ldu, pmos_height_ldu)
    for plate, x_off, z_off, rotated in pmos_tiles:
        real_z_off = z_off + nmos_height_ldu
        if rotated:
            ldr_lines.append(f"1 {COLOR_NWELL} {x_off} {Y_SUBSTRATE_HIGH} {real_z_off} 0 0 1 0 1 0 -1 0 0 {plate}")
        else:
            ldr_lines.append(f"1 {COLOR_NWELL} {x_off} {Y_SUBSTRATE_HIGH} {real_z_off} 1 0 0 0 1 0 0 0 1 {plate}")

    ldr_lines.append("")

    # 3. Pins and Rails
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

            rect_tiles = get_best_plates(w, h)
            y_off = Y_PINS if color == COLOR_METAL1 else Y_RAILS

            for plate, tx_off, tz_off, rotated in rect_tiles:
                # Add local tile offsets to global rectangle base
                gx = min(x1_ldu, x2_ldu) + tx_off
                gz = min(y1_ldu, y2_ldu) + tz_off

                if rotated:
                    ldr_lines.append(f"1 {color} {gx} {y_off} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
                else:
                    ldr_lines.append(f"1 {color} {gx} {y_off} {gz} 1 0 0 0 1 0 0 0 1 {plate}")
        ldr_lines.append("")

    # 4. Obstructions
    if macro_data['obs']:
        ldr_lines.append("0 // Obstructions")
        for rect in macro_data['obs']:
            x1, y1, x2, y2 = rect['coords']
            x1_ldu, y1_ldu = um_to_ldu_coord(x1), um_to_ldu_coord(y1)
            x2_ldu, y2_ldu = um_to_ldu_coord(x2), um_to_ldu_coord(y2)

            w = abs(x2_ldu - x1_ldu)
            h = abs(y2_ldu - y1_ldu)

            rect_tiles = get_best_plates(w, h)
            y_off = Y_PINS

            for plate, tx_off, tz_off, rotated in rect_tiles:
                gx = min(x1_ldu, x2_ldu) + tx_off
                gz = min(y1_ldu, y2_ldu) + tz_off

                if rotated:
                    ldr_lines.append(f"1 {COLOR_METAL1} {gx} {y_off} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
                else:
                    ldr_lines.append(f"1 {COLOR_METAL1} {gx} {y_off} {gz} 1 0 0 0 1 0 0 0 1 {plate}")
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
