import re
import sys
import os

# Constants based on modeling_guidelines.md (V3)
# 1 stud = 0.12 um
# 1 stud = 20 LDU
# 1 um = 20 / 0.12 = 166.6666... LDU
UM_TO_LDU = 20 / 0.12

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

ROUND_BRICK = "3062b.dat" # 1x1 round brick

# LDraw Colors (V3)
COLOR_SUBSTRATE = 8      # Dark Gray
COLOR_NWELL = 7         # Light Gray
COLOR_ACTIVE_NMOS = 288 # Dark Green
COLOR_ACTIVE_PMOS = 38  # Dark Orange
COLOR_POLY = 4           # Red
COLOR_METAL1 = 1         # Blue
COLOR_METAL2 = 2         # Green
COLOR_VDD = 14           # Yellow
COLOR_VSS = 0            # Black
COLOR_CONTACT = 15       # White
COLOR_VIA = 0            # Black (per guidelines)

# Y-Offsets (Negative is up in LDraw)
Y_SUBSTRATE_LOW = 0
Y_SUBSTRATE_HIGH = -8
Y_ACTIVE = -16
Y_POLY = -24
Y_METAL1 = -56
Y_CONTACT = -48
Y_METAL2 = -88
Y_VIA = -80

def get_best_plates(width_ldu, depth_ldu):
    """
    Greedily tile the given area with standard LEGO plates using a coverage map.
    Returns a list of (plate_file, x_offset_ldu, z_offset_ldu, is_rotated).
    """
    w_studs = round(width_ldu / 20)
    d_studs = round(depth_ldu / 20)

    if w_studs == 0: w_studs = 1
    if d_studs == 0: d_studs = 1

    covered = [[False for _ in range(d_studs)] for _ in range(w_studs)]
    tiles = []

    # Sort plates by area descending
    sorted_plates = sorted(PLATES, key=lambda x: x[0]*x[1], reverse=True)

    for z in range(d_studs):
        for x in range(w_studs):
            if not covered[x][z]:
                best_p = None
                for pw, pd, pfile in sorted_plates:
                    if x + pw <= w_studs and z + pd <= d_studs:
                        if all(not covered[ix][iz] for ix in range(x, x+pw) for iz in range(z, z+pd)):
                            best_p = (pw, pd, pfile, False)
                            break
                    if x + pd <= w_studs and z + pw <= d_studs:
                        if all(not covered[ix][iz] for ix in range(x, x+pd) for iz in range(z, z+pw)):
                            best_p = (pw, pd, pfile, True)
                            break

                if best_p:
                    pw, pd, pfile, rotated = best_p
                    rw = pd if rotated else pw
                    rd = pw if rotated else pd
                    for ix in range(x, x+rw):
                        for iz in range(z, z+rd):
                            covered[ix][iz] = True

                    x_off = x * 20 + (rw * 20) // 2
                    z_off = z * 20 + (rd * 20) // 2
                    tiles.append((pfile, x_off, z_off, rotated))
                else:
                    covered[x][z] = True

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

    # 1. Substrate low (V3)
    ldr_lines.append("0 // Substrate low (V3)")
    tiles = get_best_plates(width_ldu, height_ldu)
    for plate, x_off, z_off, rotated in tiles:
        if rotated:
            ldr_lines.append(f"1 {COLOR_SUBSTRATE} {x_off} {Y_SUBSTRATE_LOW} {z_off} 0 0 1 0 1 0 -1 0 0 {plate}")
        else:
            ldr_lines.append(f"1 {COLOR_SUBSTRATE} {x_off} {Y_SUBSTRATE_LOW} {z_off} 1 0 0 0 1 0 0 0 1 {plate}")

    # 2. Substrate high / N-Well
    ldr_lines.append("0 STEP")
    ldr_lines.append("0 // Substrate high / N-Well")
    split_z = ((height_ldu // 2) // 20) * 20
    for plate, x_off, z_off, rotated in tiles:
        color = COLOR_SUBSTRATE
        if z_off > split_z:
            color = COLOR_NWELL

        if rotated:
            ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_HIGH} {z_off} 0 0 1 0 1 0 -1 0 0 {plate}")
        else:
            ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_HIGH} {z_off} 1 0 0 0 1 0 0 0 1 {plate}")

    # 3. Active Regions (Simplified: horizontal strips)
    ldr_lines.append("0 STEP")
    ldr_lines.append("0 // Active Regions")
    # NMOS strip (bottom)
    nmos_z = 5 * 20 # 5th stud row
    tiles_nmos = get_best_plates(width_ldu, 40)
    for plate, x_off, z_off, rotated in tiles_nmos:
        gz = nmos_z - 20 + z_off
        if rotated:
            ldr_lines.append(f"1 {COLOR_ACTIVE_NMOS} {x_off} {Y_ACTIVE} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
        else:
            ldr_lines.append(f"1 {COLOR_ACTIVE_NMOS} {x_off} {Y_ACTIVE} {gz} 1 0 0 0 1 0 0 0 1 {plate}")

    # PMOS strip (top)
    pmos_z = 11 * 20 # 11th stud row
    tiles_pmos = get_best_plates(width_ldu, 40)
    for plate, x_off, z_off, rotated in tiles_pmos:
        gz = pmos_z - 20 + z_off
        if rotated:
            ldr_lines.append(f"1 {COLOR_ACTIVE_PMOS} {x_off} {Y_ACTIVE} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
        else:
            ldr_lines.append(f"1 {COLOR_ACTIVE_PMOS} {x_off} {Y_ACTIVE} {gz} 1 0 0 0 1 0 0 0 1 {plate}")

    # 4. Pins, Rails, and Contacts
    active_regions = [
        (0, width_ldu, nmos_z-20, nmos_z+20),
        (0, width_ldu, pmos_z-20, pmos_z+20)
    ]

    metal1_rects = []

    for pin in macro_data['pins']:
        ldr_lines.append("0 STEP")
        ldr_lines.append(f"0 // Pin {pin['name']}")
        color = COLOR_METAL1
        is_rail = False
        if pin['name'] == 'VDD':
            color = COLOR_VDD
            is_rail = True
        elif pin['name'] == 'VSS':
            color = COLOR_VSS
            is_rail = True

        for rect in pin['rects']:
            if rect['layer'] == 'Metal1':
                x1, y1, x2, y2 = rect['coords']
                x1_ldu, y1_ldu = um_to_ldu_coord(x1), um_to_ldu_coord(y1)
                x2_ldu, y2_ldu = um_to_ldu_coord(x2), um_to_ldu_coord(y2)

                xmin, xmax = min(x1_ldu, x2_ldu), max(x1_ldu, x2_ldu)
                zmin, zmax = min(y1_ldu, y2_ldu), max(y1_ldu, y2_ldu)

                metal1_rects.append((xmin, xmax, zmin, zmax))

                w = xmax - xmin
                h = zmax - zmin
                rect_tiles = get_best_plates(w, h)

                for plate, tx_off, tz_off, rotated in rect_tiles:
                    gx = xmin + tx_off
                    gz = zmin + tz_off
                    if rotated:
                        ldr_lines.append(f"1 {color} {gx} {Y_METAL1} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
                    else:
                        ldr_lines.append(f"1 {color} {gx} {Y_METAL1} {gz} 1 0 0 0 1 0 0 0 1 {plate}")

                # Add Contacts (Round Bricks)
                if not is_rail:
                    # Check overlap with active regions
                    for axmin, axmax, azmin, azmax in active_regions:
                        oxmin, oxmax = max(xmin, axmin), min(xmax, axmax)
                        ozmin, ozmax = max(zmin, azmin), min(zmax, azmax)

                        if oxmin < oxmax and ozmin < ozmax:
                            # Place a round brick in the center of the overlap if it's large enough,
                            # or just every stud? Let's do every stud in the overlap for "lego feel"
                            s_xmin = (oxmin // 20) * 20 + 10
                            s_xmax = (oxmax // 20) * 20
                            s_zmin = (ozmin // 20) * 20 + 10
                            s_zmax = (ozmax // 20) * 20

                            for sx in range(s_xmin, s_xmax + 20, 20):
                                for sz in range(s_zmin, s_zmax + 20, 20):
                                    if sx <= oxmax and sz <= ozmax:
                                        ldr_lines.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")

            elif rect['layer'] == 'Metal2':
                # Metal 2 and Vias
                x1, y1, x2, y2 = rect['coords']
                x1_ldu, y1_ldu = um_to_ldu_coord(x1), um_to_ldu_coord(y1)
                x2_ldu, y2_ldu = um_to_ldu_coord(x2), um_to_ldu_coord(y2)

                xmin, xmax = min(x1_ldu, x2_ldu), max(x1_ldu, x2_ldu)
                zmin, zmax = min(y1_ldu, y2_ldu), max(y1_ldu, y2_ldu)

                w = xmax - xmin
                h = zmax - zmin
                rect_tiles = get_best_plates(w, h)
                for plate, tx_off, tz_off, rotated in rect_tiles:
                    gx = xmin + tx_off
                    gz = zmin + tz_off
                    if rotated:
                        ldr_lines.append(f"1 {COLOR_METAL2} {gx} {Y_METAL2} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
                    else:
                        ldr_lines.append(f"1 {COLOR_METAL2} {gx} {Y_METAL2} {gz} 1 0 0 0 1 0 0 0 1 {plate}")

                # Add Vias (Black Round Bricks)
                # Check overlap with Metal 1
                for mxmin, mxmax, mzmin, mzmax in metal1_rects:
                    oxmin, oxmax = max(xmin, mxmin), min(xmax, mxmax)
                    ozmin, ozmax = max(zmin, mzmin), min(zmax, mzmax)
                    if oxmin < oxmax and ozmin < ozmax:
                        sx = (oxmin // 20) * 20 + 10
                        sz = (ozmin // 20) * 20 + 10
                        if sx <= oxmax and sz <= ozmax:
                             ldr_lines.append(f"1 {COLOR_VIA} {sx} {Y_VIA} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")

    # 5. Obstructions
    if macro_data['obs']:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Obstructions")
        for rect in macro_data['obs']:
            if rect['layer'] == 'Metal1':
                x1, y1, x2, y2 = rect['coords']
                x1_ldu, y1_ldu = um_to_ldu_coord(x1), um_to_ldu_coord(y1)
                x2_ldu, y2_ldu = um_to_ldu_coord(x2), um_to_ldu_coord(y2)
                w = abs(x2_ldu - x1_ldu)
                h = abs(y2_ldu - y1_ldu)
                rect_tiles = get_best_plates(w, h)
                for plate, tx_off, tz_off, rotated in rect_tiles:
                    gx = min(x1_ldu, x2_ldu) + tx_off
                    gz = min(y1_ldu, y2_ldu) + tz_off
                    if rotated:
                        ldr_lines.append(f"1 {COLOR_METAL1} {gx} {Y_METAL1} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
                    else:
                        ldr_lines.append(f"1 {COLOR_METAL1} {gx} {Y_METAL1} {gz} 1 0 0 0 1 0 0 0 1 {plate}")

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
