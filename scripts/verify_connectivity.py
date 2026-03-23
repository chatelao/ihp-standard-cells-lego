import os
import re
import sys

# Standard LEGO part dimensions for tiling
PLATE_DIMENSIONS = {
    "91405.dat": (16, 16), "92438.dat": (16, 8), "3027.dat": (16, 6), "3456.dat": (14, 6),
    "3028.dat": (12, 6), "3033.dat": (10, 6), "3029.dat": (12, 4), "3036.dat": (8, 6),
    "3030.dat": (10, 4), "3958.dat": (6, 6), "4282.dat": (16, 2), "3035.dat": (8, 4),
    "2445.dat": (12, 2), "3032.dat": (6, 4), "3832.dat": (10, 2), "3034.dat": (8, 2),
    "3031.dat": (4, 4), "60479.dat": (12, 1), "3795.dat": (6, 2), "4477.dat": (10, 1),
    "3460.dat": (8, 1), "3020.dat": (4, 2), "3666.dat": (6, 1), "3021.dat": (3, 2),
    "3710.dat": (4, 1), "3022.dat": (2, 2), "3623.dat": (3, 1), "3023.dat": (2, 1),
    "3024.dat": (1, 1), "3070.dat": (1, 1), "6141.dat": (1, 1), "3062b.dat": (1, 1),
}

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
        elif line.startswith('0 STEP'):
            current_label = None
        elif line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                color = int(tokens[1])
                x, y, z = float(tokens[2]), float(tokens[3]), float(tokens[4])
                rot = [float(t) for t in tokens[5:14]]
                part = tokens[14]
                parts.append({'color': color, 'x': x, 'y': y, 'z': z, 'rot': rot, 'part': part, 'label': current_label})
    return parts

def get_part_studs(p):
    pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
    is_rotated = p['rot'][0] == 0
    if is_rotated: pw, pd = pd, pw
    half_w_ldu, half_d_ldu = (pw * 20) / 2, (pd * 20) / 2
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
        blob_parts_indices, queue = [], [i]
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
        label = None
        if labels:
            pin_labels = [l for l in labels if l.startswith("Pin ")]
            rail_labels = [l for l in labels if "Rail" in l]
            if pin_labels: label = pin_labels[0]
            elif rail_labels: label = rail_labels[0]
            else: label = list(labels)[0]
        blobs.append({'label': label, 'color': blob_parts[0]['color'], 'studs': blob_studs, 'parts': blob_parts})
    return blobs

def get_blob_name(blob, category_counters):
    color, label = blob['color'], blob['label']

    # 1. Trust "Pin " labels above all
    if label and label.startswith("Pin "):
        name = label[4:]
        if name.endswith(" Rail"): name = name[:-5]
        return name

    # 2. Special case for VDD/VSS Rails
    if label and "Rail" in label:
        if "VDD" in label: return "VDD"
        if "VSS" in label: return "VSS"

    # 3. Standard Pin naming
    if color == 14: # VDD
        category_counters['VDD'] += 1
        return "VDD" if category_counters['VDD'] == 1 else f"VDD{category_counters['VDD']}"
    if color == 0: # VSS
        category_counters['VSS'] += 1
        return "VSS" if category_counters['VSS'] == 1 else f"VSS{category_counters['VSS']}"
    if color == 9: # Input
        category_counters['Input'] += 1
        return f"Input{category_counters['Input']}"
    if color == 272: # Output
        category_counters['Output'] += 1
        return f"Output{category_counters['Output']}"

    cat = "NMOS" if color == 288 else "PMOS" if color == 38 else "Poly" if color == 4 else "Internal" if color == 1 else "Unknown"
    category_counters[cat] += 1
    return f"{cat}{category_counters[cat]}"

def get_physical_connections(parts):
    nmos_blobs = find_blobs(parts, [-16], [288])
    pmos_blobs = find_blobs(parts, [-16], [38])
    poly_blobs = find_blobs(parts, [-24], [4])
    metal_blobs = find_blobs(parts, [-56, -64], [14, 0, 9, 272, 1])

    # Sort blobs for stable naming across different LDR part orderings
    def blob_sort_key(b):
        if not b['studs']: return (0, 0)
        min_x = min(s[0] for s in b['studs'])
        min_z = min(s[1] for s in b['studs'])
        return (min_z, min_x)

    nmos_blobs.sort(key=blob_sort_key)
    pmos_blobs.sort(key=blob_sort_key)
    poly_blobs.sort(key=blob_sort_key)
    metal_blobs.sort(key=blob_sort_key)

    counters = {'NMOS': 0, 'PMOS': 0, 'Poly': 0, 'Input': 0, 'Output': 0, 'Internal': 0, 'VDD': 0, 'VSS': 0}
    for b in nmos_blobs + pmos_blobs + poly_blobs + metal_blobs: b['name'] = get_blob_name(b, counters)

    connections = set()
    contacts = [p for p in parts if p['part'] == '3062b.dat' and p['y'] == -48]
    bridge_plates = set((int(round((p['x'] - 10) / 20)), int(round((p['z'] - 10) / 20))) for p in parts if p['part'] == '6141.dat' and p['y'] == -24)
    for c in contacts:
        c_stud = (int(round((c['x'] - 10) / 20)), int(round((c['z'] - 10) / 20)))
        has_bridge = c_stud in bridge_plates
        target_silicon = nmos_blobs + pmos_blobs if has_bridge else poly_blobs
        connected_silicon = [b for b in target_silicon if c_stud in b['studs']]
        connected_metal = [b for b in metal_blobs if c_stud in b['studs']]
        for s in connected_silicon:
            for m in connected_metal: connections.add((s['name'], m['name']))
    return connections

def parse_md_matrix(md_filepath):
    with open(md_filepath, 'r', encoding='utf-8') as f: content = f.read()
    match = re.search(r'## Connectivity Matrix\n\n\| Silicon \| (.*?) \|\n\| --- \| (.*?) \|\n(.*?)(?:\n\n|\n##|$)', content, re.DOTALL)
    if not match: return set()

    # Improved parsing for headers to skip the first empty and 'Silicon'
    header_line = match.group(1)
    # Header line is " B | VSS2 | X | VDD | VSS "
    headers = [h.strip() for h in header_line.split('|') if h.strip()]

    rows = match.group(3).strip().split('\n')
    matrix_connections = set()
    for row in rows:
        cells = [c.strip() for c in row.split('|')]
        # Row format: | Silicon | Col1 | Col2 | ... |
        # Split by |: ['', 'NMOS2', 'X', 'X', 'X', ' ', 'X', '']
        # The filter(None) or if h.strip() might be skipping empty columns that ARE in headers

        if len(cells) < 3: continue
        silicon_name = cells[1]

        # We need to find which indices in 'cells' correspond to which 'headers'
        # cells[0] is '', cells[1] is 'NMOS2', cells[2] is 'X', etc.
        # Header names start at index 2 of 'cells'
        for i, h_name in enumerate(headers):
            cell_idx = i + 2
            if cell_idx < len(cells):
                if cells[cell_idx].upper() == 'X':
                    matrix_connections.add((silicon_name, h_name))
    return matrix_connections

def main():
    design_dir, models_dir = 'design', 'models'
    all_passed = True
    for filename in sorted(os.listdir(design_dir)):
        if filename.endswith('.md'):
            cell_name = filename[:-3]
            ldr_path = os.path.join(models_dir, f"{cell_name}.ldr")
            if not os.path.exists(ldr_path): continue
            md_conn = parse_md_matrix(os.path.join(design_dir, filename))
            ldr_parts = parse_ldr_full(ldr_path)
            ldr_conn = get_physical_connections(ldr_parts)
            if md_conn != ldr_conn:
                print(f"FAIL: {cell_name} - Connectivity Matrix mismatch")
                missing = md_conn - ldr_conn
                extra = ldr_conn - md_conn
                if missing:
                    print(f"  Missing (in MD but not in LDR):")
                    for m in sorted(list(missing)): print(f"    {m[0]} -> {m[1]}")
                if extra:
                    print(f"  Extra (in LDR but not in MD):")
                    for e in sorted(list(extra)): print(f"    {e[0]} -> {e[1]}")

                # Debug: show what was found in each
                # print(f"  MD Headers found: {parse_md_matrix_headers(os.path.join(design_dir, filename))}")

                all_passed = False
            else: print(f"PASS: {cell_name}")

def parse_md_matrix_headers(md_filepath):
    with open(md_filepath, 'r', encoding='utf-8') as f: content = f.read()
    match = re.search(r'## Connectivity Matrix\n\n\| Silicon \| (.*?) \|\n', content)
    if not match: return []
    return [h.strip() for h in match.group(1).split('|') if h.strip()]
    if not all_passed: sys.exit(1)

if __name__ == "__main__": main()
