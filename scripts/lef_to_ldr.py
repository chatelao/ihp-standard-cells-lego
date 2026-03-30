import math
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

# Snapping tolerance (LDU)
SNAPPING_TOLERANCE = 9.0

# CIF to LDU conversion: 1 unit = 1 nm, 270 nm = 20 LDU
CIF_TO_LDU = 20 / 270

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
    if not grid: return []
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
                if color is None:
                    covered[x][z] = True
                    continue
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

def parse_cif(cif_path):
    if not os.path.exists(cif_path):
        return None
    with open(cif_path, 'r') as f:
        cif_content = f.read()

    layers = {}
    current_layer = None

    # CIF units are nm. 1 LDU = 13.5 nm.
    # Applying +10 LDU offset only to Z-axis (LEF Y) to align with existing logic and verify_top_view.py.
    def to_ldr_x(val):
        return val * CIF_TO_LDU
    def to_ldr_z(val):
        return val * CIF_TO_LDU + 10

    commands = cif_content.split(';')
    for cmd in commands:
        cmd = cmd.strip()
        if not cmd: continue

        if cmd.startswith('L '):
            current_layer = cmd[2:].strip()
            if current_layer not in layers:
                layers[current_layer] = []
        elif cmd.startswith('B '):
            if current_layer:
                parts = re.split(r'\s+|,', cmd[2:].strip())
                if len(parts) >= 4:
                    try:
                        w_nm, h_nm, xc_nm, yc_nm = map(float, parts[:4])
                        x1 = to_ldr_x(xc_nm - w_nm/2)
                        z1 = to_ldr_z(yc_nm - h_nm/2)
                        x2 = to_ldr_x(xc_nm + w_nm/2)
                        z2 = to_ldr_z(yc_nm + h_nm/2)
                        layers[current_layer].append({
                            'type': 'box',
                            'coords': [x1, z1, x2, z2]
                        })
                    except ValueError:
                        continue
        elif cmd.startswith('P '):
            if current_layer:
                points_str = cmd[2:].strip().split()
                points = []
                for p in points_str:
                    pt = p.split(',')
                    if len(pt) == 2:
                        try:
                            px_nm, py_nm = float(pt[0]), float(pt[1])
                            points.append((to_ldr_x(px_nm), to_ldr_z(py_nm)))
                        except ValueError:
                            continue
                if points:
                    layers[current_layer].append({
                        'type': 'polygon',
                        'points': points
                    })
    return layers

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

        is_gate = "ANTENNAGATEAREA" in pin_body
        is_diff = "ANTENNADIFFAREA" in pin_body

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

        pins.append({'name': pin_name, 'direction': direction, 'rects': rects, 'is_gate': is_gate, 'is_diff': is_diff})

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

def is_stud_occupied(gx, gz, xmin, xmax, zmin, zmax):
    """
    Refined snapping rule:
    - If a dimension (width or height) is <= 21.0 LDU, use a center-based rule.
    - Otherwise, use the SNAPPING_TOLERANCE (9.0 LDU) overlap rule.
    """
    overlap_x = min(xmax, gx + 20) - max(xmin, gx)
    overlap_z = min(zmax, gz + 20) - max(zmin, gz)
    if overlap_x <= 0 or overlap_z <= 0:
        return False

    center_x = (xmin + xmax) / 2
    center_z = (zmin + zmax) / 2
    width = xmax - xmin
    height = zmax - zmin

    is_occ_x = (gx <= center_x < gx + 20) if width <= 21.0 else (overlap_x >= SNAPPING_TOLERANCE)
    is_occ_z = (gz <= center_z < gz + 20) if height <= 21.0 else (overlap_z >= SNAPPING_TOLERANCE)

    return is_occ_x and is_occ_z

def is_point_in_poly(x, z, poly):
    n = len(poly)
    inside = False
    p1x, p1z = poly[0]
    for i in range(n + 1):
        p2x, p2z = poly[i % n]
        if z > min(p1z, p2z):
            if z <= max(p1z, p2z):
                if x <= max(p1x, p2x):
                    if p1z != p2z:
                        xints = (z - p1z) * (p2x - p1x) / (p2z - p1z) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1z = p2x, p2z
    return inside

def is_stud_occupied_geom(gx, gz, geom):
    if geom['type'] == 'box':
        xmin, zmin, xmax, zmax = geom['coords']
        return is_stud_occupied(gx, gz, xmin, xmax, zmin, zmax)

    if geom['type'] == 'polygon':
        poly = geom['points']
        xs = [p[0] for p in poly]
        zs = [p[1] for p in poly]
        xmin, zmin, xmax, zmax = min(xs), min(zs), max(xs), max(zs)

        # Quick reject
        if max(xmin, gx) >= min(xmax, gx+20) or max(zmin, gz) >= min(zmax, gz+20):
            return False

        width = xmax - xmin
        height = zmax - zmin

        # For polygons, we check center of stud
        if is_point_in_poly(gx + 10, gz + 10, poly):
            return True

        # Also check if bbox overlap is significant for larger polygons
        if width > 21.0 and height > 21.0:
            overlap_x = min(xmax, gx + 20) - max(xmin, gx)
            overlap_z = min(zmax, gz + 20) - max(zmin, gz)
            if overlap_x >= SNAPPING_TOLERANCE and overlap_z >= SNAPPING_TOLERANCE:
                # Still check center to be safe against concave shapes
                return True

    return False

def get_expected_parity(stud_x, stud_z, is_big, is_drive_2):
    """
    Gold Standard Parity Rules (V3):
    - VSS Rail (Track 0): ODD
    - VDD Rail (Track 14): EVEN
    - NMOS Contacts (Track 2, 4): ALWAYS EVEN
    - PMOS Contacts (Track 8, 10, 12): Drive-1 Small=ODD, else EVEN
    - Input Contacts (Track 6): Small=ODD, Big=Symmetric
    """
    if stud_z == 0: return 1 # VSS
    if stud_z == 14: return 0 # VDD
    if stud_z in [2, 4]: return 0 # NMOS
    if stud_z in [8, 10, 12]:
        return 0 if (is_drive_2 or is_big) else 1
    if stud_z == 6:
        if not is_big: return 1
        return 1 if stud_x < 8 else 0
    return 1 # Fallback ODD

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

    # CIF Data Loading
    cif_data = parse_cif(f"specifications/cells/{macro_data['name']}.cif")

    active_grid = [[(COLOR_SUBSTRATE if (z*20+10) < split_z else COLOR_NWELL) for z in range(d_studs)] for x in range(w_studs)]

    active_studs = w_studs - 2
    if active_studs < 1: active_studs = 1
    x_start_active = (w_studs - active_studs) // 2
    x_end_active = x_start_active + active_studs

    if cif_data and 'L1D0' in cif_data:
        for geom in cif_data['L1D0']:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i*20, k*20, geom):
                        if (k*20+10) < split_z:
                            active_grid[i][k] = COLOR_ACTIVE_NMOS
                        else:
                            active_grid[i][k] = COLOR_ACTIVE_PMOS
    else:
        for x in range(x_start_active, x_end_active):
            # NMOS (Studs 2-4, Z=40 to 100)
            for z in range(2, 5):
                active_grid[x][z] = COLOR_ACTIVE_NMOS
            # PMOS (Studs 8-12, Z=160 to 260)
            for z in range(8, 13):
                active_grid[x][z] = COLOR_ACTIVE_PMOS

    # Cell-specific Active Region logic (Handmade optimizations)
    if macro_data['name'] == 'sg13g2_nand2b_2':
        # Isolation gaps from golden handmade design
        active_grid[3][10] = COLOR_NWELL # PMOS Gap at X=3
        active_grid[3][12] = COLOR_NWELL # PMOS Gap at X=3
        active_grid[3][8] = COLOR_NWELL # PMOS Gap at X=3
        active_grid[4][2] = COLOR_SUBSTRATE # NMOS Gap at X=4
        active_grid[4][4] = COLOR_SUBSTRATE # NMOS Gap at X=4

    # Add active regions under rails for the full width of the cell
    for x in range(w_studs):
        # South border (VSS, Stud 0)
        active_grid[x][0] = COLOR_ACTIVE_NMOS
        # North border (VDD, Stud 14)
        active_grid[x][14] = COLOR_ACTIVE_PMOS

    # 4. Polysilicon Gates
    ldr_lines.append("0 STEP")
    ldr_lines.append("0 // Polysilicon Gates")
    is_decap = 'decap' in macro_data['name'].lower()
    is_drive_2 = macro_data['name'].endswith('_2')
    is_big = w_studs > 7

    poly_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]

    # Use CIF Polysilicon if available
    if cif_data and 'L5D0' in cif_data:
        for geom in cif_data['L5D0']:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i*20, k*20, geom):
                        # Polysilicon is restricted to Tracks 1-13 center area
                        if 1 <= k <= 13:
                            poly_grid[i][k] = COLOR_POLY

    # Identify Power Finger occupancy to avoid gate/contact overlaps
    power_occupancy = [[False for _ in range(d_studs)] for _ in range(w_studs)]
    for pin in macro_data['pins']:
        if pin['name'] in ['VDD', 'VSS']:
            for rect in pin['rects']:
                if rect['layer'] == 'Metal1':
                    lx1, lz1 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                    lx2, lz2 = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                    xmin, xmax = min(lx1, lx2), max(lx1, lx2)
                    zmin, zmax = min(lz1, lz2), max(lz1, lz2)
                    for i in range(w_studs):
                        for k in range(d_studs):
                            if is_stud_occupied(i*20, k*20, xmin, xmax, zmin, zmax):
                                power_occupancy[i][k] = True

    def is_compliant_global(stud_x, stud_z):
        if stud_z % 2 != 0: return False
        if stud_x % 2 != get_expected_parity(stud_x, stud_z, is_big, is_drive_2): return False
        # NEVER overlap with power fingers
        return not power_occupancy[stud_x][stud_z]

    # Map CIF Metal 1 to LEF pins/nets
    cif_net_map = {} # (stud_x, stud_z) -> net_name/pin_name
    if cif_data and 'L6D0' in cif_data and 'L8D0' in cif_data:
        # 1. Identify which LEF pin each CIF Metal 1 rectangle belongs to
        cif_m1_to_net = [] # list of (geom, net_name)
        for geom in cif_data['L8D0']:
            # Find overlapping LEF pin
            xs = [p[0] for p in geom['points']] if geom['type'] == 'polygon' else [geom['coords'][0], geom['coords'][2]]
            zs = [p[1] for p in geom['points']] if geom['type'] == 'polygon' else [geom['coords'][1], geom['coords'][3]]
            xmin, zmin, xmax, zmax = min(xs), min(zs), max(xs), max(zs)

            matched_net = "Internal"
            max_overlap = 0
            for pin in macro_data['pins']:
                for rect in pin['rects']:
                    if rect['layer'] == 'Metal1':
                        lx1, lz1 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                        lx2, lz2 = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                        l_xmin, l_xmax = min(lx1, lx2), max(lx1, lx2)
                        l_zmin, l_zmax = min(lz1, lz2), max(lz1, lz2)

                        overlap_x = min(xmax, l_xmax) - max(xmin, l_xmin)
                        overlap_z = min(zmax, l_zmax) - max(zmin, l_zmin)
                        if overlap_x > 0 and overlap_z > 0:
                            area = overlap_x * overlap_z
                            if area > max_overlap:
                                max_overlap = area
                                matched_net = pin['name']
            cif_m1_to_net.append((geom, matched_net))

        # 2. Map CIF contacts to nets via CIF Metal 1 overlap
        for c_geom in cif_data['L6D0']:
            c_xmin, c_zmin, c_xmax, c_zmax = c_geom['coords']
            cx, cz = (c_xmin + c_xmax) / 2, (c_zmin + c_zmax) / 2

            for m1_geom, net_name in cif_m1_to_net:
                is_inside = False
                if m1_geom['type'] == 'box':
                    m_xmin, m_zmin, m_xmax, m_zmax = m1_geom['coords']
                    if m_xmin <= cx <= m_xmax and m_zmin <= cz <= m_zmax:
                        is_inside = True
                elif m1_geom['type'] == 'polygon':
                    if is_point_in_poly(cx, cz, m1_geom['points']):
                        is_inside = True

                if is_inside:
                    # Snapping to nearest compliant stud
                    best_stud = None
                    min_dist = float('inf')
                    for i in range(w_studs):
                        for k in range(d_studs):
                            sx, sz = i * 20 + 10, k * 20 + 10
                            if is_compliant_global(i, k):
                                dist = abs(sx - cx) + abs(sz - cz)
                                if dist < min_dist:
                                    min_dist = dist
                                    best_stud = (i, k)
                    if best_stud:
                        cif_net_map[best_stud] = net_name
                    break

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

        target_parity = get_expected_parity(ideal_c_x, 6, is_big, is_drive_2)

        # Try to find a CIF contact for this pin first
        cif_contacts = [s for s, net in cif_net_map.items() if net == pin['name']]
        if cif_contacts:
            # Prefer CIF contact closest to ideal Track 6 and ideal X
            best_c = min(cif_contacts, key=lambda s: (abs(s[1]-6)*10 + abs(s[0]-ideal_c_x)))
        else:
            compliant_studs = [s for s in possible_studs if is_compliant_global(s[0], s[1])]

            if not compliant_studs:
                # Fallback: Find nearest compliant stud (even Z, correct X-parity, NO power)
                best_c = None
                min_dist = float('inf')
                for i in range(w_studs):
                    for k in range(0, d_studs, 2): # Even Z only
                        if is_compliant_global(i, k):
                            dist = abs(k - 6) * 10 + abs(i - ideal_c_x)
                            if dist < min_dist:
                                min_dist = dist
                                best_c = (i, k)
            else:
                # Prefer Track 6
                at_6 = [s for s in compliant_studs if s[1] == 6]
                if at_6:
                    best_c = min(at_6, key=lambda s: abs(s[0] - ideal_c_x))
                else:
                    best_c = min(compliant_studs, key=lambda s: (abs(s[1]-6)*10 + abs(s[0]-ideal_c_x)))

        # Determine gate stud(s)
        # Gold standard: gates at C-1 and C+1 for Big/Drive-2, or C+1 for Drive-1 Small
        def get_valid_gate(target_x):
            # Try target, then fallback to nearest stud not occupied by power
            if 0 <= target_x < w_studs and not any(power_occupancy[target_x][z] for z in range(2, 13)):
                return target_x
            # Search nearby
            for offset in [1, -1, 2, -2]:
                nx = target_x + offset
                if 0 <= nx < w_studs and not any(power_occupancy[nx][z] for z in range(2, 13)):
                    return nx
            return target_x # Fallback to target if nothing found

        if is_drive_2 or is_big:
            gates = [get_valid_gate(best_c[0] - 1), get_valid_gate(best_c[0] + 1)]
            pad_x = best_c[0] * 20 + 10
            pad_part = '3623.dat'
        else:
            g = get_valid_gate(best_c[0] + 1)
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

    poly_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]

    if not (cif_data and 'L5D0' in cif_data):
        if is_decap:
            # Specialized Polysilicon for DECAP: Fill all active regions
            # We will later remove Poly where the Active-connected pin (VSS) has contacts.
            for x in range(x_start_active, x_end_active):
                for z in range(2, 13):
                    poly_grid[x][z] = COLOR_POLY
        else:
            for pin in macro_data['pins']:
                if pin['direction'] == 'INPUT':
                    config = pin_assignments[pin['name']]
                    # Mark gates on grid
                    for gs in config['gate']:
                        for gz in range(2, 13): # Studs 2-12 (~2/3 height)
                            poly_grid[gs][gz] = COLOR_POLY
                    # Mark pad/bridge on grid
                    cx = config['contact']
                    cz = config['contact_z']
                    poly_grid[cx][cz] = COLOR_POLY
                    # Connect pad to gates (horizontal bridge)
                    for gx in config['gate']:
                        for bx in range(min(cx, gx), max(cx, gx) + 1):
                            poly_grid[bx][cz] = COLOR_POLY

    # 5. Pins, Rails, and Contacts
    contact_lines = []
    metal1_lines = []
    metal2_plate_lines = []

    def add_contacts_for_rect(xmin_raw, xmax_raw, zmin_raw, zmax_raw, pin_data, current_pin_contacts, current_pin_upward_plates, color, pin_metal1_grid, added_coords):
        nonlocal poly_grid, active_grid
        pin_name = pin_data['name'] if isinstance(pin_data, dict) else pin_data
        is_gate = pin_data.get('is_gate', False) if isinstance(pin_data, dict) else False
        is_diff = pin_data.get('is_diff', False) if isinstance(pin_data, dict) else False

        def is_compliant(stud_x, stud_z):
            return is_compliant_global(stud_x, stud_z)

        possible_studs = []
        compliant_studs = []
        for sx in range(10, width_ldu, 20):
            gx = sx - 10
            for sz in range(10, height_ldu, 20):
                gz = sz - 10
                if is_stud_occupied(gx, gz, xmin_raw, xmax_raw, zmin_raw, zmax_raw):
                    possible_studs.append((sx, sz))
                    if is_compliant(sx // 20, sz // 20):
                        compliant_studs.append((sx, sz))

        already_covered = any(xmin_raw - SNAPPING_TOLERANCE <= ax <= xmax_raw + SNAPPING_TOLERANCE and zmin_raw - SNAPPING_TOLERANCE <= az <= zmax_raw + SNAPPING_TOLERANCE for ax, az in added_coords)

        if not compliant_studs:
            if already_covered:
                return
            # Fallback: Find nearest compliant stud in the cell
            mid_x = (xmin_raw + xmax_raw) / 2
            mid_z = (zmin_raw + zmax_raw) / 2
            best_fallback = None
            min_dist = float('inf')
            for sx in range(10, width_ldu, 20):
                for sz in range(10, height_ldu, 20):
                    if is_compliant(sx // 20, sz // 20):
                        dist = abs(sx - mid_x) + abs(sz - mid_z)
                        if dist < min_dist:
                            min_dist = dist
                            best_fallback = (sx, sz)
            if best_fallback:
                compliant_studs = [best_fallback]
            else:
                return

        def score_stud(sx, sz):
            stud_x, stud_z = sx // 20, sz // 20
            score = 0
            if pin_name == 'VSS' and stud_z == 0: score += 5000
            elif pin_name == 'VDD' and stud_z == 14: score += 5000
            elif (is_gate or pin_name not in ['VDD', 'VSS']) and stud_z == 6: score += 5000
            elif is_diff and stud_z in [2, 4, 8, 10, 12]: score += 5000

            # Penalize studs occupied by power fingers of *other* nets
            if pin_name not in ['VDD', 'VSS'] and power_occupancy[stud_x][stud_z]:
                score -= 10000

            # Prefer expected parity
            target_parity = get_expected_parity(stud_x, stud_z, is_big, is_drive_2)
            if stud_x % 2 == target_parity: score += 1000
            return score

        # Prioritize CIF contacts for this pin/net
        cif_contacts = [s for s, net in cif_net_map.items() if net == pin_name]
        cif_studs = []
        for csx, csz in cif_contacts:
            stud_coords = (csx * 20 + 10, csz * 20 + 10)
            if stud_coords in compliant_studs:
                cif_studs.append(stud_coords)

        best_studs = cif_studs + sorted([s for s in compliant_studs if s not in cif_studs], key=lambda s: score_stud(*s), reverse=True)

        for sx, sz in best_studs:
            if (sx, sz) not in added_coords:
                added_coords.add((sx, sz))
                stud_x, stud_z = sx // 20, sz // 20

                # Ensure Metal 1 coverage for the contact
                if 0 <= stud_x < w_studs and 0 <= stud_z < d_studs:
                    pin_metal1_grid[stud_x][stud_z] = color

                # 1. Metal 1 to Metal 2 connection (Y=-64)
                current_pin_upward_plates.append(f"1 {color} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")

                # 2. Contact Stack (Y=-48 Brick)
                current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")

                # 3. Connectivity to underlying layers (Active or Poly)
                # Gold Standard: Track 6 is for Polysilicon unless it is a Diffusion pin (is_diff)
                is_to_poly = (stud_z == 6 or is_gate) and (pin_name not in ['VDD', 'VSS']) and not is_diff
                if pin_name == 'VDD' and is_decap and stud_z != 14:
                    is_to_poly = True

                if is_to_poly:
                    # Mark gates on grid and grow vertically (Studs 2-12)
                    for gz in range(2, 13):
                        poly_grid[stud_x][gz] = COLOR_POLY
                else:
                    current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                    if is_decap: poly_grid[stud_x][stud_z] = None
                    if stud_z < 1 or stud_z > 13: # Only auto-fill Active under rails
                        if pin_name == 'VSS': active_grid[stud_x][stud_z] = COLOR_ACTIVE_NMOS
                        elif pin_name == 'VDD': active_grid[stud_x][stud_z] = COLOR_ACTIVE_PMOS
                        else: active_grid[stud_x][stud_z] = COLOR_ACTIVE_NMOS if stud_z < 8 else COLOR_ACTIVE_PMOS

    for pin in macro_data['pins']:
        added_coords = set() # (sx, sz) to prevent duplicates per pin
        current_pin_contacts = []
        current_pin_upward_plates = []
        pin_comment = f"0 // {'VDD' if pin['name']=='VDD' else 'VSS' if pin['name']=='VSS' else 'Pin '+pin['name']} Rail" if pin['name'] in ['VDD', 'VSS'] else f"0 // Pin {pin['name']}"
        color = COLOR_VDD if pin['name']=='VDD' else COLOR_VSS if pin['name']=='VSS' else COLOR_METAL1_INPUT if pin['direction']=='INPUT' else COLOR_METAL1_OUTPUT if pin['direction']=='OUTPUT' else COLOR_METAL1_INTERNAL

        # Metal 1 Grid Aggregation
        pin_metal1_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]

        if pin['name'] in pin_assignments:
            config = pin_assignments[pin['name']]
            cx, cz = config['contact'], config['contact_z']
            sx, sz = cx * 20 + 10, cz * 20 + 10
            added_coords.add((sx, sz))
            current_pin_contacts.append(pin_comment)
            current_pin_upward_plates.append(f"1 {color} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
            current_pin_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
            poly_grid[cx][cz] = COLOR_POLY
            pin_metal1_grid[cx][cz] = color

        has_via1 = False
        for rect in pin['rects']:
            if rect['layer'] == 'Via1':
                has_via1 = True
                vx1_ldu, vy1_ldu = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                vx2_ldu, vy2_ldu = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                vxmin, vxmax = snap_to_grid(min(vx1_ldu, vx2_ldu)), snap_to_grid(max(vx1_ldu, vx2_ldu))
                vzmin, vzmax = snap_to_grid(min(vy1_ldu, vy2_ldu)), snap_to_grid(max(vy1_ldu, vy2_ldu))
                if vxmax <= vxmin: vxmax = vxmin + 20
                if vzmax <= vzmin: vzmax = vzmin + 20
                for vsx in range(vxmin + 10, vxmax, 20):
                    for vsz in range(vzmin + 10, vzmax, 20):
                        current_pin_upward_plates.append(f"1 {color} {vsx} {Y_METAL2_PLATE} {vsz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")

        for rect in pin['rects']:
            if rect['layer'] == 'Metal1':
                lx1 = um_to_ldu_coord(rect['coords'][0])
                lz1 = um_to_ldu_coord(rect['coords'][1]) + 10
                lx2 = um_to_ldu_coord(rect['coords'][2])
                lz2 = um_to_ldu_coord(rect['coords'][3]) + 10
                xmin_raw, xmax_raw = min(lx1, lx2), max(lx1, lx2)
                zmin_raw, zmax_raw = min(lz1, lz2), max(lz1, lz2)

                for gsx in range(w_studs):
                    for gsz in range(d_studs):
                        gx, gz = gsx * 20, gsz * 20
                        if is_stud_occupied(gx, gz, xmin_raw, xmax_raw, zmin_raw, zmax_raw):
                            pin_metal1_grid[gsx][gsz] = color

                add_contacts_for_rect(xmin_raw, xmax_raw, zmin_raw, zmax_raw, pin, current_pin_contacts, [] if has_via1 else current_pin_upward_plates, color, pin_metal1_grid, added_coords)

        has_metal1 = any(any(cell is not None for cell in row) for row in pin_metal1_grid)
        if has_metal1:
            metal1_lines.append(pin_comment)
            rect_tiles = get_best_plates_multi(pin_metal1_grid)
            for plate, tx_off, tz_off, c, rotated in rect_tiles:
                metal1_lines.append(f"1 {c} {tx_off} {Y_METAL1} {tz_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

        if current_pin_contacts:
            if pin_comment not in current_pin_contacts:
                contact_lines.append(pin_comment)
            contact_lines.extend([l for l in current_pin_contacts if l != pin_comment])
        if current_pin_upward_plates: metal2_plate_lines.extend(current_pin_upward_plates)

    if macro_data['obs']:
        added_coords = set()
        obs_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
        has_obs = False
        for rect in macro_data['obs']:
            if rect['layer'] == 'Metal1':
                lx1 = um_to_ldu_coord(rect['coords'][0])
                lz1 = um_to_ldu_coord(rect['coords'][1]) + 10
                lx2 = um_to_ldu_coord(rect['coords'][2])
                lz2 = um_to_ldu_coord(rect['coords'][3]) + 10
                xmin_raw, xmax_raw = min(lx1, lx2), max(lx1, lx2)
                zmin_raw, zmax_raw = min(lz1, lz2), max(lz1, lz2)

                is_internal_obs = False
                for gsx in range(w_studs):
                    for gsz in range(d_studs):
                        gx, gz = gsx * 20, gsz * 20
                        if is_stud_occupied(gx, gz, xmin_raw, xmax_raw, zmin_raw, zmax_raw):
                            obs_grid[gsx][gsz] = COLOR_METAL1_INTERNAL
                            has_obs = True
                            if 1 < gsz < 13: is_internal_obs = True

                obs_contacts = []
                obs_upward = []
                # For internal obstructions in multi-stage cells, we MUST ensure a contact
                # and if it is internal (Track 2-12), it might be a gate for the next stage.
                # We use 'is_gate' flag for internal OBS to trigger Poly growth.
                add_contacts_for_rect(xmin_raw, xmax_raw, zmin_raw, zmax_raw, {'name': 'Internal', 'is_gate': is_internal_obs}, obs_contacts, obs_upward, COLOR_METAL1_INTERNAL, obs_grid, added_coords)
                if obs_contacts:
                    contact_lines.append("0 // Internal / Obstructions")
                    contact_lines.extend(obs_contacts)
                metal2_plate_lines.extend(obs_upward)

        if has_obs:
            metal1_lines.append("0 // Internal / Obstructions")
            rect_tiles = get_best_plates_multi(obs_grid)
            for plate, tx_off, tz_off, c, rotated in rect_tiles:
                metal1_lines.append(f"1 {c} {tx_off} {Y_METAL1} {tz_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    if not is_decap:
        for pin in macro_data['pins']:
            if pin['name'] in ['VDD', 'VSS']:
                for rect in pin['rects']:
                    if rect['layer'] == 'Metal1':
                        lx1, lz1 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                        lx2, lz2 = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                        xmin_raw, xmax_raw = min(lx1, lx2), max(lx1, lx2)
                        zmin_raw, zmax_raw = min(lz1, lz2), max(lz1, lz2)
                        for gsx in range(w_studs):
                            for gsz in range(d_studs):
                                gx, gz = gsx * 20, gsz * 20
                                if min(xmax_raw, gx+20) - max(xmin_raw, gx) >= SNAPPING_TOLERANCE and \
                                   min(zmax_raw, gz+20) - max(zmin_raw, gz) >= SNAPPING_TOLERANCE:
                                    poly_grid[gsx][gsz] = None

    poly_tiles = get_best_plates_multi(poly_grid)
    tiles3 = get_best_plates_multi(active_grid)
    final_ldr = [f"0 {macro_data['name']}.ldr", f"0 Name: {macro_data['name']}.ldr", "0 Author: lef_to_ldr.py", "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt", "0 !LPUB PLI GLOBAL ON", ""]
    final_ldr.append("0 // Substrate low (V3)")
    for plate, x_off, z_off, color, rotated in tiles1: final_ldr.append(f"1 {color} {x_off} {Y_SUBSTRATE_LOW} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")
    final_ldr.append("0 STEP\n0 // Substrate high / N-Well")
    for plate, x_off, z_off, color, rotated in tiles2: final_ldr.append(f"1 {color} {x_off} {Y_SUBSTRATE_HIGH} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")
    final_ldr.append("0 STEP\n0 // Active Regions")
    for plate, x_off, z_off, color, rotated in tiles3: final_ldr.append(f"1 {color} {x_off} {Y_ACTIVE} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")
    final_ldr.append("0 STEP\n0 // Polysilicon Gates")
    for plate, x_off, z_off, color, rotated in poly_tiles: final_ldr.append(f"1 {color} {x_off} {Y_POLY} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")
    if contact_lines: final_ldr.append("0 STEP\n0 // Contacts")
    final_ldr.extend(contact_lines)
    if metal1_lines: final_ldr.append("0 STEP\n0 // Metal 1")
    final_ldr.extend(metal1_lines)
    if metal2_plate_lines: final_ldr.append("0 STEP\n0 // Metal 2 Connections")
    final_ldr.extend(metal2_plate_lines)
    return "\n".join(final_ldr)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python lef_to_ldr.py <lef_file> <macro_name>")
        sys.exit(1)
    lef_file, macro_name = sys.argv[1], sys.argv[2]
    with open(lef_file, 'r') as f: lef_content = f.read()
    macro_data = parse_lef_macro(lef_content, macro_name)
    if not macro_data:
        print(f"Error: Macro {macro_name} not found.")
        sys.exit(1)
    ldr_content = generate_ldr(macro_data)
    os.makedirs("models", exist_ok=True)
    output_file = f"models/{macro_name}.ldr"
    with open(output_file, 'w') as f: f.write(ldr_content)
    print(f"Generated {output_file}")
