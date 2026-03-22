import math
import os
import re
import sys
import argparse

# Constants from modeling_guidelines.md (V3)
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

TILE_1X1 = "3070.dat"     # 1x1 flat tile
ROUND_BRICK = "3062b.dat" # 1x1 round brick
ROUND_PLATE = "6141.dat"  # 1x1 round plate

COLOR_MAP_REV = {
    'S': 8,   # Substrate Dark Gray
    'N': 7,   # N-Well Light Gray
    'n': 288, # NMOS Dark Green
    'p': 38,  # PMOS Dark Orange
    'G': 4,   # Polysilicon Red
    'I': 9,   # Metal 1 Input Light Blue
    'C': 1,   # Metal 1 Connection Blue
    'O': 272, # Metal 1 Output Dark Blue
    '+': 14,  # VDD Yellow
    '-': 0,   # VSS Black
}

# Contact mappings
CONTACT_MAP = {
    'i': 'I',
    'o': 'O',
    'c': 'C',
    '&': '+',
    '_': '-',
}

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

def parse_lef_macro(lef_content, macro_name):
    pattern = rf"(?<!PROPERTYDEFINITIONS\n  )MACRO\s+{macro_name}(.*?)END\s+{macro_name}"
    match = re.search(pattern, lef_content, re.DOTALL)
    if not match: return None
    body = match.group(1)

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
    return {'pins': pins}

def parse_design_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    layers = {}
    pattern = r'## (.*?)\n(?:GOLDEN STANDARD\n\n)?```\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)

    for layer_name, grid_text in matches:
        lines = grid_text.strip('\n').split('\n')
        if not lines: continue
        scale_line = lines[0]
        width = len(scale_line[2:])
        grid_lines = lines[1:]
        parsed_grid = []
        for line in grid_lines:
            chars = line[2:].ljust(width)
            parsed_grid.append(list(chars))
        if not parsed_grid: continue
        parsed_grid.reverse()
        h = len(parsed_grid)
        w = width
        final_grid = [[None for _ in range(h)] for _ in range(w)]
        for z in range(h):
            for x in range(w):
                char = parsed_grid[z][x]
                if char != ' ':
                    final_grid[x][z] = char
        layers[layer_name] = final_grid
    return layers

def generate_ldr_from_layers(cell_name, layers, macro_data):
    ldr_lines = [
        f"0 {cell_name}.ldr",
        f"0 Name: {cell_name}.ldr",
        "0 Author: design_to_ldr.py",
        "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt",
        "0 !LPUB PLI GLOBAL ON",
        ""
    ]

    if 'Substrate' in layers:
        grid = layers['Substrate']
        w, h = len(grid), len(grid[0])
        ldr_lines.append("0 // Substrate low (V3)")
        low_grid = [[COLOR_MAP_REV.get('S') for _ in range(h)] for _ in range(w)]
        # Interlocking: use prefer_rotated=True for the bottom layer
        for plate, x, z, color, rot in get_best_plates_multi(low_grid, prefer_rotated=True):
            ldr_lines.append(f"1 {color} {x} {Y_SUBSTRATE_LOW} {z} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Substrate high / N-Well")
        high_grid = [[COLOR_MAP_REV.get(grid[x][z]) for z in range(h)] for x in range(w)]
        for plate, x, z, color, rot in get_best_plates_multi(high_grid):
            ldr_lines.append(f"1 {color} {x} {Y_SUBSTRATE_HIGH} {z} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")

    if 'Active' in layers:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Active Regions")
        grid = layers['Active']
        w, h = len(grid), len(grid[0])
        active_grid = [[COLOR_MAP_REV.get(grid[x][z]) for z in range(h)] for x in range(w)]
        for plate, x, z, color, rot in get_best_plates_multi(active_grid):
            ldr_lines.append(f"1 {color} {x} {Y_ACTIVE} {z} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")

    if 'Polysilicon' in layers:
        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Polysilicon Gates")
        grid = layers['Polysilicon']
        w, h = len(grid), len(grid[0])
        poly_grid = [[COLOR_MAP_REV.get(grid[x][z]) for z in range(h)] for x in range(w)]
        for plate, x, z, color, rot in get_best_plates_multi(poly_grid):
            ldr_lines.append(f"1 {color} {x} {Y_POLY} {z} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")

    if 'Metal 1' in layers:
        grid = layers['Metal 1']
        w, h = len(grid), len(grid[0])
        contacts = []
        metal2_plates = []
        for x in range(w):
            for z in range(h):
                char = grid[x][z]
                if char in CONTACT_MAP or char == 'c':
                    sx, sz = x * 20 + 10, z * 20 + 10
                    # 1. Metal 1 to Metal 2 connection (Y=-64)
                    real_char = CONTACT_MAP.get(char, char)
                    color = COLOR_MAP_REV.get(real_char)
                    if color is not None:
                        metal2_plates.append(f"1 {color} {sx} {Y_METAL2_PLATE} {sz} 1 0 0 0 1 0 0 0 1 {TILE_1X1}")

                    # 2. Contact Stack (Y=-48 Brick)
                    contacts.append(f"1 15 {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")

                    # 3. Connectivity to underlying layers (Active or Poly)
                    is_to_poly = False
                    if 'Polysilicon' in layers:
                        poly_grid = layers['Polysilicon']
                        if x < len(poly_grid) and z < len(poly_grid[x]):
                            if poly_grid[x][z] == 'G': is_to_poly = True
                    if z == 6: is_to_poly = True # Track 6 is Polysilicon track

                    if not is_to_poly:
                         # Active connection: Need 1x1 plate at Y=-24 to bridge brick to Active.
                         contacts.append(f"1 15 {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")

        if contacts:
            ldr_lines.append("0 STEP")
            ldr_lines.append("0 // Contacts")
            ldr_lines.extend(contacts)

        ldr_lines.append("0 STEP")
        ldr_lines.append("0 // Metal 1")

        # Tile by pin
        assigned = [[False for _ in range(h)] for _ in range(w)]
        if macro_data:
            for pin in macro_data['pins']:
                pin_grid = [[None for _ in range(h)] for _ in range(w)]
                has_pin_parts = False
                color = None
                for rect in pin['rects']:
                    if rect['layer'] == 'Metal1':
                        x1 = int(math.floor(rect['coords'][0] * 20 / 0.27 / 20))
                        z1 = int(math.floor((rect['coords'][1] * 20 / 0.27 + 10) / 20))
                        x2 = int(math.ceil(rect['coords'][2] * 20 / 0.27 / 20))
                        z2 = int(math.ceil((rect['coords'][3] * 20 / 0.27 + 10) / 20))
                        for ix in range(min(x1, x2), max(x1, x2)):
                            for iz in range(min(z1, z2), max(z1, z2)):
                                if 0 <= ix < w and 0 <= iz < h and not assigned[ix][iz]:
                                    char = grid[ix][iz]
                                    if char:
                                        real_char = CONTACT_MAP.get(char, char)
                                        color = COLOR_MAP_REV.get(real_char)
                                        pin_grid[ix][iz] = color
                                        assigned[ix][iz] = True
                                        has_pin_parts = True
                if has_pin_parts:
                    pin_label = f"0 // {'VDD' if pin['name']=='VDD' else 'VSS' if pin['name']=='VSS' else 'Pin '+pin['name']} Rail" if pin['name'] in ['VDD', 'VSS'] else f"0 // Pin {pin['name']}"
                    ldr_lines.append(pin_label)
                    for plate, x, z, c, rot in get_best_plates_multi(pin_grid):
                        ldr_lines.append(f"1 {c} {x} {Y_METAL1} {z} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")

        # Unassigned Metal 1 (Internal/Obstructions)
        rem_grid = [[None for _ in range(h)] for _ in range(w)]
        has_rem = False
        for x in range(w):
            for z in range(h):
                if not assigned[x][z] and grid[x][z]:
                    char = grid[x][z]
                    real_char = CONTACT_MAP.get(char, char)
                    rem_grid[x][z] = COLOR_MAP_REV.get(real_char)
                    has_rem = True
        if has_rem:
            ldr_lines.append("0 // Internal / Obstructions")
            for plate, x, z, c, rot in get_best_plates_multi(rem_grid):
                ldr_lines.append(f"1 {c} {x} {Y_METAL1} {z} {'0 0 1 0 1 0 -1 0 0' if rot else '1 0 0 0 1 0 0 0 1'} {plate}")

        if metal2_plates:
            ldr_lines.append("0 STEP")
            ldr_lines.append("0 // Metal 2 Connections")
            ldr_lines.extend(metal2_plates)

    return "\n".join(ldr_lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cell', help='Process only a specific cell')
    args = parser.parse_args()

    lef_path = 'specifications/sg13g2_stdcell.lef'
    with open(lef_path, 'r') as f: lef_content = f.read()
    design_dir, models_dir = 'design', 'models'
    if not os.path.exists(models_dir): os.makedirs(models_dir)

    files = os.listdir(design_dir)
    if args.cell:
        files = [f"{args.cell}.md"]

    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(design_dir, filename)
            if not os.path.exists(filepath):
                print(f"Error: {filepath} not found")
                continue
            cell_name = filename[:-3]
            print(f"Processing {cell_name}...")
            macro_data = parse_lef_macro(lef_content, cell_name)
            layers = parse_design_md(filepath)
            ldr_content = generate_ldr_from_layers(cell_name, layers, macro_data)
            with open(os.path.join(models_dir, f"{cell_name}.ldr"), 'w', encoding='utf-8') as f:
                f.write(ldr_content)

if __name__ == "__main__":
    main()
