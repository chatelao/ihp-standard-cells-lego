import os
import re
import sys

# Scaling factor: 1 LDU = 0.012 um
LDU_TO_UM = 0.012

def parse_lef_rects(lef_filepath):
    with open(lef_filepath, 'r') as f:
        content = f.read()

    macros = {}
    macro_blocks = re.finditer(r'MACRO\s+([\w\[\]<>]+)(.*?)END\s+\1', content, re.DOTALL)
    for block in macro_blocks:
        macro_name = block.group(1)
        body = block.group(2)

        pins = {}
        pin_matches = re.finditer(r'PIN\s+([\w\[\]<>]+)(.*?)END\s+\1', body, re.DOTALL)
        for pin_match in pin_matches:
            pin_name = pin_match.group(1)
            pin_body = pin_match.group(2)
            rects = re.findall(r'RECT\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', pin_body)
            pins[pin_name] = [[float(c) for c in r] for r in rects]

        macros[macro_name] = pins

    return macros

def get_ldr_pins_spatial(ldr_filepath):
    with open(ldr_filepath, 'r') as f:
        lines = f.readlines()

    pins_found = {}
    current_pin = None

    for line in lines:
        # Match pin comment
        # Support: 0 // Pin A, 0 // Pin: A, 0 // A Rail, 0 // Pin A[0]
        pin_match = re.search(r'0\s+//\s+(?:Pin\s*(?::)?\s*([\w\[\]<>]+)|([\w\[\]<>]+)\s+Rail)', line, re.IGNORECASE)
        if pin_match:
            new_pin = pin_match.group(1) or pin_match.group(2)
            current_pin = new_pin.strip()
            if current_pin not in pins_found:
                pins_found[current_pin] = []
            continue

        # Reset pin tracking if we encounter other comment headers
        if line.startswith('0 //'):
            current_pin = None
            continue

        # Match LDraw part line: 1 <color> <x> <y> <z> ...
        part_match = re.match(r'^1\s+\d+\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', line)
        if part_match and current_pin:
            x_ldu = float(part_match.group(1))
            z_ldu = float(part_match.group(3))
            pins_found[current_pin].append((x_ldu * LDU_TO_UM, z_ldu * LDU_TO_UM))

    return pins_found

def is_point_in_rects(x, y, rects, tolerance=0.15):
    for r in rects:
        x1, y1, x2, y2 = r
        # Standardize rect bounds
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        if (min_x - tolerance <= x <= max_x + tolerance) and \
           (min_y - tolerance <= y <= max_y + tolerance):
            return True
    return False

def main():
    lef_file = sys.argv[1] if len(sys.argv) > 1 else 'specifications/sg13g2_stdcell.lef'
    models_dir = sys.argv[2] if len(sys.argv) > 2 else 'models'

    if not os.path.exists(lef_file):
        print(f"Error: LEF file not found: {lef_file}")
        exit(1)
    if not os.path.isdir(models_dir):
        print(f"Error: models directory not found: {models_dir}")
        exit(1)

    macro_data = parse_lef_rects(lef_file)

    all_passed = True
    for filename in os.listdir(models_dir):
        if filename.endswith('.ldr'):
            macro_name = filename[:-4]
            if macro_name not in macro_data:
                continue

            ldr_pins = get_ldr_pins_spatial(os.path.join(models_dir, filename))
            expected_pins = macro_data[macro_name]

            macro_failed = False
            for pin_name, coords_list in ldr_pins.items():
                if pin_name not in expected_pins:
                    continue

                rects = expected_pins[pin_name]
                for x, y in coords_list:
                    if not is_point_in_rects(x, y, rects):
                        print(f"FAIL: {filename} - Pin {pin_name} at ({x:.3f}, {y:.3f}) um is outside LEF RECTs")
                        macro_failed = True
                        all_passed = False
                        break

            if not macro_failed:
                print(f"PASS: {filename} - All mapped pin components are within LEF geometric bounds")

    if not all_passed:
        # Note: Significant deviations often occur due to LEGO stud quantization (0.48um).
        exit(1)

if __name__ == "__main__":
    main()
