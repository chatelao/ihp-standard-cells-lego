import os
import re

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
    "3070.dat": (1, 1),
    "6141.dat": (1, 1),
    "3062b.dat": (1, 1),
}

def get_dimensions(parts):
    if not parts:
        return 0, 0, 0, 0

    min_x, max_x = float('inf'), float('-inf')
    min_z, max_z = float('inf'), float('-inf')

    for p in parts:
        pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
        is_rotated = p['rot'][0] == 0
        if is_rotated:
            pw, pd = pd, pw

        half_w_ldu = (pw * 20) / 2
        half_d_ldu = (pd * 20) / 2

        min_x = min(min_x, p['x'] - half_w_ldu)
        max_x = max(max_x, p['x'] + half_w_ldu)
        min_z = min(min_z, p['z'] - half_d_ldu)
        max_z = max(max_z, p['z'] + half_d_ldu)

    grid_min_x = int(round(min_x / 20)) * 20
    grid_max_x = int(round(max_x / 20)) * 20
    grid_min_z = int(round(min_z / 20)) * 20
    grid_max_z = int(round(max_z / 20)) * 20

    if grid_max_x <= grid_min_x:
        grid_max_x = grid_min_x + 20

    width_studs = (grid_max_x - grid_min_x) // 20
    height_studs = (grid_max_z - grid_min_z) // 20

    return width_studs, height_studs, grid_min_x, grid_min_z

def parse_ldr_full(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    parts = []
    current_label = None
    for line in lines:
        line = line.strip()
        if not line: continue
        if line.startswith('0 //'):
            label = line[4:].strip()
            if label not in ["Substrate low (V3)", "Substrate high / N-Well", "Active Regions", "Polysilicon Gates", "Contacts", "Metal 1", "Metal 2 Connections", "Obstructions"]:
                current_label = label
        elif line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                color = int(tokens[1])
                x = float(tokens[2])
                y = float(tokens[3])
                z = float(tokens[4])
                rot = [float(t) for t in tokens[5:14]]
                part = tokens[14]
                parts.append({'color': color, 'x': x, 'y': y, 'z': z, 'rot': rot, 'part': part, 'label': current_label})
    return parts

def get_char_for_stud(parts, x, z, layer_y_list, color_map, connection_map):
    char = ' '
    priority = {'+': 5, '-': 5, 'I': 4, 'O': 3, 'C': 2, 'S': 1, 'N': 1, 'n': 1, 'p': 1, 'G': 1}

    for p in sorted(parts, key=lambda p: priority.get(color_map.get(p['color'], ' '), 0), reverse=False):
        if p['y'] in layer_y_list and p['part'] != '3062b.dat':
            pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
            is_rotated = p['rot'][0] == 0
            if is_rotated: pw, pd = pd, pw
            half_w = (pw * 20) / 2
            half_d = (pd * 20) / 2
            if (p['x'] - half_w <= x <= p['x'] + half_w) and (p['z'] - half_d <= z <= p['z'] + half_d):
                char = color_map.get(p['color'], char)

    if layer_y_list[0] == -56:
        has_contact_below = False
        for p in parts:
            if p['part'] == '3062b.dat' and p['y'] == -48:
                if abs(p['x'] - x) < 5 and abs(p['z'] - z) < 5:
                    has_contact_below = True
                    break
        has_plate_above = False
        for p in parts:
            if (p['part'] == '3024.dat' or p['part'] == '3070.dat') and p['y'] == -64:
                if abs(p['x'] - x) < 5 and abs(p['z'] - z) < 5:
                    has_plate_above = True
                    break
        if has_contact_below or has_plate_above:
            alternatives = {'I': 'i', 'O': 'o', 'C': 'c', '+': '&', '-': '_'}
            return alternatives.get(char, 'c')
    return char

COLOR_MAP = {
    8: 'S', 7: 'N', 288: 'n', 38: 'p', 4: 'G', 9: 'I', 1: 'C', 272: 'O', 14: '+', 0: '-',
}

def extract_golden_sections(design_dir):
    golden_sections = {}
    gs_path = 'specifications/GOLDEN_STANDARD.md'
    if os.path.exists(gs_path):
        with open(gs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        header = "## 7. Golden Design Examples"
        if header in content:
            examples_part = content.split(header)[1]
            pattern = r'### (sg13g2_[a-z0-9_]+) - ([A-Za-z0-9 ]+)\n(.*?)(?=\n### |\n## |$)'
            matches = re.findall(pattern, examples_part, re.DOTALL)
            for cell_name, layer_name, text in matches:
                full_text = f"## {layer_name}\n{text.strip()}"
                golden_sections[(cell_name, layer_name)] = full_text
    if not os.path.exists(design_dir): return golden_sections
    for filename in os.listdir(design_dir):
        if filename.endswith('.md'):
            cell_name = filename[:-3]
            filepath = os.path.join(design_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            sections = content.split('\n## ')
            for section in sections[1:]:
                if 'GOLDEN STANDARD' in section:
                    lines = section.split('\n')
                    layer_name = lines[0].strip()
                    golden_sections[(cell_name, layer_name)] = '## ' + section.strip()
    return golden_sections

def update_golden_standard_file(all_golden):
    filepath = 'specifications/GOLDEN_STANDARD.md'
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    header = "## 7. Golden Design Examples"
    if all_golden:
        new_text = header + "\n"
        for (cell, layer), text in sorted(all_golden.items()):
            new_text += f"### {cell} - {layer}\n"
            content_lines = text.split('\n')
            new_text += '\n'.join(content_lines[1:]).strip() + "\n\n"
        new_text = new_text.strip() + "\n"
    else: new_text = ""
    if header in content:
        before = content.split(header)[0]
        after_match = re.search(r'\n## [8-9]\.', content.split(header)[1])
        if after_match:
            after = content.split(header)[1][after_match.start():]
            content = before + new_text + after
        else: content = before + new_text
    elif new_text: content = content.strip() + "\n\n" + new_text
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def is_inside(p, sx, sz):
    pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
    is_rotated = p['rot'][0] == 0
    if is_rotated: pw, pd = pd, pw
    half_w = (pw * 20) / 2
    half_d = (pd * 20) / 2
    return (p['x'] - half_w - 0.1 <= sx <= p['x'] + half_w + 0.1) and (p['z'] - half_d - 0.1 <= sz <= p['z'] + half_d + 0.1)

def get_blobs(parts, width_studs, height_studs, min_x, min_z, y_layers, colors):
    grid = [[None for _ in range(height_studs)] for _ in range(width_studs)]
    for p in parts:
        if p['y'] in y_layers and p['color'] in colors and p['part'] != '3062b.dat':
            pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
            is_rotated = p['rot'][0] == 0
            if is_rotated: pw, pd = pd, pw
            half_w, half_d = pw * 10, pd * 10
            for i in range(width_studs):
                for j in range(height_studs):
                    sx, sz = min_x + i*20 + 10, min_z + j*20 + 10
                    if (p['x'] - half_w - 0.1 <= sx <= p['x'] + half_w + 0.1) and (p['z'] - half_d - 0.1 <= sz <= p['z'] + half_d + 0.1):
                        grid[i][j] = (p['label'] if p['label'] else "NoLabel", p['color'])
    visited = [[False for _ in range(height_studs)] for _ in range(width_studs)]
    blobs = []
    for i in range(width_studs):
        for j in range(height_studs):
            if grid[i][j] and not visited[i][j]:
                blob_studs, stack = [], [(i, j)]
                label, color = grid[i][j]
                visited[i][j] = True
                while stack:
                    curr_i, curr_j = stack.pop()
                    blob_studs.append((curr_i, curr_j))
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = curr_i + di, curr_j + dj
                        if 0 <= ni < width_studs and 0 <= nj < height_studs and grid[ni][nj] and not visited[ni][nj]:
                            if grid[ni][nj][1] == color:
                                visited[ni][nj] = True
                                stack.append((ni, nj))
                blobs.append({'label': label, 'color': color, 'studs': blob_studs})
    return blobs

def generate_connectivity_matrix(parts, width_studs, height_studs, min_x, min_z):
    nmos_blobs = get_blobs(parts, width_studs, height_studs, min_x, min_z, [-16], [288])
    pmos_blobs = get_blobs(parts, width_studs, height_studs, min_x, min_z, [-16], [38])
    poly_blobs = get_blobs(parts, width_studs, height_studs, min_x, min_z, [-24], [4])
    metal_blobs = get_blobs(parts, width_studs, height_studs, min_x, min_z, [-56, -64], [14, 0, 9, 272, 1])

    named_silicon = []
    for i, b in enumerate(nmos_blobs): b['name'] = f"NMOS{i+1}" if len(nmos_blobs) > 1 else "NMOS"; named_silicon.append(b)
    for i, b in enumerate(pmos_blobs): b['name'] = f"PMOS{i+1}" if len(pmos_blobs) > 1 else "PMOS"; named_silicon.append(b)
    for i, b in enumerate(poly_blobs): b['name'] = f"Poly{i+1}" if len(poly_blobs) > 1 else "Polysilicon"; named_silicon.append(b)

    for b in metal_blobs:
        labels_found = set()
        for i, j in b['studs']:
            sx, sz = min_x + i*20 + 10, min_z + j*20 + 10
            for p in parts:
                if p['y'] in [-56, -64] and p['color'] == b['color'] and is_inside(p, sx, sz):
                    if p['label'] and "Internal" not in p['label'] and "Obstructions" not in p['label']:
                        labels_found.add(p['label'])
        if labels_found:
            pref_labels = [l for l in labels_found if "Rail" not in l]
            b['label'] = sorted(list(pref_labels if pref_labels else labels_found), key=len)[0]

    named_metal, label_counts = [], {}
    for b in metal_blobs:
        label = b['label']
        if label and label != "NoLabel" and "Internal" not in label and "Obstructions" not in label:
            match = re.search(r'Pin\s+(\w+)', label)
            label = match.group(1) if match else ("VDD" if "VDD" in label else "VSS" if "VSS" in label else label)
        else: label = "Int"
        b['raw_label'] = label
        label_counts[label] = label_counts.get(label, 0) + 1

    curr_counts = {}
    for b in metal_blobs:
        label = b['raw_label']
        if label_counts[label] > 1:
            curr_counts[label] = curr_counts.get(label, 0) + 1
            b['name'] = f"{label}{curr_counts[label]}"
        else:
            b['name'] = label
        named_metal.append(b)

    def sort_metal(b):
        name = b['name']
        if name.startswith('VDD'): return (4, name)
        if name.startswith('VSS'): return (5, name)
        if name in ['X', 'Y', 'Z'] or name.startswith('X') or name.startswith('Y') or name.startswith('Z'): return (3, name)
        if name.startswith('Int'): return (2, name)
        return (1, name)

    named_silicon.sort(key=lambda x: x['name'])
    named_metal.sort(key=sort_metal)

    connections = set()
    contacts = [p for p in parts if p['part'] == '3062b.dat' and p['y'] == -48]
    for c in contacts:
        cx, cz = c['x'], c['z']
        si, sj = int((cx - min_x) // 20), int((cz - min_z) // 20)
        c_silicon_names = [b['name'] for b in named_silicon if (si, sj) in b['studs']]
        c_metal_names = [b['name'] for b in named_metal if (si, sj) in b['studs']]
        for s in c_silicon_names:
            for m in c_metal_names: connections.add((s, m))

    if not named_silicon or not named_metal: return ""
    active_s = [b['name'] for b in named_silicon]
    active_m = [b['name'] for b in named_metal]
    header = "| Silicon | " + " | ".join(active_m) + " |"
    sep = "| --- | " + " | ".join(["---"] * len(active_m)) + " |"
    rows = []
    for s in active_s:
        row_vals = ["X" if (s, m) in connections else " " for m in active_m]
        rows.append(f"| {s} | " + " | ".join(row_vals) + " |")
    return "## Connectivity Matrix\n\n" + header + "\n" + sep + "\n" + "\n".join(rows) + "\n\n"

def generate_design_doc(cell_name, parts, golden_sections):
    width_studs, _, min_x, min_z = get_dimensions(parts)
    height_studs = 15
    doc = f"# Design Documentation for {cell_name}\n\n"
    layers = [("Substrate", [0, -8]), ("Active", [-16]), ("Polysilicon", [-24]), ("Metal 1", [-56])]
    scale = "  " + "".join([str(i % 10) for i in range(width_studs)])
    for layer_name, y_list in layers:
        if (cell_name, layer_name) in golden_sections:
            doc += golden_sections[(cell_name, layer_name)] + "\n\n"
            continue
        doc += f"## {layer_name}\n```\n{scale}\n"
        used_chars, layer_lines = set(), []
        for z_idx in range(14, -1, -1):
            line = f"{z_idx % 10} "
            for x_idx in range(width_studs):
                sx, sz = min_x + x_idx * 20 + 10, min_z + z_idx * 20 + 10
                char = get_char_for_stud(parts, sx, sz, y_list, COLOR_MAP, {})
                line += char
                if char != ' ': used_chars.add(char)
            layer_lines.append(line.rstrip())
        doc += "\n".join(layer_lines) + "\n```\n"
        if layer_name == "Substrate": doc += "Legend: N=N-Well, S=Substrate\n"
        elif layer_name == "Active":
            lp = []
            if 'n' in used_chars: lp.append("n=NMOS Active")
            if 'p' in used_chars: lp.append("p=PMOS Active")
            if 'S' in used_chars: lp.append("S=Substrate fill (P)")
            if 'N' in used_chars: lp.append("N=Substrate fill (N)")
            doc += f"Legend: {', '.join(lp)}\n"
        elif layer_name == "Polysilicon": doc += "Legend: G=Polysilicon\n"
        elif layer_name == "Metal 1": doc += "Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)\n"
        doc += "\n"
    doc += generate_connectivity_matrix(parts, width_studs, height_studs, min_x, min_z)
    return doc

def main():
    if not os.path.exists('design'): os.makedirs('design')
    golden_sections = extract_golden_sections('design')
    golden_sections.update(extract_golden_sections('handmade'))
    for filename in os.listdir('models'):
        if filename.startswith('sg13g2_') and filename.endswith('.ldr'):
            cell_name = filename[:-4]
            parts = parse_ldr_full(os.path.join('models', filename))
            output_path = os.path.join('design', f"{cell_name}.md")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(generate_design_doc(cell_name, parts, golden_sections))
            print(f"Generated {output_path}")
    update_golden_standard_file(golden_sections)

if __name__ == "__main__": main()
