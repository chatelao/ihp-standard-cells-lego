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
        if line.startswith('0 //'):
            comment = line[4:].strip()
            if comment.startswith("Pin ") or "Rail" in comment or "Internal" in comment:
                current_label = comment
        elif line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                color = int(tokens[1])
                x = float(tokens[2])
                y = float(tokens[3])
                z = float(tokens[4])
                rot = [float(t) for t in tokens[5:14]]
                part = tokens[14]
                parts.append({
                    'color': color,
                    'x': x, 'y': y, 'z': z,
                    'rot': rot, 'part': part,
                    'label': current_label
                })
    return parts

def get_part_studs(p):
    pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
    is_rotated = p['rot'][0] == 0
    if is_rotated:
        pw, pd = pd, pw
    half_w_ldu = (pw * 20) / 2
    half_d_ldu = (pd * 20) / 2
    min_x_stud = int(round((p['x'] - half_w_ldu) / 20))
    max_x_stud = int(round((p['x'] + half_w_ldu) / 20))
    min_z_stud = int(round((p['z'] - half_d_ldu) / 20))
    max_z_stud = int(round((p['z'] + half_d_ldu) / 20))
    studs = []
    for x in range(min_x_stud, max_x_stud):
        for z in range(min_z_stud, max_z_stud):
            studs.append((x, z))
    return studs

def find_blobs(parts, y_levels, color_filter=None):
    relevant_parts = [p for p in parts if p['y'] in y_levels and p['part'] not in ['3062b.dat', '6141.dat']]
    if color_filter is not None:
        relevant_parts = [p for p in relevant_parts if p['color'] in color_filter]
    if not relevant_parts: return []
    stud_to_parts = {}
    for i, p in enumerate(relevant_parts):
        for stud in get_part_studs(p):
            if stud not in stud_to_parts: stud_to_parts[stud] = []
            stud_to_parts[stud].append(i)
    visited = [False] * len(relevant_parts)
    blobs = []
    for i in range(len(relevant_parts)):
        if visited[i]: continue
        blob_parts_indices = []
        queue = [i]
        visited[i] = True
        while queue:
            curr_idx = queue.pop(0)
            blob_parts_indices.append(curr_idx)
            curr_part = relevant_parts[curr_idx]
            curr_studs = get_part_studs(curr_part)
            potential_neighbor_indices = set()
            for sx, sz in curr_studs:
                for idx in stud_to_parts.get((sx, sz), []): potential_neighbor_indices.add(idx)
                for dx, dz in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    for idx in stud_to_parts.get((sx + dx, sz + dz), []): potential_neighbor_indices.add(idx)
            for neighbor_idx in potential_neighbor_indices:
                if not visited[neighbor_idx]:
                    if relevant_parts[neighbor_idx]['color'] == curr_part['color']:
                        visited[neighbor_idx] = True
                        queue.append(neighbor_idx)
        blob_parts = [relevant_parts[idx] for idx in blob_parts_indices]
        blob_studs = set()
        for p in blob_parts: blob_studs.update(get_part_studs(p))
        labels = set(p['label'] for p in blob_parts if p['label'])
        label = list(labels)[0] if labels else None
        blobs.append({'label': label, 'color': blob_parts[0]['color'], 'studs': blob_studs, 'parts': blob_parts})
    return blobs

def get_blob_name(blob, category_counters):
    color = blob['color']
    label = blob['label']
    if label:
        if label.startswith("Pin "): return label[4:]
        if "VDD" in label:
            category_counters['VDD'] += 1
            return "VDD" if category_counters['VDD'] == 1 else f"VDD{category_counters['VDD']}"
        if "VSS" in label:
            category_counters['VSS'] += 1
            return "VSS" if category_counters['VSS'] == 1 else f"VSS{category_counters['VSS']}"
        if "Internal" in label:
            category_counters['Internal'] += 1
            return f"Internal{category_counters['Internal']}"
        return label
    cat = ""
    if color == 288: cat = "NMOS"
    elif color == 38: cat = "PMOS"
    elif color == 4: cat = "Poly"
    elif color == 9: cat = "Input"
    elif color == 272: cat = "Output"
    elif color == 1: cat = "Internal"
    elif color == 14:
        category_counters['VDD'] += 1
        return "VDD" if category_counters['VDD'] == 1 else f"VDD{category_counters['VDD']}"
    elif color == 0:
        category_counters['VSS'] += 1
        return "VSS" if category_counters['VSS'] == 1 else f"VSS{category_counters['VSS']}"
    else: cat = "Unknown"
    category_counters[cat] += 1
    return f"{cat}{category_counters[cat]}"

def get_char_for_stud(parts, x, z, layer_y_list, color_map, connection_map):
    char = ' '
    priority = {'+': 5, '-': 5, 'I': 4, 'O': 3, 'C': 2, 'S': 1, 'N': 1, 'n': 1, 'p': 1, 'G': 1}
    for p in sorted(parts, key=lambda p: priority.get(color_map.get(p['color'], ' '), 0), reverse=False):
        if p['y'] in layer_y_list and p['part'] != '3062b.dat':
            pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
            is_rotated = p['rot'][0] == 0
            if is_rotated: pw, pd = pd, pw
            half_w, half_d = (pw * 20) / 2, (pd * 20) / 2
            if (p['x'] - half_w <= x <= p['x'] + half_w) and (p['z'] - half_d <= z <= p['z'] + half_d):
                char = color_map.get(p['color'], char)
    if layer_y_list[0] == -56:
        has_contact_below = any(p['part'] == '3062b.dat' and p['y'] == -48 and abs(p['x']-x)<5 and abs(p['z']-z)<5 for p in parts)
        has_plate_above = any((p['part'] == '3024.dat' or p['part'] == '3070.dat') and p['y'] == -64 and abs(p['x']-x)<5 and abs(p['z']-z)<5 for p in parts)
        if has_contact_below or has_plate_above:
            return {'I': 'i', 'O': 'o', 'C': 'c', '+': '&', '-': '_'}.get(char, 'c')
    return char

COLOR_MAP = {8: 'S', 7: 'N', 288: 'n', 38: 'p', 4: 'G', 9: 'I', 1: 'C', 272: 'O', 14: '+', 0: '-'}

def extract_golden_sections(design_dir):
    golden_sections = {}
    gs_path = 'specifications/GOLDEN_STANDARD.md'
    if os.path.exists(gs_path):
        with open(gs_path, 'r', encoding='utf-8') as f: content = f.read()
        header = "## 7. Golden Design Examples"
        if header in content:
            examples_part = content.split(header)[1]
            pattern = r'### (sg13g2_[a-z0-9_]+) - ([A-Za-z0-9 ]+)\n(.*?)(?=\n### |\n## |$)'
            matches = re.findall(pattern, examples_part, re.DOTALL)
            for cell_name, layer_name, text in matches:
                golden_sections[(cell_name, layer_name)] = f"## {layer_name}\n{text.strip()}"
    if not os.path.exists(design_dir): return golden_sections
    for filename in os.listdir(design_dir):
        if filename.endswith('.md'):
            cell_name = filename[:-3]
            with open(os.path.join(design_dir, filename), 'r', encoding='utf-8') as f: content = f.read()
            sections = content.split('\n## ')
            for section in sections[1:]:
                if 'GOLDEN STANDARD' in section:
                    layer_name = section.split('\n')[0].strip()
                    golden_sections[(cell_name, layer_name)] = '## ' + section.strip()
    return golden_sections

def update_golden_standard_file(all_golden):
    filepath = 'specifications/GOLDEN_STANDARD.md'
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
    header = "## 7. Golden Design Examples"
    if all_golden:
        new_text = header + "\n"
        for (cell, layer), text in sorted(all_golden.items()):
            new_text += f"### {cell} - {layer}\n" + '\n'.join(text.split('\n')[1:]).strip() + "\n\n"
        new_text = new_text.strip() + "\n"
    else: new_text = ""
    if header in content:
        before = content.split(header)[0]
        after_match = re.search(r'\n## [8-9]\.', content.split(header)[1])
        after = content.split(header)[1][after_match.start():] if after_match else ""
        content = before + new_text + after
    elif new_text: content = content.strip() + "\n\n" + new_text
    with open(filepath, 'w', encoding='utf-8') as f: f.write(content)

def generate_connectivity_matrix(parts, nmos_blobs, pmos_blobs, poly_blobs, metal_blobs):
    silicon_blobs = nmos_blobs + pmos_blobs + poly_blobs
    connections = set()
    contacts = [p for p in parts if p['part'] == '3062b.dat' and p['y'] == -48]
    for c in contacts:
        c_stud = (int(round((c['x'] - 10) / 20)), int(round((c['z'] - 10) / 20)))
        connected_silicon = [b for b in silicon_blobs if c_stud in b['studs']]
        connected_metal = [b for b in metal_blobs if c_stud in b['studs']]
        for s in connected_silicon:
            for m in connected_metal: connections.add((s['name'], m['name'], m['color']))
    if not connections: return ""
    s_names = sorted(list(set(c[0] for c in connections)))
    m_info = {name: color for _, name, color in connections}
    def metal_sort_key(name):
        color = m_info[name]
        return ({9: 0, 1: 1, 272: 2, 14: 3, 0: 4}.get(color, 5), name)
    m_names = sorted(list(set(c[1] for c in connections)), key=metal_sort_key)
    header = "| Silicon | " + " | ".join(m_names) + " |"
    sep = "| --- | " + " | ".join(["---"] * len(m_names)) + " |"
    rows = []
    for s in s_names:
        row = f"| {s} | " + " | ".join("X" if any(c[0]==s and c[1]==m for c in connections) else " " for m in m_names) + " |"
        rows.append(row)
    return "## Connectivity Matrix\n\n" + header + "\n" + sep + "\n" + "\n".join(rows) + "\n\n"

def generate_silicon_neighbourhood(parts, nmos_blobs, pmos_blobs, poly_blobs):
    all_blobs = nmos_blobs + pmos_blobs + poly_blobs
    overlaps = set()
    for i in range(len(all_blobs)):
        for j in range(i + 1, len(all_blobs)):
            if all_blobs[i]['studs'].intersection(all_blobs[j]['studs']):
                overlaps.add(tuple(sorted((all_blobs[i]['name'], all_blobs[j]['name']))))
    if not overlaps: return ""
    rows = [f"| {s1} | {s2} |" for s1, s2 in sorted(list(overlaps))]
    return "## Silicon Neighbourhood\n\n| Silicon | Overlaps With |\n| --- | --- |\n" + "\n".join(rows) + "\n\n"

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
        used_chars = set()
        layer_lines = []
        for z_idx in range(14, -1, -1):
            line = f"{z_idx % 10} "
            for x_idx in range(width_studs):
                char = get_char_for_stud(parts, min_x+x_idx*20+10, min_z+z_idx*20+10, y_list, COLOR_MAP, {})
                line += char
                if char != ' ': used_chars.add(char)
            layer_lines.append(line.rstrip())
        doc += "\n".join(layer_lines) + "\n```\n"
        if layer_name == "Substrate": doc += "Legend: N=N-Well, S=Substrate\n"
        elif layer_name == "Active":
            legend = []
            if 'n' in used_chars: legend.append("n=NMOS Active")
            if 'p' in used_chars: legend.append("p=PMOS Active")
            if 'S' in used_chars: legend.append("S=Substrate fill (P)")
            if 'N' in used_chars: legend.append("N=Substrate fill (N)")
            doc += f"Legend: {', '.join(legend)}\n"
        elif layer_name == "Polysilicon": doc += "Legend: G=Polysilicon\n"
        elif layer_name == "Metal 1": doc += "Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)\n"
        doc += "\n"

    nmos_blobs = find_blobs(parts, [-16], [288])
    pmos_blobs = find_blobs(parts, [-16], [38])
    poly_blobs = find_blobs(parts, [-24], [4])
    metal_blobs = find_blobs(parts, [-56, -64], [14, 0, 9, 272, 1])
    counters = {'NMOS': 0, 'PMOS': 0, 'Poly': 0, 'Input': 0, 'Output': 0, 'Internal': 0, 'VDD': 0, 'VSS': 0}
    for b in nmos_blobs: b['name'] = get_blob_name(b, counters)
    for b in pmos_blobs: b['name'] = get_blob_name(b, counters)
    for b in poly_blobs: b['name'] = get_blob_name(b, counters)
    for b in metal_blobs: b['name'] = get_blob_name(b, counters)

    doc += generate_connectivity_matrix(parts, nmos_blobs, pmos_blobs, poly_blobs, metal_blobs)
    doc += generate_silicon_neighbourhood(parts, nmos_blobs, pmos_blobs, poly_blobs)
    return doc

def main():
    if not os.path.exists('design'): os.makedirs('design')
    golden = extract_golden_sections('design')
    golden.update(extract_golden_sections('handmade'))
    for filename in os.listdir('models'):
        if filename.startswith('sg13g2_') and filename.endswith('.ldr'):
            cell_name = filename[:-4]
            parts = parse_ldr_full(os.path.join('models', filename))
            doc = generate_design_doc(cell_name, parts, golden)
            with open(os.path.join('design', f"{cell_name}.md"), 'w', encoding='utf-8') as f: f.write(doc)
            print(f"Generated design/{cell_name}.md")
    update_golden_standard_file(golden)

if __name__ == "__main__": main()
