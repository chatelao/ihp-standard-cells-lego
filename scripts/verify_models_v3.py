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
    "3024.dat": (1, 1), "3070.dat": (1, 1), "3070b.dat": (1, 1), "6141.dat": (1, 1), "3062b.dat": (1, 1),
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
    """
    Unified parity rule for active and gate tracks (Z=2..12):
    - Small models (width <= 7): Always ODD (1).
    - Big models (> 7 studs): Symmetric parity - ODD if X < 8, EVEN if X >= 8.
    """
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
    import sys
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    from generate_design_docs import parse_ldr_full, find_blobs, get_blob_name

    parts = parse_ldr_full(filepath)
    nmos_blobs = find_blobs(parts, [-16], [288])
    pmos_blobs = find_blobs(parts, [-16], [38])
    poly_blobs = find_blobs(parts, [-24], [4])
    metal_blobs = find_blobs(parts, [-56, -64], [14, 0, 9, 212, 272, 1])
    counters = {'NMOS': 0, 'PMOS': 0, 'Poly': 0, 'Input': 0, 'Output': 0, 'Internal': 0, 'VDD': 0, 'VSS': 0}
    for b in nmos_blobs:
        b['name'] = get_blob_name(b, counters)
        b['cat'] = 'NMOS'
    for b in pmos_blobs:
        b['name'] = get_blob_name(b, counters)
        b['cat'] = 'PMOS'
    for b in poly_blobs:
        b['name'] = get_blob_name(b, counters)
        b['cat'] = 'Poly'
    for b in metal_blobs:
        b['name'] = get_blob_name(b, counters)

    silicon_blobs = nmos_blobs + pmos_blobs + poly_blobs
    connections = {}
    contacts = [p for p in parts if p['part'] == '3062b.dat' and p['y'] == -48 and p['color'] != 47]
    for c in contacts:
        c_stud = (int(round((c['x']-10)/20)), int(round((c['z']-10)/20)))
        connected_silicon = [b for b in silicon_blobs if c_stud in b['studs']]
        connected_metal = [b for b in metal_blobs if c_stud in b['studs']]
        for s in connected_silicon:
            if s['name'] not in connections: connections[s['name']] = set()
            for m in connected_metal: connections[s['name']].add(m['name'])
    return connections

def verify_ldr(filepath):
    filename = os.path.basename(filepath)
    cell_name = filename.replace(".ldr", "")
    is_nand2b_2_exception = os.path.exists(os.path.join("handmade", f"{cell_name}.md"))

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
            # Electrical contacts only (White 15); Trans-Clear (47) dielectric supports can sit at any M1 stud
            if (y == -48 and color == 15) or (y == -24 and color == 15):
                if not is_nand2b_2_exception:
                    if stud_z % 2 != 0:
                        errors.append(f"Contact at Stud Z={stud_z} is on an ODD track (expected EVEN)")

                    # Rail Parity is strict: MUST be EVEN for Track 0 and 14
                    if stud_z in [0, 14]:
                        if stud_x % 2 != 0:
                            errors.append(f"{'VDD' if stud_z == 14 else 'VSS'} contact at Stud X={stud_x} on Track {stud_z} has incorrect parity (expected EVEN)")
            if y == -8 and color in (7, 71):
                if stud_z < 5: errors.append(f"N-Well at Stud Z={stud_z} extends below Stud 5")
            elif y == -16:
                if color == 288:
                    if not (1 <= stud_z <= 7) and not (stud_z == 0): errors.append(f"NMOS Active at Stud Z={stud_z} outside standard Studs 1-7/0")
                elif color == 38:
                    if not (7 <= stud_z <= 13) and not (stud_z == 14): errors.append(f"PMOS Active at Stud Z={stud_z} outside standard Studs 7-13/14")

    if not has_substrate_low_v3: errors.append("Missing 'Substrate low (V3)' marker")
    if 8 not in found_colors and 72 not in found_colors: errors.append("Missing Substrate color (8/72)")
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
