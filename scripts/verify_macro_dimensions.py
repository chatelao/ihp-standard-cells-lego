import os
import re
import sys

# Constants for LDU to um conversion
LDU_PER_STUD = 20
UM_PER_STUD = 0.27
LDU_TO_UM = UM_PER_STUD / LDU_PER_STUD

def parse_lef_sizes(lef_filepath):
    with open(lef_filepath, 'r') as f:
        content = f.read()

    macros = {}
    macro_blocks = re.finditer(r'MACRO\s+([\w\[\]<>]+)(.*?)END\s+\1', content, re.DOTALL)
    for block in macro_blocks:
        macro_name = block.group(1)
        body = block.group(2)

        size_match = re.search(r'SIZE\s+([\d.-]+)\s+BY\s+([\d.-]+)', body)
        if size_match:
            width = float(size_match.group(1))
            height = float(size_match.group(2))
            macros[macro_name] = (width, height)

    return macros

def get_ldr_substrate_size(ldr_filepath):
    with open(ldr_filepath, 'r') as f:
        lines = f.readlines()

    # We assume the substrate is defined at Y=0 or Y=-8 using color 8 or 7.
    # We look for the maximum bounding box of these plates.
    min_x, max_x = float('inf'), float('-inf')
    min_z, max_z = float('inf'), float('-inf')

    found_substrate = False

    for line in lines:
        # Match LDraw part line: 1 <color> <x> <y> <z> <m0> <m1> <m2> <m3> <m4> <m5> <m6> <m7> <m8> <part>
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+\s+){9}([\w.-]+)', line)
        if match:
            color = int(match.group(1))
            x = float(match.group(2))
            y = float(match.group(3))
            z = float(match.group(4))
            part = match.group(6)

            # Check if it's a substrate component (Dark Gray 8 or Light Gray 7 at Y=0, -8)
            if color in [8, 7] and y in [0, -8]:
                found_substrate = True

                # Determine part size in studs (Standard Width x Depth)
                # These match PLATES in lef_to_ldr.py
                pw, pd = 0, 0
                if '91405' in part: pw, pd = 16, 16
                elif '92438' in part: pw, pd = 16, 8
                elif '3027' in part: pw, pd = 16, 6
                elif '3456' in part: pw, pd = 14, 6
                elif '3028' in part: pw, pd = 12, 6
                elif '3033' in part: pw, pd = 10, 6
                elif '3029' in part: pw, pd = 12, 4
                elif '3036' in part: pw, pd = 8, 6
                elif '3030' in part: pw, pd = 10, 4
                elif '3958' in part: pw, pd = 6, 6
                elif '4282' in part: pw, pd = 16, 2
                elif '3035' in part: pw, pd = 8, 4
                elif '2445' in part: pw, pd = 12, 2
                elif '3032' in part: pw, pd = 6, 4
                elif '3832' in part: pw, pd = 10, 2
                elif '3034' in part: pw, pd = 8, 2
                elif '3031' in part: pw, pd = 4, 4
                elif '60479' in part: pw, pd = 12, 1
                elif '3795' in part: pw, pd = 6, 2
                elif '4477' in part: pw, pd = 10, 1
                elif '3460' in part: pw, pd = 8, 1
                elif '3020' in part: pw, pd = 4, 2
                elif '3666' in part: pw, pd = 6, 1
                elif '3021' in part: pw, pd = 3, 2
                elif '3710' in part: pw, pd = 4, 1
                elif '3022' in part: pw, pd = 2, 2
                elif '3623' in part: pw, pd = 3, 1
                elif '3023' in part: pw, pd = 2, 1
                elif '3024' in part: pw, pd = 1, 1
                elif '3070' in part: pw, pd = 1, 1
                else: continue # Unknown part size

                # Check rotation matrix for orientation
                # Standard (Identity): 1 0 0 0 1 0 0 0 1 -> X=Width, Z=Depth
                # Rotated (Z-align): 0 0 1 0 1 0 -1 0 0 -> X=Depth, Z=Width
                parts = line.split()
                # Type 1 line: 1 <color> <x> <y> <z> <m0> <m1> <m2> <m3> <m4> <m5> <m6> <m7> <m8> <part>
                # index: 0    1      2   3   4    5    6    7    8    9   10   11   12   13   14
                m0 = float(parts[5])
                m2 = float(parts[7])
                if abs(m0) < 0.1 and abs(m2) > 0.9: # Rotated (Z-aligned)
                    pw, pd = pd, pw

                half_w_ldu = (pw * LDU_PER_STUD) / 2
                half_d_ldu = (pd * LDU_PER_STUD) / 2

                min_x = min(min_x, x - half_w_ldu)
                max_x = max(max_x, x + half_w_ldu)
                min_z = min(min_z, z - half_d_ldu)
                max_z = max(max_z, z + half_d_ldu)

    if not found_substrate:
        return None

    return (max_x - min_x) * LDU_TO_UM, (max_z - min_z) * LDU_TO_UM

def main():
    lef_file = sys.argv[1] if len(sys.argv) > 1 else 'specifications/sg13g2_stdcell.lef'
    models_dir = sys.argv[2] if len(sys.argv) > 2 else 'models'

    macro_sizes = parse_lef_sizes(lef_file)

    all_passed = True
    for filename in os.listdir(models_dir):
        if filename.endswith('.ldr'):
            macro_name = filename[:-4]
            if macro_name not in macro_sizes:
                continue

            ldr_size = get_ldr_substrate_size(os.path.join(models_dir, filename))
            if ldr_size is None:
                print(f"FAIL: {filename} - No substrate detected")
                all_passed = False
                continue

            exp_w, exp_h = macro_sizes[macro_name]
            ldr_w, ldr_h = ldr_size

            # Guidance: 3.78 um LEF height maps to 14 studs between rails.
            # Total cell height is 15 studs = 4.05 um.
            target_h = 4.05 if abs(exp_h - 3.78) < 0.001 else exp_h

            # Allow some tolerance for rounding/quantization (0.15 um)
            # 0.252 um / 2 = 0.126 um max error per side
            if abs(exp_w - ldr_w) > 0.15 or abs(target_h - ldr_h) > 0.15:
                print(f"FAIL: {filename} - Size mismatch. LEF: {exp_w:.3f}x{exp_h:.3f} (target {exp_w:.3f}x{target_h:.3f}), LDR: {ldr_w:.3f}x{ldr_h:.3f}")
                all_passed = False
            else:
                print(f"PASS: {filename} - Size matches LEF definition (quantized)")

    if not all_passed:
        exit(1)

if __name__ == "__main__":
    main()
