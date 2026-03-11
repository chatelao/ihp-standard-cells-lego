import os
import re

def verify_ldr(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    errors = []
    has_substrate_low_v3 = False

    # Track which layers and colors we see
    found_colors = set()
    found_y_levels = set()
    found_round_bricks = False

    for line in lines:
        if line.startswith('0 // Substrate low (V3)'):
            has_substrate_low_v3 = True

        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+', line)
        if match:
            color = int(match.group(1))
            y = float(match.group(3))

            found_colors.add(color)
            found_y_levels.add(y)

            if "3062b.dat" in line:
                found_round_bricks = True

            # Check specific layer mappings based on V3 guidelines
            if y == 0:
                if color != 8:
                    errors.append(f"Invalid color {color} at Y=0 (expected 8)")
            elif y == -8:
                if color not in [8, 7]:
                    errors.append(f"Invalid color {color} at Y=-8 (expected 8 or 7)")
            elif y == -16:
                if color not in [288, 38]:
                    errors.append(f"Invalid color {color} at Y=-16 (expected 288 or 38)")
            elif y == -24:
                if color != 4:
                    errors.append(f"Invalid color {color} at Y=-24 (expected 4)")
            elif y == -48:
                if color != 15:
                    errors.append(f"Invalid color {color} at Y=-48 (expected 15)")
            elif y == -56:
                # Metal 1 (1), VDD (14), VSS (0)
                if color not in [1, 14, 0]:
                    errors.append(f"Invalid color {color} at Y=-56 (expected 1, 14, or 0)")
            elif y == -80:
                if color != 0:
                    errors.append(f"Invalid color {color} at Y=-80 (expected 0)")
            elif y == -88:
                # Metal 2 (2)
                if color != 2:
                    errors.append(f"Invalid color {color} at Y=-88 (expected 2)")

    if not has_substrate_low_v3:
        errors.append("Missing 'Substrate low (V3)' marker")

    # Check if we have at least some expected colors
    if 8 not in found_colors:
        errors.append("Missing color 8 (Substrate)")
    if -8 not in found_y_levels:
        errors.append("Missing Y=-8 layer (Substrate high/N-Well)")
    if -16 not in found_y_levels:
        errors.append("Missing Y=-16 layer (Active)")
    if -56 not in found_y_levels:
        errors.append("Missing Y=-56 layer (Metal 1/Rails)")

    # Note: Not all cells have Metal 2 or Contacts if they are simple (like fill cells)
    # But most standard cells should have contacts.

    return errors

def main():
    models_dir = 'models'
    all_passed = True
    for filename in sorted(os.listdir(models_dir)):
        if filename.endswith('.ldr'):
            errors = verify_ldr(os.path.join(models_dir, filename))
            if errors:
                print(f"FAIL: {filename}")
                for err in errors:
                    print(f"  - {err}")
                all_passed = False
            else:
                print(f"PASS: {filename}")

    if not all_passed:
        exit(1)

if __name__ == "__main__":
    main()
