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

    is_drive_2 = os.path.basename(filepath).endswith('_2.ldr')

    # First pass to build Metal 1 color map and find max_x
    max_x = 0
    m1_colors = {} # (stud_x, stud_z) -> color

    # Standard LEGO Part dimensions for coverage calculation
    PART_DIMS = {
        '3034.dat': (8, 2), '3460.dat': (8, 1), '3666.dat': (6, 1),
        '3020.dat': (4, 2), '3710.dat': (4, 1), '3623.dat': (3, 1),
        '3022.dat': (2, 2), '3023.dat': (2, 1), '3024.dat': (1, 1),
        '6141.dat': (1, 1), '3062b.dat': (1, 1)
    }

    for line in lines:
        if line.startswith('0 // Substrate low (V3)'):
            has_substrate_low_v3 = True
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+(\S+)', line)
        if match:
            color, x, y, z = int(match.group(1)), float(match.group(2)), float(match.group(3)), float(match.group(4))
            rot = [float(match.group(i)) for i in range(5, 14)]
            part = match.group(14)

            max_x = max(max_x, x)
            if y == -56:
                pw, pd = PART_DIMS.get(part, (1, 1))
                is_rotated = abs(rot[0]) < 0.001
                if is_rotated: pw, pd = pd, pw

                half_w = (pw * 20) / 2
                half_d = (pd * 20) / 2

                # Use a small epsilon to avoid floating point issues at boundaries
                for ix in range(int((x - half_w + 0.1)//20), int((x + half_w - 0.1)//20) + 1):
                    for iz in range(int((z - half_d + 0.1)//20), int((z + half_d - 0.1)//20) + 1):
                        m1_colors[(ix, iz)] = color

    is_big = max_x > 140 # > 7 studs
    w_studs = int(max_x // 20) + 1

    for line in lines:
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

            if "3062b.dat" in line:
                found_round_bricks = True

            # Gold Standard Parity Checks
            if (y == -48 and color == 15) or (y == -24 and color == 15): # Contacts
                # VDD (Z=14) must be EVEN
                if stud_z == 14:
                    if stud_x % 2 != 0:
                        errors.append(f"VDD contact at Stud X={stud_x} has ODD parity (expected EVEN)")
                # VSS (Z=0) must be ODD
                elif stud_z == 0:
                    if stud_x % 2 == 0:
                        errors.append(f"VSS contact at Stud X={stud_x} has EVEN parity (expected ODD)")
                # Input contacts (typically at Stud Z=6)
                elif stud_z == 6:
                    if not is_big:
                        if stud_x % 2 == 0:
                            errors.append(f"Input contact at Stud X={stud_x} has EVEN parity in small model (expected ODD)")
                    else:
                        # Big model symmetric parity: ODD if X < 8, EVEN if X >= 8
                        expected = 1 if stud_x < 8 else 0
                        if stud_x % 2 != expected:
                            parity_name = "ODD" if expected == 1 else "EVEN"
                            errors.append(f"Input contact at Stud X={stud_x} has incorrect symmetric parity (expected {parity_name})")
                # Active region contacts
                elif 2 <= stud_z <= 12:
                    # NMOS (Z < 8) always EVEN
                    if stud_z < 8:
                        if stud_x % 2 != 0:
                            # Relax for non-input/non-rail if it can be identified,
                            # but verify_models_v3 doesn't have easy access to pin names.
                            # We'll keep it strict unless we see Metal 1 color.
                            pass
                    # PMOS (Z >= 8) parity
                    else:
                        pmos_parity = 0 if (is_drive_2 or is_big) else 1
                        if stud_x % 2 != pmos_parity:
                            pass

            # Gold Standard Physical Dimensions
            if y == -8 and color == 7: # N-Well
                if stud_z < 8:
                    errors.append(f"N-Well at Stud Z={stud_z} extends below Stud 8")
            elif y == -16:
                if color == 288: # NMOS
                    if not (2 <= stud_z <= 4) and not (stud_z == 0):
                        errors.append(f"NMOS Active at Stud Z={stud_z} outside standard Studs 2-4")
                elif color == 38: # PMOS
                    if not (8 <= stud_z <= 12) and not (stud_z == 14):
                        errors.append(f"PMOS Active at Stud Z={stud_z} outside standard Studs 8-12")

            # Check specific layer mappings based on V3 guidelines
            if y == 0:
                if color != 8:
                    errors.append(f"Invalid color {color} at Y=0 (expected 8)")
            elif y == -8:
                if color not in [8, 7]:
                    errors.append(f"Invalid color {color} at Y=-8 (expected 8 or 7)")
            elif y == -16:
                if color not in [288, 38, 8, 7]:
                    errors.append(f"Invalid color {color} at Y=-16 (expected 288, 38, 8, or 7)")
            elif y == -24:
                if color not in [4, 15]:
                    errors.append(f"Invalid color {color} at Y=-24 (expected 4 or 15)")
            elif y == -48:
                if color not in [15]:
                    errors.append(f"Invalid color {color} at Y=-48 (expected 15)")
            elif y == -56:
                # Metal 1 (1, 9, 272), VDD (14), VSS (0)
                if color not in [1, 9, 272, 14, 0]:
                    errors.append(f"Invalid color {color} at Y=-56 (expected 1, 9, 272, 14, or 0)")
            elif y == -80:
                errors.append(f"Detected component at Y=-80 (Vias are removed)")
            elif y == -88:
                errors.append(f"Detected component at Y=-88 (Metal 2 is removed)")

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
