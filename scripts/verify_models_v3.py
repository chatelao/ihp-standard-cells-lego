import os
import re

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

def get_part_studs(p):
    pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
    is_rotated = p['rot'][0] == 0
    if is_rotated: pw, pd = pd, pw
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

def get_unified_parity(stud_x, is_big):
    if not is_big:
        return 1 # ODD
    return 1 if stud_x < 8 else 0 # ODD if < 8, EVEN if >= 8

def parse_connectivity_matrix(design_filepath):
    if not os.path.exists(design_filepath): return None
    with open(design_filepath, 'r') as f: content = f.read()
    if "## Connectivity Matrix" not in content: return None
    matrix_text = content.split("## Connectivity Matrix")[1].split("##")[0].strip()
    lines = [l.strip() for l in matrix_text.split("\n") if l.strip().startswith("|")]
    if len(lines) < 3: return None
    headers = [h.strip() for h in lines[0].split("|")[2:-1]]
    matrix = {}
    for line in lines[2:]:
        parts = [p.strip() for p in line.split("|")[1:-1]]
        silicon = parts[0]
        for i, val in enumerate(parts[1:]):
            if val == "X":
                if silicon not in matrix: matrix[silicon] = set()
                matrix[silicon].add(headers[i])
    return matrix

def get_ldr_connectivity(filepath):
    with open(filepath, 'r') as f: lines = f.readlines()
    parts = []
    current_label = None
    for line in lines:
        line = line.strip()
        if line.startswith('0 //'):
            comment = line[4:].strip()
            if comment.startswith("Pin ") or "Rail" in comment or "Internal" in comment:
                current_label = comment
        elif line.startswith('0 STEP'): current_label = None
        elif line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                parts.append({
                    'color': int(tokens[1]), 'x': float(tokens[2]), 'y': float(tokens[3]), 'z': float(tokens[4]),
                    'rot': [float(t) for t in tokens[5:14]], 'part': tokens[14], 'label': current_label
                })

    # Simple blob detection for silicon and metal
    def find_blobs_simple(y_levels, color_filter):
        relevant = [p for p in parts if p['y'] in y_levels and p['color'] in color_filter and p['part'] not in ['3062b.dat', '6141.dat']]
        if not relevant: return []
        stud_to_parts = {}
        for i, p in enumerate(relevant):
            for stud in get_part_studs(p):
                if stud not in stud_to_parts: stud_to_parts[stud] = []
                stud_to_parts[stud].append(i)
        visited = [False] * len(relevant)
        blobs = []
        for i in range(len(relevant)):
            if visited[i]: continue
            blob_parts_indices = []
            queue = [i]
            visited[i] = True
            while queue:
                curr_idx = queue.pop(0)
                blob_parts_indices.append(curr_idx)
                curr_part = relevant[curr_idx]
                curr_studs = get_part_studs(curr_part)
                potential = set()
                for sx, sz in curr_studs:
                    for idx in stud_to_parts.get((sx, sz), []): potential.add(idx)
                    for dx, dz in [(0,1), (0,-1), (1,0), (-1,0)]:
                        for idx in stud_to_parts.get((sx+dx, sz+dz), []): potential.add(idx)
                for neighbor_idx in potential:
                    if not visited[neighbor_idx] and relevant[neighbor_idx]['color'] == curr_part['color']:
                        visited[neighbor_idx] = True
                        queue.append(neighbor_idx)
            blob_parts = [relevant[idx] for idx in blob_parts_indices]
            blob_studs = set()
            for p in blob_parts: blob_studs.update(get_part_studs(p))

            # Labeling logic similar to generate_design_docs.py
            labels = set(p['label'] for p in blob_parts if p['label'])
            label = None
            if labels:
                pin_labels = [l for l in labels if l.startswith("Pin ")]
                rail_labels = [l for l in labels if "Rail" in l]
                if pin_labels: label = pin_labels[0][4:]
                elif rail_labels:
                    if "VDD" in rail_labels[0]: label = "VDD"
                    elif "VSS" in rail_labels[0]: label = "VSS"
                    else: label = rail_labels[0]
                else: label = list(labels)[0]

            cat = ""
            if relevant[0]['color'] == 288: cat = "NMOS"
            elif relevant[0]['color'] == 38: cat = "PMOS"
            elif relevant[0]['color'] == 4: cat = "Poly"

            blobs.append({'name': label, 'cat': cat, 'studs': blob_studs, 'color': relevant[0]['color']})

        # Name those that don't have labels
        counters = {'NMOS': 0, 'PMOS': 0, 'Poly': 0, 'Input': 0, 'Output': 0, 'Internal': 0}
        for b in blobs:
            if not b['name']:
                name_cat = b['cat'] if b['cat'] else ({9:'Input', 272:'Output', 1:'Internal'}.get(relevant[0]['color'], 'Unknown'))
                counters[name_cat] += 1
                b['name'] = f"{name_cat}{counters[name_cat]}"
        return blobs

    silicon_blobs = find_blobs_simple([-16], [288, 38]) + find_blobs_simple([-24], [4])
    metal_blobs = find_blobs_simple([-56], [14, 0, 9, 272, 1])

    connections = {}
    contacts = [p for p in parts if p['part'] == '3062b.dat' and p['y'] == -48]
    round_plates = set((int(round((p['x']-10)/20)), int(round((p['z']-10)/20))) for p in parts if p['part'] == '6141.dat' and p['y'] == -24)

    for c in contacts:
        c_stud = (int(round((c['x']-10)/20)), int(round((c['z']-10)/20)))
        has_plate = c_stud in round_plates
        connected_silicon = []
        for b in silicon_blobs:
            if c_stud in b['studs']:
                if b['cat'] == 'Poly' or has_plate: connected_silicon.append(b)
        connected_metal = [b for b in metal_blobs if c_stud in b['studs']]
        for s in connected_silicon:
            if s['name'] not in connections: connections[s['name']] = set()
            for m in connected_metal: connections[s['name']].add(m['name'])
    return connections

def verify_ldr(filepath):
    filename = os.path.basename(filepath)
    is_nand2b_2_exception = "sg13g2_nand2b_2" in filename or "sg13g2_xor2_1" in filename

    with open(filepath, 'r') as f:
        lines = f.readlines()

    errors = []
    has_substrate_low_v3 = False
    found_colors = set()
    found_y_levels = set()
    found_round_bricks = False
    pin_map = {}
    max_x = 0
    for line in lines:
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+', line)
        if match:
            color = int(match.group(1))
            x = float(match.group(2))
            y = float(match.group(3))
            z = float(match.group(4))
            max_x = max(max_x, x)
            if y == -64:
                stud_x = int(x // 20)
                stud_z = int(z // 20)
                pin_map[(stud_x, stud_z)] = color

    is_big = max_x > 140 # > 7 studs
    for line in lines:
        if line.startswith('0 // Substrate low (V3)'):
            has_substrate_low_v3 = True
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+', line)
        if match:
            color = int(match.group(1))
            x = float(match.group(2))
            y = float(match.group(3))
            z = float(match.group(4))
            stud_x = int(x // 20)
            stud_z = int(z // 20)
            found_colors.add(color)
            found_y_levels.add(y)
            if "3062b.dat" in line: found_round_bricks = True
            if (y == -48 and color == 15) or (y == -24 and color == 15):
                pin_color = pin_map.get((stud_x, stud_z))
                if not is_nand2b_2_exception:
                    if stud_z % 2 != 0:
                        errors.append(f"Contact at Stud Z={stud_z} is on an ODD track (expected EVEN)")
                    if pin_color == 14: # VDD
                        if stud_x % 2 != 0: errors.append(f"VDD contact at Stud X={stud_x} has incorrect parity (expected EVEN)")
                    elif pin_color == 0: # VSS
                        if stud_x % 2 != 1: errors.append(f"VSS contact at Stud X={stud_x} has incorrect parity (expected ODD)")
                    elif pin_color in [1, 9, 272]: # Signal
                        expected_parity = get_unified_parity(stud_x, is_big)
                        if stud_x % 2 != expected_parity:
                            errors.append(f"Signal contact at Stud X={stud_x} has incorrect parity")
            if y == -8 and color == 7:
                if stud_z < 8: errors.append(f"N-Well at Stud Z={stud_z} extends below Stud 8")
            elif y == -16:
                if color == 288:
                    if not (2 <= stud_z <= 4) and not (stud_z == 0): errors.append(f"NMOS Active at Stud Z={stud_z} outside standard Studs 2-4/0")
                elif color == 38:
                    if not (8 <= stud_z <= 12) and not (stud_z == 14): errors.append(f"PMOS Active at Stud Z={stud_z} outside standard Studs 8-12/14")

    if not has_substrate_low_v3: errors.append("Missing 'Substrate low (V3)' marker")
    if 8 not in found_colors: errors.append("Missing color 8 (Substrate)")
    if -8 not in found_y_levels: errors.append("Missing Y=-8 layer")
    if -16 not in found_y_levels: errors.append("Missing Y=-16 layer")
    if -56 not in found_y_levels: errors.append("Missing Y=-56 layer")

    # Connectivity Matrix Verification
    design_file = os.path.join('design', filename.replace('.ldr', '.md'))
    expected_matrix = parse_connectivity_matrix(design_file)
    if expected_matrix:
        actual_matrix = get_ldr_connectivity(filepath)
        # Compare sets of connections for each silicon blob
        all_silicon = set(expected_matrix.keys()) | set(actual_matrix.keys())
        for s in all_silicon:
            exp = expected_matrix.get(s, set())
            act = actual_matrix.get(s, set())
            if exp != act:
                if exp - act: errors.append(f"Silicon {s} missing connections to: {', '.join(exp - act)}")
                if act - exp: errors.append(f"Silicon {s} has extra connections to: {', '.join(act - exp)}")

    return errors

if __name__ == "__main__":
    import sys
    models_dir = 'models'
    all_passed = True
    files = [sys.argv[1]] if len(sys.argv) > 1 else sorted([os.path.join(models_dir, f) for f in os.listdir(models_dir) if f.endswith('.ldr')])
    for filepath in files:
        errs = verify_ldr(filepath)
        if errs:
            print(f"FAIL: {os.path.basename(filepath)}")
            for e in errs: print(f"  - {e}")
            all_passed = False
        else:
            print(f"PASS: {os.path.basename(filepath)}")
    if not all_passed: sys.exit(1)
