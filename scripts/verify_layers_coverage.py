import os
import re
import sys

LDU_PER_STUD = 20

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
}

def verify_coverage(ldr_filepath):
    with open(ldr_filepath, 'r') as f:
        lines = f.readlines()

    layers_to_check = [0, -8, -16]
    layers_data = {y: [] for y in layers_to_check}

    global_min_x, global_max_x = float('inf'), float('-inf')
    global_min_z, global_max_z = float('inf'), float('-inf')

    for line in lines:
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+\s+){9}([\w.-]+)', line, re.IGNORECASE)
        if match:
            x, y, z, part = float(match.group(2)), float(match.group(3)), float(match.group(4)), match.group(6).lower()
            # Use small tolerance for float comparison of Y-coordinates
            target_y = next((ty for ty in layers_to_check if abs(y - ty) < 0.1), None)
            if target_y is not None:
                if part not in PLATE_DIMENSIONS:
                    continue # Skip non-plate parts if any

                pw, pd = PLATE_DIMENSIONS[part]
                parts = line.split()
                m0 = float(parts[5])
                m2 = float(parts[7])
                if abs(m0) < 0.1 and abs(m2) > 0.9: # Rotated
                    pw, pd = pd, pw

                half_w_ldu = (pw * LDU_PER_STUD) / 2
                half_d_ldu = (pd * LDU_PER_STUD) / 2

                x1, x2 = x - half_w_ldu, x + half_w_ldu
                z1, z2 = z - half_d_ldu, z + half_d_ldu

                layers_data[y].append(((x1, z1, x2, z2), part))

                global_min_x = min(global_min_x, x1)
                global_max_x = max(global_max_x, x2)
                global_min_z = min(global_min_z, z1)
                global_max_z = max(global_max_z, z2)

    if global_min_x == float('inf'):
        return [f"No plates found in the first three layers (0, -8, -16)."]

    # Align to grid using floor/ceil to avoid round-to-even issues
    import math
    global_min_x = int(math.floor(global_min_x / 20 + 0.1) * 20)
    global_max_x = int(math.ceil(global_max_x / 20 - 0.1) * 20)
    global_min_z = int(math.floor(global_min_z / 20 + 0.1) * 20)
    global_max_z = int(math.ceil(global_max_z / 20 - 0.1) * 20)

    w_studs = (global_max_x - global_min_x) // 20
    d_studs = (global_max_z - global_min_z) // 20

    errors = []
    for y in layers_to_check:
        grid = [[0 for _ in range(d_studs)] for _ in range(w_studs)]
        for (x1, z1, x2, z2), part in layers_data[y]:
            # Snap to grid using math.floor to avoid floating point issues
            ix1 = int(math.floor((x1 - global_min_x) / 20 + 0.1))
            iz1 = int(math.floor((z1 - global_min_z) / 20 + 0.1))
            ix2 = int(math.floor((x2 - global_min_x) / 20 + 0.1))
            iz2 = int(math.floor((z2 - global_min_z) / 20 + 0.1))

            for i in range(ix1, ix2):
                for j in range(iz1, iz2):
                    if 0 <= i < w_studs and 0 <= j < d_studs:
                        grid[i][j] += 1
                    else:
                        errors.append(f"Plate {part} at Y={y} is out of global bounds: stud ({i},{j})")

        for i in range(w_studs):
            for j in range(d_studs):
                if grid[i][j] == 0:
                    errors.append(f"Gap at Y={y}, stud ({i}, {j}) at world ({global_min_x + i*20}, {global_min_z + j*20})")
                elif grid[i][j] > 1:
                    errors.append(f"Overlap at Y={y}, stud ({i}, {j}) (count={grid[i][j]})")

    return errors

def main():
    models_dir = 'models'
    all_passed = True
    for filename in sorted(os.listdir(models_dir)):
        if filename.endswith('.ldr'):
            errors = verify_coverage(os.path.join(models_dir, filename))
            if errors:
                print(f"FAIL: {filename}")
                # Print unique errors to avoid flooding
                for err in sorted(list(set(errors))):
                    print(f"  - {err}")
                all_passed = False
            else:
                print(f"PASS: {filename}")

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
