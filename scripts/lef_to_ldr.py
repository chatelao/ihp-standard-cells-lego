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
    if not grid: return []
    w_studs = len(grid)
    d_studs = len(grid[0])
    covered = [[False for _ in range(d_studs)] for _ in range(w_studs)]
    tiles = []
    sorted_plates = sorted(PLATES, key=lambda x: x[0]*x[1], reverse=True)
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
                        for iz in range(z, z+rd): covered[ix][iz] = True
                    x_off = x * 20 + (rw * 20) // 2
                    z_off = z * 20 + (rd * 20) // 2
                    tiles.append((pfile, x_off, z_off, color, rotated))
                else: covered[x][z] = True
    return tiles

def parse_cif(cif_path):
    if not os.path.exists(cif_path): return None
    with open(cif_path, 'r') as f: cif_content = f.read()
    layers = {}
    current_layer = None
    def to_ldr_x(val): return val * CIF_TO_LDU
    def to_ldr_z(val): return val * CIF_TO_LDU + 10
    commands = cif_content.split(';')
    for cmd in commands:
        cmd = cmd.strip()
        if not cmd: continue
        if cmd.startswith('L '):
            current_layer = cmd[2:].strip()
            if current_layer not in layers: layers[current_layer] = []
        elif cmd.startswith('B '):
            if current_layer:
                parts = re.split(r'\s+|,', cmd[2:].strip())
                if len(parts) >= 4:
                    try:
                        w_nm, h_nm, xc_nm, yc_nm = map(float, parts[:4])
                        layers[current_layer].append({'type': 'box', 'coords': [to_ldr_x(xc_nm - w_nm/2), to_ldr_z(yc_nm - h_nm/2), to_ldr_x(xc_nm + w_nm/2), to_ldr_z(yc_nm + h_nm/2)]})
                    except ValueError: continue
        elif cmd.startswith('P '):
            if current_layer:
                points_str = cmd[2:].strip().split()
                points = []
                for p in points_str:
                    pt = p.split(',')
                    if len(pt) == 2:
                        try: points.append((to_ldr_x(float(pt[0])), to_ldr_z(float(pt[1]))))
                        except ValueError: continue
                if points: layers[current_layer].append({'type': 'polygon', 'points': points})
        elif cmd.startswith('94 '):
            parts = cmd[3:].strip().split()
            if len(parts) >= 2:
                label_text = parts[0]
                coord_part = parts[1].split(',')
                if len(coord_part) == 2:
                    try:
                        if 'labels' not in layers: layers['labels'] = []
                        layers['labels'].append({'text': label_text, 'x': to_ldr_x(float(coord_part[0])), 'z': to_ldr_z(float(coord_part[1]))})
                    except ValueError: pass
    return layers

def parse_lef_macro(lef_content, macro_name):
    pattern = rf"(?<!PROPERTYDEFINITIONS\n  )MACRO\s+{macro_name}(.*?)END\s+{macro_name}"
    match = re.search(pattern, lef_content, re.DOTALL)
    if not match: return None
    body = match.group(1)
    size_match = re.search(r"SIZE\s+([\d\.]+)\s+BY\s+([\d\.]+)\s*;", body)
    width_um = float(size_match.group(1)) if size_match else 0
    height_um = float(size_match.group(2)) if size_match else 0
    pins = []
    pin_matches = re.finditer(r"PIN\s+([\w\[\]<>]+)(.*?)END\s+\1", body, re.DOTALL)
    for pin_match in pin_matches:
        pin_name, pin_body = pin_match.group(1), pin_match.group(2)
        direction_match = re.search(r"DIRECTION\s+(\w+)\s*;", pin_body)
        direction = direction_match.group(1) if direction_match else "UNKNOWN"
        is_gate, is_diff = "ANTENNAGATEAREA" in pin_body, "ANTENNADIFFAREA" in pin_body
        rects = []
        port_matches = re.finditer(r"PORT\s+(.*?)END", pin_body, re.DOTALL)
        for port_match in port_matches:
            port_body = port_match.group(1)
            layer_matches = re.finditer(r"LAYER\s+(\w+)\s*;(.*?)(?=LAYER|END|$)", port_body, re.DOTALL)
            for layer_match in layer_matches:
                layer_name, rect_content = layer_match.group(1), layer_match.group(2)
                layer_rects = re.findall(r"RECT\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s*;", rect_content)
                for r in layer_rects: rects.append({'layer': layer_name, 'coords': [float(x) for x in r]})
        pins.append({'name': pin_name, 'direction': direction, 'rects': rects, 'is_gate': is_gate, 'is_diff': is_diff})
    obs = []
    obs_match = re.search(r"OBS\s+(.*?)END", body, re.DOTALL)
    if obs_match:
        obs_body = obs_match.group(1)
        layer_matches = re.finditer(r"LAYER\s+(\w+)\s*;(.*?)(?=LAYER|END|$)", obs_body, re.DOTALL)
        for layer_match in layer_matches:
            layer_name, rect_content = layer_match.group(1), layer_match.group(2)
            layer_rects = re.findall(r"RECT\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s*;", rect_content)
            for r in layer_rects: obs.append({'layer': layer_name, 'coords': [float(x) for x in r]})
    return {'name': macro_name, 'width_um': width_um, 'height_um': height_um, 'pins': pins, 'obs': obs}

def snap_to_grid(value, grid=20): return int(round(value / grid) * grid)
def um_to_ldu_coord(um): return round(um * UM_TO_LDU)

def is_stud_occupied(gx, gz, xmin, xmax, zmin, zmax):
    overlap_x = min(xmax, gx + 20) - max(xmin, gx)
    overlap_z = min(zmax, gz + 20) - max(zmin, gz)
    if overlap_x <= 0 or overlap_z <= 0: return False
    center_x, center_z = (xmin + xmax) / 2, (zmin + zmax) / 2
    width, height = xmax - xmin, zmax - zmin
    is_occ_x = (gx <= center_x < gx + 20) if width <= 21.0 else (overlap_x >= SNAPPING_TOLERANCE)
    is_occ_z = (gz <= center_z < gz + 20) if height <= 21.0 else (overlap_z >= SNAPPING_TOLERANCE)
    return is_occ_x and is_occ_z

def is_point_in_poly(x, z, poly):
    n, inside = len(poly), False
    p1x, p1z = poly[0]
    for i in range(n + 1):
        p2x, p2z = poly[i % n]
        if z > min(p1z, p2z) and z <= max(p1z, p2z) and x <= max(p1x, p2x):
            xints = (z - p1z) * (p2x - p1x) / (p2z - p1z) + p1x if p1z != p2z else p1x
            if p1x == p2x or x <= xints: inside = not inside
        p1x, p1z = p2x, p2z
    return inside

def is_stud_occupied_geom(gx, gz, geom):
    if geom['type'] == 'box': return is_stud_occupied(gx, gz, *geom['coords'])
    if geom['type'] == 'polygon':
        poly = geom['points']
        xs, zs = [p[0] for p in poly], [p[1] for p in poly]
        xmin, zmin, xmax, zmax = min(xs), min(zs), max(xs), max(zs)
        if max(xmin, gx) >= min(xmax, gx+20) or max(zmin, gz) >= min(zmax, gz+20): return False
        if is_point_in_poly(gx + 10, gz + 10, poly): return True
        overlap_x, overlap_z = min(xmax, gx + 20) - max(xmin, gx), min(zmax, gz + 20) - max(zmin, gz)
        if overlap_x >= 3.0 and overlap_z >= 15.0: return True
        if overlap_x >= 15.0 and overlap_z >= 3.0: return True
        if overlap_x >= SNAPPING_TOLERANCE and overlap_z >= SNAPPING_TOLERANCE: return True
    return False

def get_expected_parity(stud_x, stud_z, is_big, is_drive_2):
    if stud_z in [0, 14]: return 0
    if not is_big: return 1
    return 1 if stud_x < 8 else 0

def generate_ldr(macro_data):
    cif_data = parse_cif(f"specifications/cells/{macro_data['name']}.cif")
    width_ldu = snap_to_grid(um_to_ldu_coord(macro_data['width_um']))
    if macro_data['name'] in ['sg13g2_nand2b_2', 'sg13g2_xor2_1']: width_ldu = 300
    height_ldu, w_studs, d_studs = 300, width_ldu // 20, 15
    ldr_lines = [f"0 {macro_data['name']}.ldr", f"0 Name: {macro_data['name']}.ldr", "0 Author: lef_to_ldr.py", "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt", "0 !LPUB PLI GLOBAL ON", "", "0 // Substrate low (V3)"]
    grid1 = [[COLOR_SUBSTRATE for _ in range(d_studs)] for _ in range(w_studs)]
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(grid1, prefer_rotated=True):
        ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_LOW} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    ldr_lines.append("0 STEP\n0 // Substrate high / N-Well")
    grid2 = [[COLOR_SUBSTRATE for _ in range(d_studs)] for _ in range(w_studs)]
    if cif_data and 'L14D0' in cif_data:
        for geom in cif_data['L14D0']:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i*20, k*20, geom): grid2[i][k] = COLOR_NWELL
    else:
        for i in range(w_studs):
            for k in range(8, d_studs): grid2[i][k] = COLOR_NWELL
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(grid2):
        ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_HIGH} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    ldr_lines.append("0 STEP\n0 // Active Regions")
    active_grid = [[grid2[x][z] for z in range(d_studs)] for x in range(w_studs)]
    if cif_data and 'L1D0' in cif_data:
        for geom in cif_data['L1D0']:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i*20, k*20, geom): active_grid[i][k] = COLOR_ACTIVE_PMOS if grid2[i][k] == COLOR_NWELL else COLOR_ACTIVE_NMOS
    else:
        active_studs = max(1, w_studs - 2)
        xs, xe = (w_studs - active_studs) // 2, (w_studs - active_studs) // 2 + active_studs
        for x in range(xs, xe):
            for z in range(2, 5): active_grid[x][z] = COLOR_ACTIVE_NMOS
            for z in range(8, 13): active_grid[x][z] = COLOR_ACTIVE_PMOS
    if macro_data['name'] == 'sg13g2_nand2b_2':
        for z in [8, 10, 12]: active_grid[3][z] = COLOR_NWELL
        for z in [2, 4]: active_grid[4][z] = COLOR_SUBSTRATE
    for x in range(w_studs):
        active_grid[x][0] = COLOR_ACTIVE_NMOS
        active_grid[x][14] = COLOR_ACTIVE_PMOS
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(active_grid):
        ldr_lines.append(f"1 {color} {x_off} {Y_ACTIVE} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    ldr_lines.append("0 STEP\n0 // Polysilicon Gates")
    is_decap, is_drive_2, is_big = 'decap' in macro_data['name'].lower(), macro_data['name'].endswith('_2'), w_studs > 7
    poly_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
    if cif_data and 'L5D0' in cif_data:
        for geom in cif_data['L5D0']:
            for i in range(w_studs):
                for k in range(1, 14):
                    if is_stud_occupied_geom(i*20, k*20, geom): poly_grid[i][k] = COLOR_POLY

    power_occupancy, power_metal1_grid = [[False for _ in range(d_studs)] for _ in range(w_studs)], [[None for _ in range(d_studs)] for _ in range(w_studs)]
    for pin in macro_data['pins']:
        if pin['name'] in ['VDD', 'VSS']:
            for rect in pin['rects']:
                if rect['layer'] == 'Metal1':
                    xmin, zmin = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                    xmax, zmax = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                    for i in range(w_studs):
                        for k in range(d_studs):
                            if is_stud_occupied(i*20, k*20, min(xmin, xmax), max(xmin, xmax), min(zmin, zmax), max(zmin, zmax)):
                                power_occupancy[i][k] = True
                                power_metal1_grid[i][k] = COLOR_VDD if pin['name'] == 'VDD' else COLOR_VSS

    def is_compliant_global(sx, sz):
        if sz % 2 != 0 or sx % 2 != get_expected_parity(sx, sz, is_big, is_drive_2): return False
        return sz in [0, 14] or not power_occupancy[sx][sz]

    cif_net_map = {}
    if cif_data and 'L8D0' in cif_data:
        cif_m1_to_net, net_sources = [], []
        for pin in macro_data['pins']:
            for rect in pin['rects']:
                if rect['layer'] == 'Metal1':
                    lx1, lz1 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1]) + 10
                    lx2, lz2 = um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3]) + 10
                    net_sources.append({'coords': [min(lx1, lx2), min(lz1, lz2), max(lx1, lx2), max(lz1, lz2)], 'net': pin['name']})
        if 'L8D2' in cif_data:
            for geom in cif_data['L8D2']:
                if geom['type'] == 'box':
                    xmin, zmin, xmax, zmax = geom['coords']
                    matched_label = None
                    if 'labels' in cif_data:
                        for label in cif_data['labels']:
                            if xmin-5 <= label['x'] <= xmax+5 and zmin-5 <= label['z'] <= zmax+5:
                                matched_label = label['text']
                                break
                    if matched_label: net_sources.append({'coords': geom['coords'], 'net': matched_label})
        for geom in cif_data['L8D0']:
            xs = [p[0] for p in geom['points']] if geom['type'] == 'polygon' else [geom['coords'][0], geom['coords'][2]]
            zs = [p[1] for p in geom['points']] if geom['type'] == 'polygon' else [geom['coords'][1], geom['coords'][3]]
            xmin, zmin, xmax, zmax, matched_net, max_overlap = min(xs), min(zs), max(xs), max(zs), "Internal", 0
            for src in net_sources:
                overlap_x, overlap_z = min(xmax, src['coords'][2]) - max(xmin, src['coords'][0]), min(zmax, src['coords'][3]) - max(zmin, src['coords'][1])
                if overlap_x > 0 and overlap_z > 0 and overlap_x * overlap_z > max_overlap:
                    max_overlap = overlap_x * overlap_z
                    matched_net = src['net']
            cif_m1_to_net.append((geom, matched_net))
        if 'L6D0' in cif_data:
            for c_geom in cif_data['L6D0']:
                cx, cz = (c_geom['coords'][0] + c_geom['coords'][2]) / 2, (c_geom['coords'][1] + c_geom['coords'][3]) / 2
                for m1_geom, net_name in cif_m1_to_net:
                    is_inside = is_point_in_poly(cx, cz, m1_geom['points']) if m1_geom['type'] == 'polygon' else (m1_geom['coords'][0] <= cx <= m1_geom['coords'][2] and m1_geom['coords'][1] <= cz <= m1_geom['coords'][3])
                    if is_inside:
                        best_stud, min_dist = None, float('inf')
                        for i in range(w_studs):
                            for k in range(d_studs):
                                if is_compliant_global(i, k):
                                    dist = abs(i*20+10 - cx) + abs(k*20+10 - cz)
                                    if dist < min_dist: min_dist, best_stud = dist, (i, k)
                        if best_stud: cif_net_map[best_stud] = net_name
                        break

    input_pins = sorted([p for p in macro_data['pins'] if p['direction'] == 'INPUT'], key=lambda p: next(( (r['coords'][0]+r['coords'][2])/2 for r in p['rects'] if r['layer']=='Metal1'), 0))
    pin_assignments = {}
    for j, pin in enumerate(input_pins):
        ideal_x, cif_contacts = 4*j + 1, [s for s, net in cif_net_map.items() if net == pin['name']]
        if cif_contacts: best_c = min(cif_contacts, key=lambda s: abs(s[1]-6)*10 + abs(s[0]-ideal_x))
        else:
            possible = []
            for rect in [r for r in pin['rects'] if r['layer']=='Metal1']:
                lx1, lz1, lx2, lz2 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1])+10, um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3])+10
                for i in range(w_studs):
                    if min(lx1, lx2) <= i*20+10 <= max(lx1, lx2):
                        for k in range(d_studs):
                            if min(lz1, lz2) <= k*20+10 <= max(lz1, lz2): possible.append((i, k))
            compliant = [s for s in possible if is_compliant_global(s[0], s[1])]
            if not compliant:
                best_c, min_dist = None, float('inf')
                for i in range(w_studs):
                    for k in range(0, d_studs, 2):
                        if is_compliant_global(i, k):
                            dist = abs(k-6)*10 + abs(i-ideal_x)
                            if dist < min_dist: min_dist, best_c = dist, (i, k)
            else:
                at_6 = [s for s in compliant if s[1]==6]
                best_c = min(at_6 if at_6 else compliant, key=lambda s: abs(s[0]-ideal_x) if at_6 else abs(s[1]-6)*10 + abs(s[0]-ideal_x))
        def get_valid_gate(tx):
            if 0 <= tx < w_studs and not any(power_occupancy[tx][z] for z in range(2, 13)): return tx
            for o in [1, -1, 2, -2]:
                if 0 <= tx+o < w_studs and not any(power_occupancy[tx+o][z] for z in range(2, 13)): return tx+o
            return tx
        if is_drive_2 or is_big: gates, pad_x, pad_part = [get_valid_gate(best_c[0]-1), get_valid_gate(best_c[0]+1)], best_c[0]*20+10, '3623.dat'
        else: g = get_valid_gate(best_c[0]+1); gates, pad_x, pad_part = [g], ((best_c[0]+g)/2)*20+10, '3023.dat'
        pin_assignments[pin['name']] = {'gate': gates, 'contact': best_c[0], 'contact_z': best_c[1], 'pad_x': pad_x, 'pad_part': pad_part}

    if not (cif_data and 'L5D0' in cif_data):
        if is_decap:
            for x in range(max(1, w_studs-2)):
                for z in range(2, 13): poly_grid[x+(w_studs-max(1, w_studs-2))//2][z] = COLOR_POLY
        else:
            for pin in input_pins:
                cfg = pin_assignments[pin['name']]
                for gs in cfg['gate']:
                    for gz in range(2, 13): poly_grid[gs][gz] = COLOR_POLY
                poly_grid[cfg['contact']][cfg['contact_z']] = COLOR_POLY
                for gx in cfg['gate']:
                    for bx in range(min(cfg['contact'], gx), max(cfg['contact'], gx)+1): poly_grid[bx][cfg['contact_z']] = COLOR_POLY

    contact_lines, metal1_lines, metal2_plate_lines = [], [], []
    def add_contacts_for_rect(xmin_raw, xmax_raw, zmin_raw, zmax_raw, pin_data, cur_contacts, cur_upward, col, pin_m1_grid, added):
        p_name = pin_data['name'] if isinstance(pin_data, dict) else pin_data
        is_g, is_d = (pin_data.get('is_gate', False), pin_data.get('is_diff', False)) if isinstance(pin_data, dict) else (False, False)
        possible, compliant = [], []
        for sx in range(10, width_ldu, 20):
            for sz in range(10, height_ldu, 20):
                if is_stud_occupied(sx-10, sz-10, xmin_raw, xmax_raw, zmin_raw, zmax_raw):
                    possible.append((sx, sz))
                    if is_compliant_global(sx // 20, sz // 20): compliant.append((sx, sz))
        if not compliant:
            if any(xmin_raw-9 <= ax <= xmax_raw+9 and zmin_raw-9 <= az <= zmax_raw+9 for ax, az in added): return
            best_fb, min_d = None, float('inf')
            for sx in range(10, width_ldu, 20):
                for sz in range(10, height_ldu, 20):
                    if is_compliant_global(sx//20, sz//20):
                        dist = abs(sx-(xmin_raw+xmax_raw)/2) + abs(sz-(zmin_raw+zmax_raw)/2)
                        if dist < min_d: min_d, best_fb = dist, (sx, sz)
            if best_fb: compliant = [best_fb]
            else: return
        def score_stud(sx, sz):
            stx, stz, score = sx // 20, sz // 20, 0
            if p_name == 'VSS' and stz == 0: score += 5000
            elif p_name == 'VDD' and stz == 14: score += 5000
            elif (is_g or p_name not in ['VDD', 'VSS']) and stz == 6: score += 5000
            elif is_d and stz in [2, 4, 8, 10, 12]: score += 5000
            if p_name not in ['VDD', 'VSS'] and power_occupancy[stx][stz]: score -= 10000
            if ((stz == 6 or is_g) and p_name not in ['VDD', 'VSS'] and not is_d) and poly_grid[stx][stz] == COLOR_POLY: score += 2000
            if stx % 2 == get_expected_parity(stx, stz, is_big, is_drive_2): score += 1000
            return score
        cif_c = [s for s, net in cif_net_map.items() if net == p_name]
        cif_s = [(csx*20+10, csz*20+10) for csx, csz in cif_c if (csx*20+10, csz*20+10) in compliant]
        best_s = cif_s if cif_data else cif_s + sorted([s for s in compliant if s not in cif_s], key=lambda s: score_stud(*s), reverse=True)
        for sx, sz in best_s:
            if (sx, sz) not in added:
                added.add((sx, sz))
                stx, stz = sx // 20, sz // 20
                if 0 <= stx < w_studs and 0 <= stz < d_studs: pin_m1_grid[stx][stz] = col
                cur_upward.append(f"1 {col} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
                cur_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                if (cif_data and poly_grid[stx][stz] == COLOR_POLY) or (not cif_data and (stz == 6 or is_g) and p_name not in ['VDD', 'VSS'] and not is_d):
                    if not (cif_data and 'L5D0' in cif_data) or any(poly_grid[stx][gz] == COLOR_POLY for gz in range(1, 14)):
                        for gz in range(2, 13): poly_grid[stx][gz] = COLOR_POLY
                else:
                    cur_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                    if is_decap: poly_grid[stx][stz] = None
                    if stz < 1 or stz > 13:
                        if p_name == 'VSS': active_grid[stx][stz] = COLOR_ACTIVE_NMOS
                        elif p_name == 'VDD': active_grid[stx][stz] = COLOR_ACTIVE_PMOS
                        else: active_grid[stx][stz] = COLOR_ACTIVE_NMOS if stz < 8 else COLOR_ACTIVE_PMOS

    for pin in macro_data['pins']:
        added, cur_contacts, cur_upward, col = set(), [], [], (COLOR_VDD if pin['name']=='VDD' else COLOR_VSS if pin['name']=='VSS' else COLOR_METAL1_INPUT if pin['direction']=='INPUT' else COLOR_METAL1_OUTPUT if pin['direction']=='OUTPUT' else COLOR_METAL1_INTERNAL)
        pin_m1_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
        if pin['name'] in pin_assignments:
            cfg = pin_assignments[pin['name']]
            sx, sz = cfg['contact']*20+10, cfg['contact_z']*20+10
            added.add((sx, sz))
            cur_upward.append(f"1 {col} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
            cur_contacts.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
            poly_grid[cfg['contact']][cfg['contact_z']], pin_m1_grid[cfg['contact']][cfg['contact_z']] = COLOR_POLY, col

        has_v1 = False
        if cif_data and 'L8D2' in cif_data:
            for geom in cif_data['L8D2']:
                if geom['type'] == 'box':
                    xmin, zmin, xmax, zmax = geom['coords']
                    is_this = False
                    if 'labels' in cif_data:
                        for lbl in cif_data['labels']:
                            if xmin-5 <= lbl['x'] <= xmax+5 and zmin-5 <= lbl['z'] <= zmax+5 and lbl['text'] == pin['name']: is_this = True; break
                    if is_this:
                        has_v1 = True
                        for vsx in range(snap_to_grid(xmin)+10, snap_to_grid(xmax), 20):
                            for vsz in range(snap_to_grid(zmin)+10, snap_to_grid(zmax), 20): cur_upward.append(f"1 {col} {vsx} {Y_METAL2_PLATE} {vsz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
        else:
            for rect in [r for r in pin['rects'] if r['layer'] == 'Via1']:
                has_v1 = True
                vx1, vy1, vx2, vy2 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1])+10, um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3])+10
                vxmin, vxmax, vzmin, vzmax = snap_to_grid(min(vx1, vx2)), snap_to_grid(max(vx1, vx2)), snap_to_grid(min(vy1, vy2)), snap_to_grid(max(vy1, vy2))
                if vxmax <= vxmin: vxmax = vxmin + 20
                if vzmax <= vzmin: vzmax = vzmin + 20
                for vsx in range(vxmin+10, vxmax, 20):
                    for vsz in range(vzmin+10, vzmax, 20): cur_upward.append(f"1 {col} {vsx} {Y_METAL2_PLATE} {vsz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")

        if cif_data and 'L8D0' in cif_data:
            for m1_geom, net in cif_m1_to_net:
                if net == pin['name']:
                    xs, zs = ([p[0] for p in m1_geom['points']] if m1_geom['type']=='polygon' else [m1_geom['coords'][0], m1_geom['coords'][2]]), ([p[1] for p in m1_geom['points']] if m1_geom['type']=='polygon' else [m1_geom['coords'][1], m1_geom['coords'][3]])
                    for gsx in range(w_studs):
                        for gsz in range(d_studs):
                            if is_stud_occupied_geom(gsx*20, gsz*20, m1_geom): pin_m1_grid[gsx][gsz] = col
                    add_contacts_for_rect(min(xs), max(xs), min(zs), max(zs), pin, cur_contacts, [] if has_v1 else cur_upward, col, pin_m1_grid, added)
        else:
            for rect in [r for r in pin['rects'] if r['layer'] == 'Metal1']:
                lx1, lz1, lx2, lz2 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1])+10, um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3])+10
                xmin, xmax, zmin, zmax = min(lx1, lx2), max(lx1, lx2), min(lz1, lz2), max(lz1, lz2)
                for gsx in range(w_studs):
                    for gsz in range(d_studs):
                        if is_stud_occupied(gsx*20, gsz*20, xmin, xmax, zmin, zmax): pin_m1_grid[gsx][gsz] = col
                add_contacts_for_rect(xmin, xmax, zmin, zmax, pin, cur_contacts, [] if has_v1 else cur_upward, col, pin_m1_grid, added)
        if any(any(c is not None for c in row) for row in pin_m1_grid):
            metal1_lines.append(f"0 // {'VDD' if pin['name']=='VDD' else 'VSS' if pin['name']=='VSS' else 'Pin '+pin['name']} Rail" if pin['name'] in ['VDD', 'VSS'] else f"0 // Pin {pin['name']}")
            for plate, tx, tz, c, rot in get_best_plates_multi(pin_m1_grid): metal1_lines.append(f"1 {c} {tx} {Y_METAL1} {tz} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")
        if cur_contacts:
            lbl = f"0 // {'VDD' if pin['name']=='VDD' else 'VSS' if pin['name']=='VSS' else 'Pin '+pin['name']} Rail" if pin['name'] in ['VDD', 'VSS'] else f"0 // Pin {pin['name']}"
            contact_lines.append(lbl); contact_lines.extend(cur_contacts)
        metal2_plate_lines.extend(cur_upward)

    if cif_data and 'L8D0' in cif_data:
        added, obs_grid, has_obs = set(), [[None for _ in range(d_studs)] for _ in range(w_studs)], False
        for m1_geom, net in cif_m1_to_net:
            if net == "Internal":
                has_obs = True
                xs, zs = ([p[0] for p in m1_geom['points']] if m1_geom['type']=='polygon' else [m1_geom['coords'][0], m1_geom['coords'][2]]), ([p[1] for p in m1_geom['points']] if m1_geom['type']=='polygon' else [m1_geom['coords'][1], m1_geom['coords'][3]])
                is_int_obs = False
                for gsx in range(w_studs):
                    for gsz in range(d_studs):
                        if is_stud_occupied_geom(gsx*20, gsz*20, m1_geom):
                            obs_grid[gsx][gsz] = COLOR_METAL1_INTERNAL
                            if 1 < gsz < 13: is_int_obs = True
                cur_c, cur_u = [], []
                add_contacts_for_rect(min(xs), max(xs), min(zs), max(zs), {'name': 'Internal', 'is_gate': is_int_obs}, cur_c, cur_u, COLOR_METAL1_INTERNAL, obs_grid, added)
                if cur_c: contact_lines.append("0 // Internal / Obstructions"); contact_lines.extend(cur_c)
                metal2_plate_lines.extend(cur_u)
    elif macro_data['obs']:
        added, obs_grid, has_obs = set(), [[None for _ in range(d_studs)] for _ in range(w_studs)], False
        for rect in [r for r in macro_data['obs'] if r['layer']=='Metal1']:
            lx1, lz1, lx2, lz2 = um_to_ldu_coord(rect['coords'][0]), um_to_ldu_coord(rect['coords'][1])+10, um_to_ldu_coord(rect['coords'][2]), um_to_ldu_coord(rect['coords'][3])+10
            is_int_obs = False
            for gsx in range(w_studs):
                for gsz in range(d_studs):
                    if is_stud_occupied(gsx*20, gsz*20, min(lx1, lx2), max(lx1, lx2), min(lz1, lz2), max(lz1, lz2)):
                        obs_grid[gsx][gsz], has_obs = COLOR_METAL1_INTERNAL, True
                        if 1 < gsz < 13: is_int_obs = True
            cur_c, cur_u = [], []
            add_contacts_for_rect(min(lx1, lx2), max(lx1, lx2), min(lz1, lz2), max(lz1, lz2), {'name': 'Internal', 'is_gate': is_int_obs}, cur_c, cur_u, COLOR_METAL1_INTERNAL, obs_grid, added)
            if cur_c: contact_lines.append("0 // Internal / Obstructions"); contact_lines.extend(cur_c)
            metal2_plate_lines.extend(cur_u)
    if any(any(c is not None for c in row) for row in obs_grid):
        metal1_lines.append("0 // Internal / Obstructions")
        for plate, tx, tz, c, rot in get_best_plates_multi(obs_grid): metal1_lines.append(f"1 {c} {tx} {Y_METAL1} {tz} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")

    if not (cif_data and 'L5D0' in cif_data):
        for x in range(w_studs):
            for z in range(d_studs):
                if power_occupancy[x][z]: poly_grid[x][z] = None

    final_ldr = [f"0 {macro_data['name']}.ldr", f"0 Name: {macro_data['name']}.ldr", "0 Author: lef_to_ldr.py", "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt", "0 !LPUB PLI GLOBAL ON", "", "0 // Substrate low (V3)"]
    for p, x, z, c, r in get_best_plates_multi(grid1, prefer_rotated=True): final_ldr.append(f"1 {c} {x} {Y_SUBSTRATE_LOW} {z} {'0 0 1 0 1 0 -1 0 0' if r else '1 0 0 0 1 0 0 0 1'} {p}")
    final_ldr.append("0 STEP\n0 // Substrate high / N-Well")
    for p, x, z, c, r in get_best_plates_multi(grid2): final_ldr.append(f"1 {c} {x} {Y_SUBSTRATE_HIGH} {z} {'0 0 1 0 1 0 -1 0 0' if r else '1 0 0 0 1 0 0 0 1'} {p}")
    final_ldr.append("0 STEP\n0 // Active Regions")
    for p, x, z, c, r in get_best_plates_multi(active_grid): final_ldr.append(f"1 {c} {x} {Y_ACTIVE} {z} {'0 0 1 0 1 0 -1 0 0' if r else '1 0 0 0 1 0 0 0 1'} {p}")
    final_ldr.append("0 STEP\n0 // Polysilicon Gates")
    for p, x, z, c, r in get_best_plates_multi(poly_grid): final_ldr.append(f"1 {c} {x} {Y_POLY} {z} {'0 0 1 0 1 0 -1 0 0' if r else '1 0 0 0 1 0 0 0 1'} {p}")
    if contact_lines: final_ldr.append("0 STEP\n0 // Contacts"); final_ldr.extend(contact_lines)
    if metal1_lines: final_ldr.append("0 STEP\n0 // Metal 1"); final_ldr.extend(metal1_lines)
    if metal2_plate_lines: final_ldr.append("0 STEP\n0 // Metal 2 Connections"); final_ldr.extend(metal2_plate_lines)
    return "\n".join(final_ldr)

if __name__ == "__main__":
    if len(sys.argv) < 3: sys.exit(1)
    lef_file, macro_name = sys.argv[1], sys.argv[2]
    with open(lef_file, 'r') as f: lef_content = f.read()
    macro_data = parse_lef_macro(lef_content, macro_name)
    if not macro_data: sys.exit(1)
    ldr_content = generate_ldr(macro_data)
    os.makedirs("models", exist_ok=True)
    with open(f"models/{macro_name}.ldr", 'w') as f: f.write(ldr_content)
    print(f"Generated models/{macro_name}.ldr")
