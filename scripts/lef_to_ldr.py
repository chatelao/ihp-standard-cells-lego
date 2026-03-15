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
ROUND_PLATE = "6141.dat"  # 1x1 round plate

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

def get_best_plates_multi(grid):
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

    for z in range(d_studs):
        for x in range(w_studs):
            if not covered[x][z]:
                color = grid[x][z]
                best_p = None
                for pw, pd, pfile in sorted_plates:
                    # Try normal
                    if x + pw <= w_studs and z + pd <= d_studs:
                        if all(not covered[ix][iz] and grid[ix][iz] == color
                               for ix in range(x, x+pw) for iz in range(z, z+pd)):
                            best_p = (pw, pd, pfile, False)
                            break
                    # Try rotated
                    if x + pd <= w_studs and z + pw <= d_studs:
                        if all(not covered[ix][iz] and grid[ix][iz] == color
                               for ix in range(x, x+pd) for iz in range(z, z+pw)):
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

def generate_ldr(macro_data):
    ldr_lines = [
        f"0 {macro_data['name']}.ldr",
        f"0 Name: {macro_data['name']}.ldr",
        "0 Author: lef_to_ldr.py",
        "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt",
        ""
    ]

    width_ldu = snap_to_grid(um_to_ldu_coord(macro_data['width_um']))
    # Force standard cell height to 15 studs (300 LDU)
    height_ldu = 300
    w_studs = width_ldu // 20
    d_studs = height_ldu // 20

    # 1. Substrate low (V3)
    ldr_lines.append("0 // Substrate low (V3)")
    grid1 = [[COLOR_SUBSTRATE for _ in range(d_studs)] for _ in range(w_studs)]
    tiles1 = get_best_plates_multi(grid1)
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
    for x in range(x_start_active, x_end_active):
        # NMOS (Studs 2-4, Z=40 to 100)
        for z in range(2, 5):
            grid3[x][z] = COLOR_ACTIVE_NMOS
        # PMOS (Studs 8-12, Z=160 to 260)
        for z in range(8, 13):
            grid3[x][z] = COLOR_ACTIVE_PMOS

    tiles3 = get_best_plates_multi(grid3)
    for plate, x_off, z_off, color, rotated in tiles3:
        ldr_lines.append(f"1 {color} {x_off} {Y_ACTIVE} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 4. Polysilicon Gates
    ldr_lines.append("0 STEP")
    ldr_lines.append("0 // Polysilicon Gates")
    is_drive_2 = macro_data['name'].endswith('_2')

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
        (x_start_active * 20, x_end_active * 20, 160, 260)
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
        if j % 2 == 0:
            ideal_c_x, ideal_g_x = 4 * (j // 2) + 1, 4 * (j // 2) + 2
        else:
            ideal_c_x, ideal_g_x = 4 * (j // 2) + 5, 4 * (j // 2) + 4

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
            at_6 = [s for s in possible_studs if s[1] == 6]
            if at_6:
                best_c = min(at_6, key=lambda s: abs(s[0] - ideal_c_x))
            else:
                best_c = min(possible_studs, key=lambda s: (abs(s[1]-6)*10 + abs(s[0]-ideal_c_x)))

        # Determine gate stud(s)
        if is_drive_2:
            gates = [best_c[0] - 1, best_c[0] + 1]
            pad_x = best_c[0] * 20 + 10
            pad_part = '3623.dat'
        else:
            if ideal_g_x > ideal_c_x: g = best_c[0] + 1
            else: g = best_c[0] - 1
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

    def add_contacts_for_rect(xmin, xmax, zmin, zmax, pin_name, direction, current_pin_contacts):
        for sx in range(10, width_ldu, 20):
            if xmin <= sx <= xmax:
                for sz in range(10, height_ldu, 20):
                    if zmin <= sz <= zmax:
                        stud_x, stud_z = sx // 20, sz // 20
                        is_active = any(ax1 <= sx <= ax2 and az1 <= sz <= az2 for ax1, ax2, az1, az2 in active_regions)
                        if pin_name == 'VDD' and stud_z == 14 and stud_x % 2 == 0:
                            current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                        elif pin_name == 'VSS' and stud_z == 0 and stud_x % 2 == 1:
                            current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                        elif is_active and stud_z % 2 == 0:
                            if (stud_z >= 8 and stud_x % 2 == 1) or (stud_z < 8 and stud_x % 2 == 0):
                                current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                                # Fill the gap to active (8 LDU round plate at Y=-24)
                                current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")

    for pin in macro_data['pins']:
        current_pin_contacts = []
        current_pin_metal1 = []
        current_pin_metal1_rects = []

        pin_comment = f"0 // {'VDD' if pin['name']=='VDD' else 'VSS' if pin['name']=='VSS' else 'Pin '+pin['name']} Rail" if pin['name'] in ['VDD', 'VSS'] else f"0 // Pin {pin['name']}"
        color = COLOR_VDD if pin['name']=='VDD' else COLOR_VSS if pin['name']=='VSS' else COLOR_METAL1_INPUT if pin['direction']=='INPUT' else COLOR_METAL1_OUTPUT if pin['direction']=='OUTPUT' else COLOR_METAL1_INTERNAL
        current_pin_metal1.append(pin_comment)

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

                current_pin_metal1_rects.append((xmin, xmax, zmin, zmax))
                w, h = xmax - xmin, zmax - zmin
                rect_tiles = get_best_plates_multi([[color for _ in range(h // 20)] for _ in range(w // 20)])

                for plate, tx_off, tz_off, c, rotated in rect_tiles:
                    gx, gz = xmin + tx_off, zmin + tz_off
                    current_pin_metal1.append(f"1 {c} {gx} {Y_METAL1} {gz} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

                if pin['direction'] == 'INPUT':
                    cfg = pin_assignments[pin['name']]
                    current_pin_contacts.append(f"1 {COLOR_CONTACT} {cfg['contact']*20+10} {Y_CONTACT} {cfg['contact_z']*20+10} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                else:
                    add_contacts_for_rect(xmin, xmax, zmin, zmax, pin['name'], pin['direction'], current_pin_contacts)

        if current_pin_contacts: contact_lines.extend(current_pin_contacts)
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
                add_contacts_for_rect(xmin, xmax, zmin, zmax, "OBS", "UNKNOWN", obs_contacts)
                contact_lines.extend(obs_contacts)

    # Write layers in order
    if contact_lines:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Contacts")
        ldr_lines.extend(contact_lines)

    if metal1_lines:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Metal 1")
        ldr_lines.extend(metal1_lines)

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
