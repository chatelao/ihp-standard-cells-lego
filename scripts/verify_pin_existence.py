import os
import re
import sys

def parse_lef_pins(lef_filepath):
    with open(lef_filepath, 'r') as f:
        content = f.read()

    macros = {}
    # Match MACRO ... END MACRO blocks
    # Supporting names with alphanumeric, underscores, and potentially brackets
    macro_blocks = re.finditer(r'MACRO\s+([\w\[\]<>]+)(.*?)END\s+\1', content, re.DOTALL)
    for block in macro_blocks:
        macro_name = block.group(1)
        body = block.group(2)

        # Match PIN ... END PIN blocks within the macro
        pins = re.findall(r'PIN\s+([\w\[\]<>]+)', body)
        macros[macro_name] = set(pins)

    return macros

def verify_pins_in_ldr(ldr_filepath, expected_pins):
    with open(ldr_filepath, 'r') as f:
        content = f.read()

    missing_pins = []
    for pin in expected_pins:
        # Check for "0 // Pin <pin_name>", "0 // Pin: <pin_name>", or "<pin_name> Rail"
        # Escaping pin name for regex (important for brackets like A[0])
        escaped_pin = re.escape(pin)
        pattern = rf'0\s+//\s+(Pin\s+({escaped_pin}\b|:\s+{escaped_pin}\b)|{escaped_pin}\s+Rail)'
        if not re.search(pattern, content, re.IGNORECASE):
            missing_pins.append(pin)

    return missing_pins

def main():
    lef_file = sys.argv[1] if len(sys.argv) > 1 else 'specifications/sg13g2_stdcell.lef'
    models_dir = sys.argv[2] if len(sys.argv) > 2 else 'models'

    if not os.path.exists(lef_file):
        print(f"Error: LEF file not found: {lef_file}")
        exit(1)
    if not os.path.isdir(models_dir):
        print(f"Error: models directory not found: {models_dir}")
        exit(1)

    macro_pins = parse_lef_pins(lef_file)

    all_passed = True
    for filename in os.listdir(models_dir):
        if filename.endswith('.ldr'):
            macro_name = filename[:-4]
            if macro_name in macro_pins:
                expected = macro_pins[macro_name]
                missing = verify_pins_in_ldr(os.path.join(models_dir, filename), expected)

                if missing:
                    print(f"FAIL: {filename} is missing pins: {', '.join(missing)}")
                    all_passed = False
                else:
                    print(f"PASS: {filename} contains all {len(expected)} expected pins")
            else:
                # Some .ldr files might not have a direct LEF macro (e.g. sub-parts)
                # but for standard cells, they should.
                pass

    if not all_passed:
        exit(1)

if __name__ == "__main__":
    main()
