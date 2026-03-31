import math
import re
import sys
import os

CIF_TO_LDU = 20 / 270
LDR_Z_OFFSET = 10
SNAPPING_TOLERANCE = 9.0
CELL_HEIGHT_STUDS = 15

PLATE_DIMENSIONS = {
    "91405.dat": (16, 16), "92438.dat": (16, 8), "3027.dat": (16, 6), "3456.dat": (14, 6),
    "3028.dat": (12, 6), "3033.dat": (10, 6), "3029.dat": (12, 4), "3036.dat": (8, 6),
    "3030.dat": (10, 4), "3958.dat": (6, 6), "4282.dat": (16, 2), "3035.dat": (8, 4),
    "2445.dat": (12, 2), "3032.dat": (6, 4), "3832.dat": (10, 2), "3034.dat": (8, 2),
    "3031.dat": (4, 4), "60479.dat": (12, 1), "3795.dat": (6, 2), "4477.dat": (10, 1),
    "3460.dat": (8, 1), "3020.dat": (4, 2), "3666.dat": (6, 1), "3021.dat": (3, 2),
    "3710.dat": (4, 1), "3022.dat": (2, 2), "3623.dat": (3, 1), "3023.dat": (2, 1),
    "3024.dat": (1, 1), "3070.dat": (1, 1)
}

def to_ldr_x(val): return val * CIF_TO_LDU
def to_ldr_z(val): return val * CIF_TO_LDU + LDR_Z_OFFSET

def parse_cif_poly(cif_path):
    if not os.path.exists(cif_path): return None
    with open(cif_path, 'r') as f: cif_content = f.read()
    poly_geoms = []; current_layer = None
    commands = cif_content.split(';')
    for cmd in commands:
        cmd = cmd.strip()
        if not cmd: continue
        if cmd.startswith('L '): current_layer = cmd[2:].strip()
        elif cmd.startswith('B ') and current_layer == 'L5D0':
            parts = re.split(r'\s+|,', cmd[2:].strip())
            if len(parts) >= 4:
                w_nm, h_nm, xc_nm, yc_nm = map(float, parts[:4])
                x1, z1 = to_ldr_x(xc_nm - w_nm/2), to_ldr_z(yc_nm - h_nm/2)
                x2, z2 = to_ldr_x(xc_nm + w_nm/2), to_ldr_z(yc_nm + h_nm/2)
                poly_geoms.append({'type': 'box', 'coords': [min(x1,x2), min(z1,z2), max(x1,x2), max(z1,z2)]})
        elif cmd.startswith('P ') and current_layer == 'L5D0':
            points_str = cmd[2:].strip().split()
            points = []
            for p in points_str:
                pt = p.split(',')
                if len(pt) == 2: points.append((to_ldr_x(float(pt[0])), to_ldr_z(float(pt[1]))))
            if points: poly_geoms.append({'type': 'polygon', 'points': points})
    return poly_geoms

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
    n = len(poly); inside = False; p1x, p1z = poly[0]
    for i in range(n + 1):
        p2x, p2z = poly[i % n]
        if z > min(p1z, p2z) and z <= max(p1z, p2z) and x <= max(p1x, p2x):
            if p1z != p2z:
                xints = (z - p1z) * (p2x - p1x) / (p2z - p1z) + p1x
                if p1x == p2x or x <= xints: inside = not inside
        p1x, p1z = p2x, p2z
    return inside

def is_stud_occupied_geom(gx, gz, geom):
    if geom['type'] == 'box': return is_stud_occupied(gx, gz, *geom['coords'])
    if geom['type'] == 'polygon':
        poly = geom['points']
        if is_point_in_poly(gx + 10, gz + 10, poly): return True
        xs, zs = [p[0] for p in poly], [p[1] for p in poly]
        xmin, xmax, zmin, zmax = min(xs), max(xs), min(zs), max(zs)
        if xmax - xmin > 21.0 and zmax - zmin > 21.0:
            return (min(xmax, gx + 20) - max(xmin, gx)) >= SNAPPING_TOLERANCE and (min(zmax, gz + 20) - max(zmin, gz)) >= SNAPPING_TOLERANCE
    return False

def get_ldr_data(ldr_path):
    with open(ldr_path, 'r') as f: lines = f.readlines()
    poly_parts = []; substrate_parts = []
    for line in lines:
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+\s+){9}([\w.-]+)', line, re.IGNORECASE)
        if match:
            color, x, y, z, part = int(match.group(1)), float(match.group(2)), float(match.group(3)), float(match.group(4)), match.group(6).lower()
            if color == 4 and abs(y - (-24)) < 0.1: poly_parts.append({'x': x, 'z': z, 'part': part, 'line': line})
            if color == 8 and abs(y - 0) < 0.1: substrate_parts.append({'x': x, 'z': z, 'part': part, 'line': line})
    return poly_parts, substrate_parts

def get_grid_from_parts(parts, w_studs):
    grid = [[False for _ in range(CELL_HEIGHT_STUDS)] for _ in range(w_studs)]
    for p in parts:
        pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
        tokens = p['line'].split()
        m0, m2 = float(tokens[5]), float(tokens[7])
        if abs(m0) < 0.1 and abs(m2) > 0.9: pw, pd = pd, pw
        ix1, iz1 = int(round((p['x'] - pw*10)/20)), int(round((p['z'] - pd*10)/20))
        for i in range(ix1, ix1 + pw):
            for j in range(iz1, iz1 + pd):
                if 0 <= i < w_studs and 0 <= j < CELL_HEIGHT_STUDS: grid[i][j] = True
    return grid

def main():
    cell_name = sys.argv[1] if len(sys.argv) > 1 else None
    if cell_name:
        cells = [cell_name]
    else:
        cells = sorted([f[:-4] for f in os.listdir('models') if f.endswith('.ldr')])

    total_ratios = []
    for cell in cells:
        ldr_path = f'models/{cell}.ldr'
        cif_path = f'specifications/cells/{cell}.cif'
        if not os.path.exists(ldr_path) or not os.path.exists(cif_path): continue

        poly_parts, substrate_parts = get_ldr_data(ldr_path)
        if not substrate_parts: continue

        max_x = max(p['x'] + (PLATE_DIMENSIONS.get(p['part'],(1,1))[0]*10 if abs(float(p['line'].split()[5])) > 0.9 else PLATE_DIMENSIONS.get(p['part'],(1,1))[1]*10) for p in substrate_parts)
        w_studs = int(round(max_x / 20))

        cif_geoms = parse_cif_poly(cif_path)
        cif_grid = [[False for _ in range(CELL_HEIGHT_STUDS)] for _ in range(w_studs)]
        for geom in cif_geoms:
            for i in range(w_studs):
                for k in range(CELL_HEIGHT_STUDS):
                    if is_stud_occupied_geom(i*20, k*20, geom):
                        if 1 <= k <= 13: cif_grid[i][k] = True

        ldr_grid = get_grid_from_parts(poly_parts, w_studs)

        matches = sum(cif_grid[i][j] == ldr_grid[i][j] for i in range(w_studs) for j in range(CELL_HEIGHT_STUDS))
        ratio = matches / (w_studs * CELL_HEIGHT_STUDS)
        total_ratios.append(ratio)

        if len(cells) == 1:
            print(f"{cell} Poly Match: {ratio:.2%}")
            print("X: " + "".join([str(i % 10) for i in range(w_studs)]))
            for j in range(CELL_HEIGHT_STUDS - 1, -1, -1):
                line = f"Z{j % 10} "
                for i in range(w_studs):
                    c = "P" if cif_grid[i][j] else "."
                    l = "P" if ldr_grid[i][j] else "."
                    if c == l: line += c
                    elif c == "P": line += "C"
                    else: line += "L"
                print(line)

    if total_ratios:
        print(f"\nAverage Poly Match Ratio across {len(total_ratios)} cells: {sum(total_ratios)/len(total_ratios):.2%}")

if __name__ == "__main__":
    main()
