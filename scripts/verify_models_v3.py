import os
import re

def get_unified_parity(stud_x, is_big):
    """
    Unified parity rule for active and gate tracks (Z=2..12):
    - Small models (width <= 7): Always ODD (1).
    - Big models (> 7 studs): Symmetric parity - ODD if X < 8, EVEN if X >= 8.
    """
    if not is_big:
        return 1 # ODD
    return 1 if stud_x < 8 else 0 # ODD if < 8, EVEN if >= 8

def verify_ldr(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    errors = []
    has_substrate_low_v3 = False

    # Track which layers and colors we see
    found_colors = set()
    found_y_levels = set()
    found_round_bricks = False

    # Pre-scan for Metal 2 connections to identify pin types at coordinates
    pin_map = {} # (stud_x, stud_z) -> color
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
    w_studs = int(max_x // 20) + 1

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

            if "3062b.dat" in line:
                found_round_bricks = True

            # Gold Standard Parity Checks
            if (y == -48 and color == 15) or (y == -24 and color == 15): # Contacts
                pin_color = pin_map.get((stud_x, stud_z))

                # Check Track Alignment (Only EVEN tracks)
                if stud_z % 2 != 0:
                    errors.append(f"Contact at Stud Z={stud_z} is on an ODD track (expected EVEN)")

                if pin_color == 14: # VDD
                    if stud_z != 14:
                        errors.append(f"VDD contact at Stud Z={stud_z} (expected Track 14)")
                    if stud_x % 2 != 0:
                        errors.append(f"VDD contact at Stud X={stud_x} has ODD parity (expected EVEN)")
                elif pin_color == 0: # VSS
                    if stud_z != 0:
                        errors.append(f"VSS contact at Stud Z={stud_z} (expected Track 0)")
                    if stud_x % 2 == 0:
                        errors.append(f"VSS contact at Stud X={stud_x} has EVEN parity (expected ODD)")
                elif pin_color in [1, 9, 272]: # Signal (Internal, Input, Output)
                    if not (2 <= stud_z <= 12):
                        errors.append(f"Signal contact at Stud Z={stud_z} outside tracks 2-12")
                    expected_parity = get_unified_parity(stud_x, is_big)
                    if stud_x % 2 != expected_parity:
                        parity_name = "ODD" if expected_parity == 1 else "EVEN"
                        errors.append(f"Signal contact at Stud X={stud_x} has incorrect parity (expected {parity_name})")

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
            elif y == -64:
                # Metal 2 Connection Plates (1, 9, 272, 14, 0)
                if color not in [1, 9, 272, 14, 0]:
                    errors.append(f"Invalid color {color} at Y=-64 (expected 1, 9, 272, 14, or 0)")
                if "3070.dat" not in line:
                    errors.append(f"Invalid part at Y=-64 (expected 3070.dat 1x1 tile)")
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
