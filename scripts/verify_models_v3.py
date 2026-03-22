import os
import re

def get_unified_parity(stud_x, is_big):
    if not is_big:
        return 1 # ODD
    return 1 if stud_x < 8 else 0 # ODD if < 8, EVEN if >= 8

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

    # Connectivity Matrix Verification (V4)
    # Ensure that contacts for a pin only connect to a single silicon blob (or expected blobs)
    # and that Obstructions do not connect to functional silicon.
    from generate_design_docs import find_blobs, get_part_studs, parse_ldr_full

    parts = parse_ldr_full(filepath)
    nmos_blobs = find_blobs(parts, [-16], [288])
    pmos_blobs = find_blobs(parts, [-16], [38])
    poly_blobs = find_blobs(parts, [-24], [4])
    silicon_blobs = nmos_blobs + pmos_blobs + poly_blobs

    metal_blobs = find_blobs(parts, [-56, -64], [14, 0, 9, 272, 1])

    contacts = [p for p in parts if p['part'] == '3062b.dat' and p['y'] == -48]
    for c in contacts:
        c_stud = (int(round((c['x'] - 10) / 20)), int(round((c['z'] - 10) / 20)))
        connected_silicon = [b for b in silicon_blobs if c_stud in b['studs']]
        connected_metal = [b for b in metal_blobs if c_stud in b['studs']]

        for s in connected_silicon:
            # V4 Strict Connectivity:
            # 1. Poly connection: Metal -> Contact Brick (Y=-48) -> Poly (Y=-24)
            # 2. Active connection: Metal -> Contact Brick (Y=-48) -> Round Plate (Y=-24) -> Active (Y=-16)

            is_poly_blob = s['color'] == 4
            has_round_plate = any(p['part'] == '6141.dat' and p['y'] == -24 and (int(round((p['x']-10)/20)), int(round((p['z']-10)/20))) == c_stud for p in parts)

            if is_poly_blob:
                if has_round_plate:
                    errors.append(f"Contact at {c_stud} for Poly blob {s.get('name', 'unnamed')} unexpectedly has a round plate at Y=-24")
            else:
                if not has_round_plate:
                    errors.append(f"Contact at {c_stud} for Active blob {s.get('name', 'unnamed')} missing required round plate at Y=-24")

        for m in connected_metal:
            m_color = m['color']
            # color 1 is internal/obstruction.
            if m_color == 1:
                # If it's an obstruction contact (Metal 1 color 1), it should NOT hit functional silicon
                if connected_silicon:
                    # Check if any part of the metal blob has a label starting with "Pin"
                    # If it's truly an obstruction, it shouldn't.
                    is_real_pin = any(p['label'] and p['label'].startswith("Pin ") for p in m['parts'])
                    if not is_real_pin:
                        errors.append(f"Obstruction contact at {c_stud} unexpectedly connects to functional silicon")

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
