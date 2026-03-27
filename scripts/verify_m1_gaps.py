import os
import re

# Constants from MAPPING_RULEBOOK.md
CELL_HEIGHT_STUDS = 15

# LDraw Part dimensions for Metal 1 (plates and tiles)
PLATE_DIMENSIONS = {
    "91405.dat": (16, 16), "92438.dat": (16, 8), "3027.dat": (16, 6), "3456.dat": (14, 6),
    "3028.dat": (12, 6), "3033.dat": (10, 6), "3029.dat": (12, 4), "3036.dat": (8, 6),
    "3030.dat": (10, 4), "3958.dat": (6, 6), "4282.dat": (16, 2), "3035.dat": (8, 4),
    "2445.dat": (12, 2), "3032.dat": (6, 4), "3832.dat": (10, 2), "3034.dat": (8, 2),
    "3031.dat": (4, 4), "60479.dat": (12, 1), "3795.dat": (6, 2), "4477.dat": (10, 1),
    "3460.dat": (8, 1), "3020.dat": (4, 2), "3666.dat": (6, 1), "3021.dat": (3, 2),
    "3710.dat": (4, 1), "3022.dat": (2, 2), "3623.dat": (3, 1), "3023.dat": (2, 1),
    "3024.dat": (1, 1), "3070.dat": (1, 1),
}

def get_part_studs(p):
    pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
    tokens = p['line'].split()
    m0 = float(tokens[5])
    m2 = float(tokens[7])
    if abs(m0) < 0.1 and abs(m2) > 0.9: # Rotated
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

def verify_m1_gaps(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    parts = []
    current_label = "Unknown"
    for line in lines:
        line = line.strip()
        if line.startswith('0 //'):
            comment = line[4:].strip()
            if comment.startswith("Pin ") or "Rail" in comment or "Internal" in comment or "Obstructions" in comment:
                current_label = comment
        elif line.startswith('0 STEP'):
            pass # We don't reset label on STEP to avoid losing it for Metal 2 connections
        elif line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                color = int(tokens[1])
                x = float(tokens[2])
                y = float(tokens[3])
                z = float(tokens[4])
                part = tokens[14].lower()
                # Metal 1 is at Y = -56. Metal 2 connection tiles at Y = -64.
                if abs(y - (-56)) < 0.1 or abs(y - (-64)) < 0.1:
                    parts.append({
                        'x': x, 'z': z, 'color': color, 'part': part,
                        'label': current_label, 'line': line
                    })

    if not parts:
        return []

    # Map each stud to its net label
    stud_to_net = {}
    errors = []
    for p in parts:
        net = p['label']
        for sx, sz in get_part_studs(p):
            if (sx, sz) in stud_to_net and stud_to_net[(sx, sz)] != net:
                errors.append(f"Overlap at ({sx}, {sz}) between {net} and {stud_to_net[(sx, sz)]}")
            stud_to_net[(sx, sz)] = net

    # Check for gaps (4-neighbors only: N, S, E, W)
    for (sx, sz), net in stud_to_net.items():
        for dx, dz in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, nz = sx + dx, sz + dz
            if (nx, nz) in stud_to_net:
                other_net = stud_to_net[(nx, nz)]
                if other_net != net:
                    # Adjacent studs must have the same net
                    errors.append(f"Adjacency (no gap) at ({sx}, {sz}) and ({nx}, {nz}) between {net} and {other_net}")

    # Deduplicate errors
    unique_errors = sorted(list(set(errors)))
    return unique_errors

if __name__ == "__main__":
    import sys
    models_dir = 'models'
    all_passed = True
    files = [sys.argv[1]] if len(sys.argv) > 1 else sorted([os.path.join(models_dir, f) for f in os.listdir(models_dir) if f.endswith('.ldr')])
    for filepath in files:
        errs = verify_m1_gaps(filepath)
        if errs:
            print(f"FAIL: {os.path.basename(filepath)}")
            for e in errs: print(f"  - {e}")
            all_passed = False
        else:
            print(f"PASS: {os.path.basename(filepath)}")
    if not all_passed: sys.exit(1)
