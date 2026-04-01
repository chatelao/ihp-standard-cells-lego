import math
import re
import sys
import os

# Constants based on modeling_guidelines.md (V3)
# 1 stud = 0.27 um = 20 LDU
# 1 LDU = 13.5 nm
UM_TO_LDU = 20 / 0.27
CIF_TO_LDU = 20 / 270 # 1 unit = 1 nm, 270 nm = 20 LDU

# LEGO Part IDs (Standard orientations are usually X-aligned)
PLATES = [
    (16, 16, "91405.dat"), (16, 8, "92438.dat"), (16, 6, "3027.dat"),
    (14, 6, "3456.dat"), (12, 6, "3028.dat"), (10, 6, "3033.dat"),
    (12, 4, "3029.dat"), (8, 6, "3036.dat"), (10, 4, "3030.dat"),
    (6, 6, "3958.dat"), (16, 2, "4282.dat"), (8, 4, "3035.dat"),
    (12, 2, "2445.dat"), (6, 4, "3032.dat"), (10, 2, "3832.dat"),
    (8, 2, "3034.dat"), (4, 4, "3031.dat"), (12, 1, "60479.dat"),
    (6, 2, "3795.dat"), (10, 1, "4477.dat"), (8, 1, "3460.dat"),
    (4, 2, "3020.dat"), (6, 1, "3666.dat"), (3, 2, "3021.dat"),
    (4, 1, "3710.dat"), (2, 2, "3022.dat"), (3, 1, "3623.dat"),
    (2, 1, "3023.dat"), (1, 1, "3024.dat"),
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

SNAPPING_TOLERANCE = 9.0

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
                        for iz in range(z, z+rd):
                            covered[ix][iz] = True
                    x_off = x * 20 + (rw * 20) // 2
                    z_off = z * 20 + (rd * 20) // 2
                    tiles.append((pfile, x_off, z_off, color, rotated))
                else:
                    covered[x][z] = True
    return tiles

def parse_cif(cif_path):
    if not os.path.exists(cif_path): return None
    with open(cif_path, 'r') as f: cif_content = f.read()
    layers = {}
    labels = []
    boundary = None
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
            parts = re.split(r'\s+|,', cmd[2:].strip())
            if len(parts) >= 4:
                try:
                    w_nm, h_nm, xc_nm, yc_nm = map(float, parts[:4])
                    x1, z1 = to_ldr_x(xc_nm - w_nm/2), to_ldr_z(yc_nm - h_nm/2)
                    x2, z2 = to_ldr_x(xc_nm + w_nm/2), to_ldr_z(yc_nm + h_nm/2)
                    geom = {'type': 'box', 'coords': [x1, z1, x2, z2]}
                    if current_layer == 'L189D4': boundary = geom
                    elif current_layer: layers[current_layer].append(geom)
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
            parts = re.split(r'\s+', cmd[3:].strip())
            if len(parts) >= 2:
                name = parts[0]
                coords = parts[1].split(',')
                if len(coords) == 2:
                    try: labels.append({'name': name, 'x': to_ldr_x(float(coords[0])), 'z': to_ldr_z(float(coords[1]))})
                    except ValueError: pass
    return {'layers': layers, 'labels': labels, 'boundary': boundary}

def is_point_in_poly(x, z, poly):
    n, inside = len(poly), False
    p1x, p1z = poly[0]
    for i in range(n + 1):
        p2x, p2z = poly[i % n]
        if z > min(p1z, p2z) and z <= max(p1z, p2z) and x <= max(p1x, p2x):
            if p1z != p2z:
                xints = (z - p1z) * (p2x - p1x) / (p2z - p1z) + p1x
                if p1x == p2x or x <= xints: inside = not inside
        p1x, p1z = p2x, p2z
    return inside

def is_stud_occupied(gx, gz, xmin, xmax, zmin, zmax):
    overlap_x = min(xmax, gx + 20) - max(xmin, gx)
    overlap_z = min(zmax, gz + 20) - max(zmin, gz)
    if overlap_x <= 0 or overlap_z <= 0: return False
    center_x, center_z = (xmin + xmax) / 2, (zmin + zmax) / 2
    width, height = xmax - xmin, zmax - zmin
    is_occ_x = (gx <= center_x < gx + 20) if width <= 21.0 else (overlap_x >= SNAPPING_TOLERANCE)
    is_occ_z = (gz <= center_z < gz + 20) if height <= 21.0 else (overlap_z >= SNAPPING_TOLERANCE)
    return is_occ_x and is_occ_z

def is_stud_occupied_geom(gx, gz, geom):
    if geom['type'] == 'box':
        xmin, zmin, xmax, zmax = geom['coords']
        return is_stud_occupied(gx, gz, xmin, xmax, zmin, zmax)
    if geom['type'] == 'polygon':
        poly = geom['points']
        xs, zs = [p[0] for p in poly], [p[1] for p in poly]
        xmin, zmin, xmax, zmax = min(xs), min(zs), max(xs), max(zs)
        if max(xmin, gx) >= min(xmax, gx+20) or max(zmin, gz) >= min(zmax, gz+20): return False
        if is_point_in_poly(gx + 10, gz + 10, poly): return True
    return False

def get_expected_parity(stud_x, stud_z, is_big):
    if stud_z in [0, 14]: return 0
    if not is_big: return 1
    return 1 if stud_x < 8 else 0

def generate_ldr(cif_data, cell_name):
    boundary = cif_data['boundary']
    width_ldu = int(round((boundary['coords'][2] - boundary['coords'][0]) / 20) * 20) if boundary else 0
    if not width_ldu: width_ldu = 240 # Fallback
    height_ldu = 300
    w_studs, d_studs = width_ldu // 20, height_ldu // 20
    is_big = w_studs > 7

    ldr_lines = [f"0 {cell_name}.ldr", f"0 Name: {cell_name}.ldr", "0 Author: cif_to_ldr.py", "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt", "0 !LPUB PLI GLOBAL ON", ""]

    # 1. Substrate
    ldr_lines.append("0 // Substrate low")
    grid1 = [[COLOR_SUBSTRATE for _ in range(d_studs)] for _ in range(w_studs)]
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(grid1, True):
        ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_LOW} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 2. Substrate High / N-Well
    ldr_lines.append("0 STEP\n0 // Substrate high / N-Well")
    grid2 = [[COLOR_SUBSTRATE for _ in range(d_studs)] for _ in range(w_studs)]
    if 'L14D0' in cif_data['layers']:
        for geom in cif_data['layers']['L14D0']:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i*20, k*20, geom): grid2[i][k] = COLOR_NWELL
    else: # Fallback to Track 8 split
        for i in range(w_studs):
            for k in range(8, d_studs): grid2[i][k] = COLOR_NWELL
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(grid2):
        ldr_lines.append(f"1 {color} {x_off} {Y_SUBSTRATE_HIGH} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 3. Active
    ldr_lines.append("0 STEP\n0 // Active Regions")
    active_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
    if 'L1D0' in cif_data['layers']:
        for geom in cif_data['layers']['L1D0']:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i*20, k*20, geom):
                        active_grid[i][k] = COLOR_ACTIVE_PMOS if grid2[i][k] == COLOR_NWELL else COLOR_ACTIVE_NMOS
    # Fill under rails
    for i in range(w_studs):
        active_grid[i][0] = COLOR_ACTIVE_NMOS
        active_grid[i][14] = COLOR_ACTIVE_PMOS
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(active_grid):
        ldr_lines.append(f"1 {color} {x_off} {Y_ACTIVE} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 4. Poly
    ldr_lines.append("0 STEP\n0 // Polysilicon Gates")
    poly_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
    if 'L5D0' in cif_data['layers']:
        for geom in cif_data['layers']['L5D0']:
            for i in range(w_studs):
                for k in range(1, 14):
                    if is_stud_occupied_geom(i*20, k*20, geom): poly_grid[i][k] = COLOR_POLY
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(poly_grid):
        ldr_lines.append(f"1 {color} {x_off} {Y_POLY} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 5. Labels & Nets mapping
    net_map = {} # label_name -> list of geoms
    for label in cif_data['labels']:
        lx, lz = label['x'], label['z']
        matched = False
        if 'L8D0' in cif_data['layers']:
            for geom in cif_data['layers']['L8D0']:
                if geom['type'] == 'box':
                    x1, z1, x2, z2 = geom['coords']
                    if x1-5 <= lx <= x2+5 and z1-5 <= lz <= z2+5:
                        if label['name'] not in net_map: net_map[label['name']] = []
                        net_map[label['name']].append(geom)
                        matched = True
                elif geom['type'] == 'polygon':
                    if is_point_in_poly(lx, lz, geom['points']):
                        if label['name'] not in net_map: net_map[label['name']] = []
                        net_map[label['name']].append(geom)
                        matched = True

    # Metal 1 Grid & Contacts
    metal1_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
    contact_lines = []
    metal2_lines = []

    # 6. Contacts
    if 'L6D0' in cif_data['layers']:
        ldr_lines.append("0 STEP\n0 // Contacts")
        added_contacts = set()
        for geom in cif_data['layers']['L6D0']:
            if geom['type'] == 'box':
                x1, z1, x2, z2 = geom['coords']
                cx, cz = (x1 + x2) / 2, (z1 + z2) / 2
                best_stud = None
                min_dist = float('inf')
                for i in range(w_studs):
                    for k in range(d_studs):
                        sx, sz = i * 20 + 10, k * 20 + 10
                        target_parity = get_expected_parity(i, k, is_big)
                        if (k % 2 == 0) and (i % 2 == target_parity):
                            dist = abs(sx - cx) + abs(sz - cz)
                            if dist < min_dist: min_dist, best_stud = dist, (i, k)
                if best_stud and best_stud not in added_contacts:
                    added_contacts.add(best_stud)
                    sx, sz = best_stud[0]*20+10, best_stud[1]*20+10
                    contact_lines.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                    if poly_grid[best_stud[0]][best_stud[1]] is None: # Not poly, so must be active
                         contact_lines.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                    # Also ensure Metal 2 plate
                    # Determine color from net
                    color = COLOR_METAL1_INTERNAL
                    for net_name, geoms in net_map.items():
                        for m_geom in geoms:
                            if m_geom['type'] == 'box':
                                mx1, mz1, mx2, mz2 = m_geom['coords']
                                if mx1-10 <= cx <= mx2+10 and mz1-10 <= cz <= mz2+10:
                                    if net_name == 'VDD': color = COLOR_VDD
                                    elif net_name == 'VSS': color = COLOR_VSS
                                    elif net_name == 'X' or net_name == 'Y': color = COLOR_METAL1_OUTPUT
                                    else: color = COLOR_METAL1_INPUT
                                    break
                            elif m_geom['type'] == 'polygon':
                                if is_point_in_poly(cx, cz, m_geom['points']):
                                    if net_name == 'VDD': color = COLOR_VDD
                                    elif net_name == 'VSS': color = COLOR_VSS
                                    elif net_name == 'X' or net_name == 'Y': color = COLOR_METAL1_OUTPUT
                                    else: color = COLOR_METAL1_INPUT
                                    break
                    metal2_lines.append(f"1 {color} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")
        ldr_lines.extend(contact_lines)

    # 7. Metal 1
    ldr_lines.append("0 STEP\n0 // Metal 1")
    if 'L8D0' in cif_data['layers']:
        for geom in cif_data['layers']['L8D0']:
            color = COLOR_METAL1_INTERNAL
            # Match net for color
            for net_name, geoms in net_map.items():
                if geom in geoms:
                    if net_name == 'VDD': color = COLOR_VDD
                    elif net_name == 'VSS': color = COLOR_VSS
                    elif net_name == 'X' or net_name == 'Y': color = COLOR_METAL1_OUTPUT
                    else: color = COLOR_METAL1_INPUT
                    break
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i*20, k*20, geom): metal1_grid[i][k] = color
    for plate, x_off, z_off, color, rotated in get_best_plates_multi(metal1_grid):
        ldr_lines.append(f"1 {color} {x_off} {Y_METAL1} {z_off} {'0 0 1 0 1 0 -1 0 0' if rotated else '1 0 0 0 1 0 0 0 1'} {plate}")

    # 8. Metal 2 Connections
    if metal2_lines:
        ldr_lines.append("0 STEP\n0 // Metal 2 Connections")
        ldr_lines.extend(metal2_lines)

    return "\n".join(ldr_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cif_to_ldr.py <cif_file>")
        sys.exit(1)
    cif_file = sys.argv[1]
    cell_name = os.path.basename(cif_file).replace(".cif", "")
    cif_data = parse_cif(cif_file)
    if not cif_data or not cif_data['boundary']:
        print(f"Error: Could not parse CIF or missing boundary in {cif_file}")
        sys.exit(1)
    ldr_content = generate_ldr(cif_data, cell_name)
    os.makedirs("models", exist_ok=True)
    output_file = f"models/{cell_name}.ldr"
    with open(output_file, 'w') as f: f.write(ldr_content)
    print(f"Generated {output_file}")
