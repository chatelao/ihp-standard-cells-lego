import math
import re
import sys
import os

# Constants from MAPPING_RULEBOOK.md
UM_TO_LDU = 20 / 0.27
LDU_PER_STUD = 20
LDR_Z_OFFSET = 10
CELL_HEIGHT_STUDS = 15

# LDraw Part dimensions for Metal 1 (plates and tiles)
PLATE_DIMENSIONS = {
    "91405.dat": (16, 16),
    "92438.dat": (16, 8),
    "3027.dat": (16, 6),
    "3456.dat": (14, 6),
    "3028.dat": (12, 6),
    "3033.dat": (10, 6),
    "3029.dat": (12, 4),
    "3036.dat": (8, 6),
    "3030.dat": (10, 4),
    "3958.dat": (6, 6),
    "4282.dat": (16, 2),
    "3035.dat": (8, 4),
    "2445.dat": (12, 2),
    "3032.dat": (6, 4),
    "3832.dat": (10, 2),
    "3034.dat": (8, 2),
    "3031.dat": (4, 4),
    "60479.dat": (12, 1),
    "3795.dat": (6, 2),
    "4477.dat": (10, 1),
    "3460.dat": (8, 1),
    "3020.dat": (4, 2),
    "3666.dat": (6, 1),
    "3021.dat": (3, 2),
    "3710.dat": (4, 1),
    "3022.dat": (2, 2),
    "3623.dat": (3, 1),
    "3023.dat": (2, 1),
    "3024.dat": (1, 1),
    "3070.dat": (1, 1), # Flat tile
}

def um_to_ldu_coord(um):
    return round(um * UM_TO_LDU)

def parse_lef_metal1(lef_filepath):
    with open(lef_filepath, 'r') as f:
        content = f.read()

    macros = {}
    # Improved regex to avoid property definitions
    macro_blocks = re.finditer(r'(?<!PROPERTYDEFINITIONS\n  )MACRO\s+([\w\[\]<>]+)(.*?)END\s+\1', content, re.DOTALL)
    for block in macro_blocks:
        macro_name = block.group(1)
        body = block.group(2)

        size_match = re.search(r'SIZE\s+([\d\.]+)\s+BY\s+([\d\.]+)\s*;', body)
        width_um = float(size_match.group(1)) if size_match else 0

        rects = []
        # Parse PINs
        pin_matches = re.finditer(r'PIN\s+([\w\[\]<>]+)(.*?)END\s+\1', body, re.DOTALL)
        for pin_match in pin_matches:
            pin_body = pin_match.group(2)
            # Find Metal1 layers in Ports
            port_matches = re.finditer(r'PORT\s+(.*?)END', pin_body, re.DOTALL)
            for port_match in port_matches:
                layer_matches = re.finditer(r'LAYER\s+Metal1\s*;(.*?)(?=LAYER|END|$)', port_match.group(1), re.DOTALL)
                for layer_match in layer_matches:
                    pin_rects = re.findall(r'RECT\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', layer_match.group(1))
                    rects.extend([[float(c) for c in r] for r in pin_rects])

        # Parse OBS
        obs_match = re.search(r'OBS\s+(.*?)END', body, re.DOTALL)
        if obs_match:
            layer_matches = re.finditer(r'LAYER\s+Metal1\s*;(.*?)(?=LAYER|END|$)', obs_match.group(1), re.DOTALL)
            for layer_match in layer_matches:
                obs_rects = re.findall(r'RECT\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', layer_match.group(1))
                rects.extend([[float(c) for c in r] for r in obs_rects])

        macros[macro_name] = {
            'width_um': width_um,
            'rects': rects
        }

    return macros

def get_lef_grid(macro):
    # Determine cell width in studs
    # Rulebook: sg13g2_nand2b_2 and sg13g2_xor2_1 are 300 LDU (15 studs)
    if macro['name'] in ['sg13g2_nand2b_2', 'sg13g2_xor2_1']:
        width_ldu = 300
    else:
        width_ldu = int(round(macro['width_um'] * UM_TO_LDU / 20) * 20)

    w_studs = width_ldu // 20
    d_studs = CELL_HEIGHT_STUDS
    grid = [[False for _ in range(d_studs)] for _ in range(w_studs)]

    for r in macro['rects']:
        lx1 = um_to_ldu_coord(r[0])
        lz1 = um_to_ldu_coord(r[1]) + LDR_Z_OFFSET
        lx2 = um_to_ldu_coord(r[2])
        lz2 = um_to_ldu_coord(r[3]) + LDR_Z_OFFSET

        xmin_raw, xmax_raw = min(lx1, lx2), max(lx1, lx2)
        zmin_raw, zmax_raw = min(lz1, lz2), max(lz1, lz2)

        # Inclusive snapping logic from lef_to_ldr.py
        xmin = math.floor(xmin_raw / 20) * 20
        xmax = math.ceil(xmax_raw / 20) * 20
        zmin = math.floor(zmin_raw / 20) * 20
        zmax = math.ceil(zmax_raw / 20) * 20

        if xmax <= xmin: xmax = xmin + 20
        if zmax <= zmin: zmax = zmin + 20

        for gx in range(xmin + 10, xmax, 20):
            for gz in range(zmin + 10, zmax, 20):
                gsx, gsz = gx // 20, gz // 20
                if 0 <= gsx < w_studs and 0 <= gsz < d_studs:
                    grid[gsx][gsz] = True
    return grid

def get_ldr_grid(ldr_filepath):
    with open(ldr_filepath, 'r') as f:
        lines = f.readlines()

    metal1_parts = []
    for line in lines:
        # Match LDraw part line: 1 <color> <x> <y> <z> ... <part>
        match = re.match(r'^1\s+\d+\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+\s+){9}([\w.-]+)', line, re.IGNORECASE)
        if match:
            x, y, z, part = float(match.group(1)), float(match.group(2)), float(match.group(3)), match.group(5).lower()
            # Metal 1 is at Y = -56. Metal 2 connection tiles (flat) at Y = -64.
            # We treat both as Metal 1 occupancy for the top view.
            if abs(y - (-56)) < 0.1 or abs(y - (-64)) < 0.1:
                metal1_parts.append({'x': x, 'z': z, 'part': part, 'line': line})

    if not metal1_parts:
        return None

    # Determine bounding box from LDR
    min_x, max_x = float('inf'), float('-inf')
    min_z, max_z = float('inf'), float('-inf')

    for p in metal1_parts:
        pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
        # Check rotation matrix
        tokens = p['line'].split()
        m0 = float(tokens[5])
        m2 = float(tokens[7])
        if abs(m0) < 0.1 and abs(m2) > 0.9: # Rotated
            pw, pd = pd, pw

        half_w = (pw * 20) / 2
        half_d = (pd * 20) / 2
        min_x = min(min_x, p['x'] - half_w)
        max_x = max(max_x, p['x'] + half_w)
        min_z = min(min_z, p['z'] - half_d)
        max_z = max(max_z, p['z'] + half_d)

    # Force alignment to 20 LDU grid
    grid_min_x = int(math.floor(min_x / 20 + 0.1) * 20)
    grid_max_x = int(math.ceil(max_x / 20 - 0.1) * 20)
    grid_min_z = int(math.floor(min_z / 20 + 0.1) * 20)
    grid_max_z = int(math.ceil(max_z / 20 - 0.1) * 20)

    # Standard cell height is 300 LDU (15 studs)
    # We ignore deviations in Z-range if they are within bounds
    w_studs = (grid_max_x - 0) // 20
    d_studs = CELL_HEIGHT_STUDS
    grid = [[False for _ in range(d_studs)] for _ in range(w_studs)]

    for p in metal1_parts:
        pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
        tokens = p['line'].split()
        m0 = float(tokens[5])
        m2 = float(tokens[7])
        if abs(m0) < 0.1 and abs(m2) > 0.9: # Rotated
            pw, pd = pd, pw

        ix1 = int(math.floor((p['x'] - (pw*20)/2) / 20 + 0.1))
        iz1 = int(math.floor((p['z'] - (pd*20)/2) / 20 + 0.1))
        ix2 = int(math.floor((p['x'] + (pw*20)/2) / 20 + 0.1))
        iz2 = int(math.floor((p['z'] + (pd*20)/2) / 20 + 0.1))

        for i in range(ix1, ix2):
            for j in range(iz1, iz2):
                if 0 <= i < w_studs and 0 <= j < d_studs:
                    grid[i][j] = True
    return grid

def print_grid(grid, label):
    if not grid: return
    w = len(grid)
    h = len(grid[0])
    print(f"--- {label} ---")
    scale = "  " + "".join([str(i % 10) for i in range(w)])
    print(scale)
    for j in range(h - 1, -1, -1):
        line = f"{j % 10} "
        for i in range(w):
            line += "X" if grid[i][j] else "."
        print(line)

def calculate_match(grid1, grid2):
    if not grid1 or not grid2: return 0.0
    w1, h1 = len(grid1), len(grid1[0])
    w2, h2 = len(grid2), len(grid2[0])

    w = max(w1, w2)
    h = max(h1, h2)

    matches = 0
    total = w * h

    for i in range(w):
        for j in range(h):
            val1 = grid1[i][j] if i < w1 and j < h1 else False
            val2 = grid2[i][j] if i < w2 and j < h2 else False
            if val1 == val2:
                matches += 1
    return matches / total

def main():
    lef_file = 'specifications/sg13g2_stdcell.lef'
    models_dir = 'models'

    lef_macros = parse_lef_metal1(lef_file)

    all_results = []

    for filename in sorted(os.listdir(models_dir)):
        if filename.endswith('.ldr'):
            macro_name = filename[:-4]
            if macro_name not in lef_macros:
                continue

            macro_info = lef_macros[macro_name]
            macro_info['name'] = macro_name

            lef_grid = get_lef_grid(macro_info)
            ldr_grid = get_ldr_grid(os.path.join(models_dir, filename))

            if ldr_grid is None:
                print(f"WARN: No Metal 1 found in {filename}")
                continue

            ratio = calculate_match(lef_grid, ldr_grid)
            all_results.append((macro_name, ratio))

            if len(sys.argv) > 1 and sys.argv[1] == macro_name:
                print_grid(lef_grid, f"LEF View: {macro_name}")
                print_grid(ldr_grid, f"LEGO View: {macro_name}")

            print(f"{macro_name}: {ratio:.2%}")

    if all_results:
        avg = sum(r[1] for r in all_results) / len(all_results)
        print(f"\nAverage Match Ratio across {len(all_results)} cells: {avg:.2%}")

if __name__ == "__main__":
    main()
