import os
import re

def verify_ldr(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    errors = []
    has_substrate_low = False

    # Track which layers and colors we see
    found_colors = set()
    found_y_levels = set()

    for line in lines:
        if line.startswith('0 // Substrate low (V3)'):
            has_substrate_low = True

        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+', line)
        if match:
            color = int(match.group(1))
            y = float(match.group(3))

            found_colors.add(color)
            found_y_levels.add(y)

            # Check specific layer mappings (V3)
            if y == 0:
                if color != 8:
                    errors.append(f"Invalid color {color} at Y=0 (expected 8)")
            elif y == -8:
                if color not in [8, 7]:
                    errors.append(f"Invalid color {color} at Y=-8 (expected 8 or 7)")
            elif y == -16:
                if color not in [288, 38, 15]:
                    errors.append(f"Invalid color {color} at Y=-16 (expected 288, 38, or 15)")
            elif y == -32:
                if color not in [1, 14, 0, 15]:
                    errors.append(f"Invalid color {color} at Y=-32 (expected 1, 14, 0, or 15)")
            elif y == -56:
                if color != 2:
                    errors.append(f"Invalid color {color} at Y=-56 (expected 2)")

    if not has_substrate_low:
        errors.append("Missing 'Substrate low (V3)' marker")

    if 8 not in found_colors:
        errors.append("Missing color 8 (Substrate)")
    if -8 not in found_y_levels:
        errors.append("Missing Y=-8 layer")
    if -16 not in found_y_levels:
        errors.append("Missing Y=-16 layer (Diffusion)")
    if -32 not in found_y_levels:
        errors.append("Missing Y=-32 layer (Metal 1)")

    return errors

def main():
    models_dir = 'models'
    all_passed = True
    for filename in os.listdir(models_dir):
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
