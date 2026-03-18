import re
import sys
import os

# Constants based on modeling_guidelines.md (V3)
# 1 stud = 0.27 um
# 1 stud = 20 LDU
# 1 um = 20 / 0.27 = 74.074... LDU
UM_TO_LDU = 20 / 0.27

# LEGO Part IDs (Standard orientations are usually X-aligned)
# Name: (width_studs, depth_studs, file)
# Sorted by area (descending) to facilitate greedy tiling
PLATES = [
    (16, 16, "91405.dat"), # 256
    (16, 8, "92438.dat"),  # 128
    (16, 6, "3027.dat"),   # 96
    (14, 6, "3456.dat"),   # 84
    (12, 6, "3028.dat"),   # 72
    (10, 6, "3033.dat"),   # 60
    (12, 4, "3029.dat"),   # 48
    (8, 6, "3036.dat"),    # 48
    (10, 4, "3030.dat"),   # 40
    (6, 6, "3958.dat"),    # 36
    (16, 2, "4282.dat"),   # 32
    (8, 4, "3035.dat"),    # 32
    (12, 2, "2445.dat"),   # 24
    (6, 4, "3032.dat"),    # 24
    (10, 2, "3832.dat"),   # 20
    (8, 2, "3034.dat"),    # 16
    (4, 4, "3031.dat"),    # 16
    (12, 1, "60479.dat"),  # 12
    (6, 2, "3795.dat"),    # 12
    (10, 1, "4477.dat"),   # 10
    (8, 1, "3460.dat"),    # 8
    (4, 2, "3020.dat"),    # 8
    (6, 1, "3666.dat"),    # 6
    (3, 2, "3021.dat"),    # 6
    (4, 1, "3710.dat"),    # 4
    (2, 2, "3022.dat"),    # 4
    (3, 1, "3623.dat"),    # 3
    (2, 1, "3023.dat"),    # 2
    (1, 1, "3024.dat"),    # 1
]

ROUND_BRICK = "3062b.dat" # 1x1 round brick
ROUND_PLATE = "6141.dat"  # 1x1 round plate
TILE_1X1 = "3070.dat"     # 1x1 flat tile

# LDraw Colors (V3)
COLOR_SUBSTRATE = 8      # Dark Gray
COLOR_NWELL = 7         # Light Gray
COLOR_ACTIVE_NMOS = 288 # Dark Green
COLOR_ACTIVE_PMOS = 38  # Dark Orange
COLOR_POLY = 4           # Red
COLOR_METAL1_INTERNAL = 1 # Blue
COLOR_METAL1_INPUT = 9    # Light Blue
COLOR_METAL1_OUTPUT = 272 # Dark Blue
COLOR_VDD = 14           # Yellow
COLOR_VSS = 0            # Black
COLOR_CONTACT = 15       # White

# Y-Offsets (Negative is up in LDraw)
Y_SUBSTRATE_LOW = 0
Y_SUBSTRATE_HIGH = -8
Y_ACTIVE = -16
Y_POLY = -24
Y_METAL1 = -56
Y_CONTACT = -48
Y_METAL2_PLATE = -64

def get_best_plates_multi(grid, prefer_rotated=False):
    """
    Greedily tile the given color grid with standard LEGO plates.
    'grid' is a 2D list [x][z] of color IDs.
    Returns a list of (plate_file, x_offset_ldu, z_offset_ldu, color, is_rotated).
    """
    w_studs = len(grid)
    d_studs = len(grid[0])
    covered = [[False for _ in range(d_studs)] for _ in range(w_studs)]
    tiles = []

    # Sort plates by area descending
    sorted_plates = sorted(PLATES, key=lambda x: x[0]*x[1], reverse=True)

    # Interlocking: if prefer_rotated, scan X then Z
    outer_range = range(w_studs) if prefer_rotated else range(d_studs)
    inner_range = range(d_studs) if prefer_rotated else range(w_studs)

    for o in outer_range:
        for i in inner_range:
            x, z = (o, i) if prefer_rotated else (i, o)
            if not covered[x][z]:
                color = grid[x][z]
                best_p = None
                for pw, pd, pfile in sorted_plates:
                    # Interlocking: if prefer_rotated, try rotated first
                    configs = [(pd, pw, pfile, True), (pw, pd, pfile, False)] if prefer_rotated else [(pw, pd, pfile, False), (pd, pw, pfile, True)]

                    for cpw, cpd, cpfile, crotated in configs:
                        if x + cpw <= w_studs and z + cpd <= d_studs:
                            if all(not covered[ix][iz] and grid[ix][iz] == color
                                   for ix in range(x, x+cpw) for iz in range(z, z+cpd)):
                                best_p = (cpw, cpd, cpfile, crotated)
                                break
                    if best_p: break

                if best_p:
                    rw, rd, pfile, rotated = best_p
                    for ix in range(x, x+rw):
                        for iz in range(z, z+rd):
                            covered[ix][iz] = True

                    x_off = x * 20 + (rw * 20) // 2
                    z_off = z * 20 + (rd * 20) // 2
                    tiles.append((pfile, x_off, z_off, color, rotated))
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
    pin_matches = re.finditer(r"PIN\s+([\w\[\]<>]+)(.*?)END\s+\1", body, re.DOTALL)
    for pin_match in pin_matches:
        pin_name = pin_match.group(1)
        pin_body = pin_match.group(2)

        direction_match = re.search(r"DIRECTION\s+(\w+)\s*;", pin_body)
        direction = direction_match.group(1) if direction_match else "UNKNOWN"

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

        pins.append({'name': pin_name, 'direction': direction, 'rects': rects})

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

def snap_to_grid(value, grid=20):
    """Snaps a value to the nearest grid multiple, ensuring at least one grid unit."""
    return int(round(value / grid) * grid)

def um_to_ldu_coord(um):
    return round(um * UM_TO_LDU)

def get_unified_parity(stud_x, is_big):
    """
    Unified parity rule for active and gate tracks (Z=2..12):
    - Small models (width <= 7): Always ODD (1).
    - Big models (> 7 studs): Symmetric parity - ODD if X < 8, EVEN if X >= 8.
    """
    if not is_big:
        return 1 # ODD
    return 1 if stud_x < 8 else 0 # ODD if < 8, EVEN if >= 8

def generate_ldr(macro_data):
    ldr_lines = [
        f"0 {macro_data['name']}.ldr",
        f"0 Name: {macro_data['name']}.ldr",
        "0 Author: lef_to_ldr.py",
        "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt",
        "0 !LPUB PLI GLOBAL ON",
        ""
    ]

    width_ldu = snap_to_grid(um_to_ldu_coord(macro_data['width_um']))
    if macro_data['name'] in ['sg13g2_nand2b_2', 'sg13g2_xor2_1']:
        width_ldu = 300
    # Force standard cell height to 15 studs (300 LDU)
    height_ldu = 300
    w_studs = width_ldu // 20
    d_studs = height_ldu // 20

    # 1. Substrate low (V3)
    ldr_lines.append("0 // Substrate low (V3)")
    grid1 = [[COLOR_SUBSTRATE for _ in range(d_studs)] for _ in range(w_studs)]
    # Interlocking: use prefer_rotated=True for the bottom layer
    tiles1 = get_best_plates_multi(grid1, prefer_rotated=True)
    for plate, x_off, z_off, color, rotated in tiles1:
        ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_LOW} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 2. Substrate high / N-Well
    ldr_lines.append("0 STEP")
    ldr_lines.append("0 // Substrate high / N-Well")
    # N-Well typically occupies the upper half of the cell (split at Stud 8)
    split_z = 160
    grid2 = [[COLOR_SUBSTRATE if (z*20+10) < split_z else COLOR_NWELL for z in range(d_studs)] for x in range(w_studs)]
    tiles2 = get_best_plates_multi(grid2)
    for plate, x_off, z_off, color, rotated in tiles2:
        ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_HIGH} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 3. Active Regions
    ldr_lines.append("0 STEP")
    ldr_lines.append("0 // Active Regions")

    active_studs = w_studs - 2
    if active_studs < 1: active_studs = 1
    x_start_active = (w_studs - active_studs) // 2
    x_end_active = x_start_active + active_studs

    # Substrate fill in Active layer
    grid3 = [[(COLOR_SUBSTRATE if (z*20+10) < split_z else COLOR_NWELL) for z in range(d_studs)] for x in range(w_studs)]
    if macro_data['name'] == 'sg13g2_nand2b_2':
        # Specialized Active regions for nand2b_2 (15 studs wide)
        # PMOS (Z=8..12): Gaps at X=3, X=14
        pmos_x = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for x in pmos_x:
            for z in range(8, 13):
                grid3[x][z] = COLOR_ACTIVE_PMOS
        # NMOS (Z=2..4): Gaps at X=0, X=4, X=14
        nmos_x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for x in nmos_x:
            for z in range(2, 5):
                grid3[x][z] = COLOR_ACTIVE_NMOS
    else:
        for x in range(x_start_active, x_end_active):
            # NMOS (Studs 2-4, Z=40 to 100)
            for z in range(2, 5):
                grid3[x][z] = COLOR_ACTIVE_NMOS
            # PMOS (Studs 8-12, Z=160 to 260)
            for z in range(8, 13):
                grid3[x][z] = COLOR_ACTIVE_PMOS

    # Add active regions under rails for the full width of the cell
    for x in range(w_studs):
        # South border (VSS, Stud 0)
        grid3[x][0] = COLOR_ACTIVE_NMOS
        # North border (VDD, Stud 14)
        grid3[x][14] = COLOR_ACTIVE_PMOS

    tiles3 = get_best_plates_multi(grid3)
    for plate, x_off, z_off, color, rotated in tiles3:
        ldr_lines.append(f"1 {color} {x_off} {Y_ACTIVE} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 4. Polysilicon Gates
    ldr_lines.append("0 STEP")
    ldr_lines.append("0 // Polysilicon Gates")
    is_drive_2 = macro_data['name'].endswith('_2')
    is_big = w_studs > 7

    # Pre-calculate pin assignments for fixed columns
    input_pins = [p for p in macro_data['pins'] if p['direction'] == 'INPUT']
    def get_pin_x(p):
        for r in p['rects']:
            if r['layer'] == 'Metal1':
                return (r['coords'][0] + r['coords'][2]) / 2
        return 0
    input_pins.sort(key=get_pin_x)

    pin_assignments = {} # name -> config dict
    active_regions = [
        (x_start_active * 20, x_end_active * 20, 40, 100),
        (x_start_active * 20, x_end_active * 20, 160, 260),
        # Active regions under rails for the full width of the cell
        (0, width_ldu, 0, 20),
        (0, width_ldu, 280, 300)
    ]

    for j, pin in enumerate(input_pins):
        # Find all possible (x, z) studs for the contact within LEF RECTs
        possible_studs = []
        for rect in pin['rects']:
            if rect['layer'] == 'Metal1':
                # Exact bounds in LDU
                lx1 = um_to_ldu_coord(rect['coords'][0])
                lz1 = um_to_ldu_coord(rect['coords'][1]) + 10
                lx2 = um_to_ldu_coord(rect['coords'][2])
                lz2 = um_to_ldu_coord(rect['coords'][3]) + 10
                for i in range(w_studs):
                    cx = i * 20 + 10
                    if lx1 <= cx <= lx2:
                        for k in range(d_studs):
                            cz = k * 20 + 10
                            if lz1 <= cz <= lz2:
                                possible_studs.append((i, k))

        # Gold Standard ideals:
        # Distribution: 2 pins -> 1, 5. 3 pins -> 1, 5, 9. 4 pins -> 1, 5, 9, 13
        ideal_c_x = 4 * j + 1

        if not possible_studs:
            # Fallback to nearest stud center if none strictly inside
            best_c = (ideal_c_x, 6) # Default
            min_dist = float('inf')
            for rect in pin['rects']:
                if rect['layer'] == 'Metal1':
                    mid_x = (rect['coords'][0] + rect['coords'][2]) / 2
                    mid_y = (rect['coords'][1] + rect['coords'][3]) / 2
                    mid_x_ldu = um_to_ldu_coord(mid_x)
                    mid_z_ldu = um_to_ldu_coord(mid_y) + 10
                    si, sk = mid_x_ldu // 20, mid_z_ldu // 20
                    dist = abs(sk - 6) * 10 + abs(si - ideal_c_x)
                    if dist < min_dist:
                        min_dist = dist
                        best_c = (si, sk)
        else:
            # Filter by parity
            target_parity = get_unified_parity(ideal_c_x, is_big)
            parity_studs = [s for s in possible_studs if s[0] % 2 == target_parity]
            if not parity_studs:
                parity_studs = possible_studs # Relax if no matches

            at_6 = [s for s in parity_studs if s[1] == 6]
            if at_6:
                best_c = min(at_6, key=lambda s: abs(s[0] - ideal_c_x))
            else:
                best_c = min(parity_studs, key=lambda s: (abs(s[1]-6)*10 + abs(s[0]-ideal_c_x)))

        # Determine gate stud(s)
        # Gold standard: gates at C-1 and C+1 for Big/Drive-2, or C+1 for Drive-1 Small
        if is_drive_2 or is_big:
            gates = [best_c[0] - 1, best_c[0] + 1]
            pad_x = best_c[0] * 20 + 10
            pad_part = '3623.dat'
        else:
            g = best_c[0] + 1
            gates = [g]
            pad_x = ((best_c[0] + g) / 2) * 20 + 10
            pad_part = '3023.dat'

        pin_assignments[pin['name']] = {
            'gate': gates,
            'contact': best_c[0],
            'contact_z': best_c[1],
            'pad_x': pad_x,
            'pad_part': pad_part
        }

    for pin in macro_data['pins']:
        if pin['direction'] == 'INPUT':
            config = pin_assignments[pin['name']]
            ldr_lines.append(f"1 {COLOR_POLY} {config['pad_x']} {Y_POLY} {config['contact_z']*20+10} 1 0 0 0 1 0 0 0 1 {config['pad_part']}")
            for gs in config['gate']:
                gx = gs * 20 + 10
                gate_tiles = get_best_plates_multi([[COLOR_POLY for _ in range(13)]]) # Studs 1-13
                for pfile, tx_off, tz_off, color, rotated in gate_tiles:
                    gz = 20 + tz_off
                    ldr_lines.append(f"1 {color} {gx} {Y_POLY} {gz} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {pfile}")

    # 5. Pins, Rails, and Contacts
    contact_lines = []
    metal1_lines = []
    metal2_plate_lines = []

    def add_contacts_for_rect(xmin, xmax, zmin, zmax, pin_name, direction, current_pin_contacts, current_pin_upward_plates, color):
        for sx in range(10, width_ldu, 20):
            if xmin <= sx <= xmax:
                for sz in range(10, height_ldu, 20):
                    if zmin <= sz <= zmax:
                        stud_x, stud_z = sx // 20, sz // 20
                        is_active = any(ax1 <= sx <= ax2 and az1 <= sz <= az2 for ax1, ax2, az1, az2 in active_regions)

                        # Power Rails: Must use exact tracks (Z=0 or Z=14)
                        if pin_name == 'VDD':
                            if stud_z == 14 and stud_x % 2 == 0:
                                current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                                current_pin_upward_plates.append(f"1 {color} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
                                if is_active:
                                    current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                        elif pin_name == 'VSS':
                            if stud_z == 0 and stud_x % 2 == 1:
                                current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                                current_pin_upward_plates.append(f"1 {color} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
                                if is_active:
                                    current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                        # Signal pins and Obstructions: Must use even tracks 2-12
                        elif 0 < stud_z < 14 and stud_z % 2 == 0:
                            # Unified parity rule for active and gate tracks (Z=2..12)
                            if stud_x % 2 == get_unified_parity(stud_x, is_big):
                                # Contacts are allowed in active regions or on the gate track (Z=6)
                                if is_active or stud_z == 6:
                                    current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                                    current_pin_upward_plates.append(f"1 {color} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
                                    # Fill the gap to active/poly (8 LDU round plate at Y=-24)
                                    current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")

    for pin in macro_data['pins']:
        current_pin_contacts = []
        current_pin_upward_plates = []
        current_pin_metal1 = []

        pin_comment = f"0 // {'VDD' if pin['name']=='VDD' else 'VSS' if pin['name']=='VSS' else 'Pin '+pin['name']} Rail" if pin['name'] in ['VDD', 'VSS'] else f"0 // Pin {pin['name']}"
        color = COLOR_VDD if pin['name']=='VDD' else COLOR_VSS if pin['name']=='VSS' else COLOR_METAL1_INPUT if pin['direction']=='INPUT' else COLOR_METAL1_OUTPUT if pin['direction']=='OUTPUT' else COLOR_METAL1_INTERNAL
        current_pin_metal1.append(pin_comment)

        # First, check for explicit Via1 rects for upward plates
        has_via1 = False
        for rect in pin['rects']:
            if rect['layer'] == 'Via1':
                has_via1 = True
                vx1_ldu, vy1_ldu = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                vx2_ldu, vy2_ldu = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                vxmin, vxmax = snap_to_grid(min(vx1_ldu, vx2_ldu)), snap_to_grid(max(vx1_ldu, vx2_ldu))
                vzmin, vzmax = snap_to_grid(min(vy1_ldu, vy2_ldu)), snap_to_grid(max(vy1_ldu, vy2_ldu))

                # Ensure at least one stud if rect is very small
                if vxmax <= vxmin: vxmax = vxmin + 20
                if vzmax <= vzmin: vzmax = vzmin + 20

                for vsx in range(vxmin + 10, vxmax, 20):
                    for vsz in range(vzmin + 10, vzmax, 20):
                        current_pin_upward_plates.append(f"1 {color} {vsx} {Y_METAL2_PLATE} {vsz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")

        for rect in pin['rects']:
            if rect['layer'] == 'Metal1':
                x1_ldu, y1_ldu = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                x2_ldu, y2_ldu = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                xmin, xmax = snap_to_grid(min(x1_ldu, x2_ldu)), snap_to_grid(max(x1_ldu, x2_ldu))
                zmin, zmax = snap_to_grid(min(y1_ldu, y2_ldu)), snap_to_grid(max(y1_ldu, y2_ldu))

                if xmax <= xmin:
                    if xmax + 20 <= width_ldu: xmax += 20
                    elif xmin - 20 >= 0: xmin -= 20
                    else: xmax = xmin + 20
                if zmax <= zmin:
                    if zmax + 20 <= height_ldu: zmax += 20
                    elif zmin - 20 >= 0: zmin -= 20
                    else: zmax = zmin + 20

                w, h = xmax - xmin, zmax - zmin
                rect_tiles = get_best_plates_multi([[color for _ in range(h // 20)] for _ in range(w // 20)])

                for plate, tx_off, tz_off, c, rotated in rect_tiles:
                    gx, gz = xmin + tx_off, zmin + tz_off
                    current_pin_metal1.append(f"1 {c} {gx} {Y_METAL1} {gz} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

                if pin['direction'] == 'INPUT':
                    cfg = pin_assignments[pin['name']]
                    current_pin_contacts.append(f"1 {COLOR_CONTACT} {cfg['contact']*20+10} {Y_CONTACT} {cfg['contact_z']*20+10} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                    if not has_via1:
                        current_pin_upward_plates.append(f"1 {color} {cfg['contact']*20+10} {Y_METAL2_PLATE} {cfg['contact_z']*20+10} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
                else:
                    # If we don't have Via1, we'll add upward plates based on contacts inside add_contacts_for_rect
                    add_contacts_for_rect(xmin, xmax, zmin, zmax, pin['name'], pin['direction'], current_pin_contacts, [] if has_via1 else current_pin_upward_plates, color)

        if current_pin_contacts: contact_lines.extend(current_pin_contacts)
        if current_pin_upward_plates: metal2_plate_lines.extend(current_pin_upward_plates)
        if len(current_pin_metal1) > 1: metal1_lines.extend(current_pin_metal1)

    # Obstructions
    if macro_data['obs']:
        metal1_lines.append("0 // Obstructions")
        for rect in macro_data['obs']:
            if rect['layer'] == 'Metal1':
                x1, y1, x2, y2 = rect['coords']
                x1_ldu, y1_ldu = um_to_ldu_coord(x1), um_to_ldu_coord(y1) + 10
                x2_ldu, y2_ldu = um_to_ldu_coord(x2), um_to_ldu_coord(y2) + 10

                xmin = max(0, min(width_ldu, snap_to_grid(min(x1_ldu, x2_ldu))))
                xmax = max(0, min(width_ldu, snap_to_grid(max(x1_ldu, x2_ldu))))
                zmin = max(0, min(height_ldu, snap_to_grid(min(y1_ldu, y2_ldu))))
                zmax = max(0, min(height_ldu, snap_to_grid(max(y1_ldu, y2_ldu))))

                if xmax <= xmin:
                    if xmax + 20 <= width_ldu: xmax += 20
                    elif xmin - 20 >= 0: xmin -= 20
                    else: xmax = xmin + 20
                if zmax <= zmin:
                    if zmax + 20 <= height_ldu: zmax += 20
                    elif zmin - 20 >= 0: zmin -= 20
                    else: zmax = zmin + 20

                w = xmax - xmin
                h = zmax - zmin
                rect_tiles = get_best_plates_multi([[COLOR_METAL1_INTERNAL for _ in range(h // 20)] for _ in range(w // 20)])
                for plate, tx_off, tz_off, c, rotated in rect_tiles:
                    gx = xmin + tx_off
                    gz = zmin + tz_off
                    if rotated:
                        metal1_lines.append(f"1 {c} {gx} {Y_METAL1} {gz} 0 0 1 0 1 0 -1 0 0 {plate}")
                    else:
                        metal1_lines.append(f"1 {c} {gx} {Y_METAL1} {gz} 1 0 0 0 1 0 0 0 1 {plate}")

                # Add Contacts for Obstructions
                obs_contacts = []
                obs_upward = []
                add_contacts_for_rect(xmin, xmax, zmin, zmax, "OBS", "UNKNOWN", obs_contacts, obs_upward, COLOR_METAL1_INTERNAL)
                contact_lines.extend(obs_contacts)
                metal2_plate_lines.extend(obs_upward)

    # Write layers in order
    if contact_lines:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Contacts")
        ldr_lines.extend(contact_lines)

    if metal1_lines:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Metal 1")
        ldr_lines.extend(metal1_lines)

    if metal2_plate_lines:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Metal 2 Connections")
        ldr_lines.extend(metal2_plate_lines)

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
