import math
import re
import sys
import os

# Constants from MAPPING_RULEBOOK.md
UM_TO_LDU = 20 / 0.27
LDU_PER_STUD = 20
LDR_Z_OFFSET = 10
CELL_HEIGHT_STUDS = 15

PLATE_DIMENSIONS = {
    "91405.dat": (16, 16), "92438.dat": (16, 8), "3027.dat": (16, 6),
    "3456.dat": (14, 6), "3028.dat": (12, 6), "3033.dat": (10, 6),
    "3029.dat": (12, 4), "3036.dat": (8, 6), "3030.dat": (10, 4),
    "3958.dat": (6, 6), "4282.dat": (16, 2), "3035.dat": (8, 4),
    "2445.dat": (12, 2), "3032.dat": (6, 4), "3832.dat": (10, 2),
    "3034.dat": (8, 2), "3031.dat": (4, 4), "60479.dat": (12, 1),
    "3795.dat": (6, 2), "4477.dat": (10, 1), "3460.dat": (8, 1),
    "3020.dat": (4, 2), "3666.dat": (6, 1), "3021.dat": (3, 2),
    "3710.dat": (4, 1), "3022.dat": (2, 2), "3623.dat": (3, 1),
    "3023.dat": (2, 1), "3024.dat": (1, 1), "3070.dat": (1, 1),
}

def um_to_ldu_coord(um): return round(um * UM_TO_LDU)

def parse_lef_metal1(lef_filepath, target_macro):
    with open(lef_filepath, 'r') as f: content = f.read()
    match = re.search(r'(?<!PROPERTYDEFINITIONS\n  )MACRO\s+'+target_macro+r'(.*?)END\s+'+target_macro, content, re.DOTALL)
    if not match: return None
    body = match.group(1)
    size_match = re.search(r'SIZE\s+([\d\.]+)\s+BY\s+([\d\.]+)\s*;', body)
    width_um = float(size_match.group(1)) if size_match else 0
    rects = []
    pin_matches = re.finditer(r'PIN\s+([\w\[\]<>]+)(.*?)END\s+\1', body, re.DOTALL)
    for pin_match in pin_matches:
        pin_body = pin_match.group(2)
        port_matches = re.finditer(r'PORT\s+(.*?)END', pin_body, re.DOTALL)
        for port_match in port_matches:
            layer_matches = re.finditer(r'LAYER\s+Metal1\s*;(.*?)(?=LAYER|END|$)', port_match.group(1), re.DOTALL)
            for layer_match in layer_matches:
                pin_rects = re.findall(r'RECT\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', layer_match.group(1))
                rects.extend([[float(c) for c in r] for r in pin_rects])
    obs_match = re.search(r'OBS\s+(.*?)END', body, re.DOTALL)
    if obs_match:
        layer_matches = re.finditer(r'LAYER\s+Metal1\s*;(.*?)(?=LAYER|END|$)', obs_match.group(1), re.DOTALL)
        for layer_match in layer_matches:
            obs_rects = re.findall(r'RECT\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', layer_match.group(1))
            rects.extend([[float(c) for c in r] for r in obs_rects])
    return {'name': target_macro, 'width_um': width_um, 'rects': rects}

def get_lef_grid(macro):
    width_ldu = 300 if macro['name'] in ['sg13g2_nand2b_2', 'sg13g2_xor2_1'] else int(round(macro['width_um'] * UM_TO_LDU / 20) * 20)
    w_studs, d_studs = width_ldu // 20, CELL_HEIGHT_STUDS
    grid = [[False for _ in range(d_studs)] for _ in range(w_studs)]
    for r in macro['rects']:
        lx1, lz1, lx2, lz2 = um_to_ldu_coord(r[0]), um_to_ldu_coord(r[1]) + LDR_Z_OFFSET, um_to_ldu_coord(r[2]), um_to_ldu_coord(r[3]) + LDR_Z_OFFSET
        xmin, xmax = math.floor(min(lx1, lx2)/20)*20, math.ceil(max(lx1, lx2)/20)*20
        zmin, zmax = math.floor(min(lz1, lz2)/20)*20, math.ceil(max(lz1, lz2)/20)*20
        if xmax <= xmin: xmax = xmin + 20
        if zmax <= zmin: zmax = zmin + 20
        for gx in range(xmin+10, xmax, 20):
            for gz in range(zmin+10, zmax, 20):
                gsx, gsz = gx//20, gz//20
                if 0 <= gsx < w_studs and 0 <= gsz < d_studs: grid[gsx][gsz] = True
    return grid

def get_ldr_grid(ldr_filepath):
    with open(ldr_filepath, 'r') as f: lines = f.readlines()
    metal1_parts = []
    for line in lines:
        match = re.match(r'^1\s+\d+\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+\s+){9}([\w.-]+)', line, re.IGNORECASE)
        if match:
            x, y, z, part = float(match.group(1)), float(match.group(2)), float(match.group(3)), match.group(5).lower()
            if abs(y - (-56)) < 0.1 or abs(y - (-64)) < 0.1: metal1_parts.append({'x': x, 'z': z, 'part': part, 'line': line})
    if not metal1_parts: return None
    min_x, max_x, min_z, max_z = float('inf'), float('-inf'), float('inf'), float('-inf')
    for p in metal1_parts:
        pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
        tokens = p['line'].split()
        if abs(float(tokens[5])) < 0.1 and abs(float(tokens[7])) > 0.9: pw, pd = pd, pw
        min_x, max_x = min(min_x, p['x'] - (pw*20)/2), max(max_x, p['x'] + (pw*20)/2)
        min_z, max_z = min(min_z, p['z'] - (pd*20)/2), max(max_z, p['z'] + (pd*20)/2)
    w_studs = int(math.ceil(max_x / 20 - 0.1))
    grid = [[False for _ in range(CELL_HEIGHT_STUDS)] for _ in range(w_studs)]
    for p in metal1_parts:
        pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
        tokens = p['line'].split()
        if abs(float(tokens[5])) < 0.1 and abs(float(tokens[7])) > 0.9: pw, pd = pd, pw
        ix1, iz1, ix2, iz2 = int(math.floor((p['x']-(pw*20)/2)/20+0.1)), int(math.floor((p['z']-(pd*20)/2)/20+0.1)), int(math.floor((p['x']+(pw*20)/2)/20+0.1)), int(math.floor((p['z']+(pd*20)/2)/20+0.1))
        for i in range(ix1, ix2):
            for j in range(iz1, iz2):
                if 0 <= i < w_studs and 0 <= j < CELL_HEIGHT_STUDS: grid[i][j] = True
    return grid

def print_side_by_side(grid1, grid2, name):
    w1, w2 = len(grid1), len(grid2)
    h = CELL_HEIGHT_STUDS
    print(f"Comparison for {name}:")
    header = "   LEF View" + " " * (w1 - 4) + "    " + "LEGO View"
    print(header)
    scale = "   " + "".join([str(i % 10) for i in range(w1)]) + "    " + "".join([str(i % 10) for i in range(w2)])
    print(scale)
    for j in range(h - 1, -1, -1):
        line = f"{j % 10} "
        line1 = "".join(["X" if grid1[i][j] else "." for i in range(w1)])
        line2 = "".join(["X" if grid2[i][j] else "." for i in range(w2)])
        print(f"{line} {line1}    {line2}")

def main():
    if len(sys.argv) < 2: return
    name = sys.argv[1]
    macro = parse_lef_metal1('specifications/sg13g2_stdcell.lef', name)
    if not macro: return
    grid1 = get_lef_grid(macro)
    grid2 = get_ldr_grid(f'models/{name}.ldr')
    if grid1 and grid2: print_side_by_side(grid1, grid2, name)

if __name__ == "__main__": main()
