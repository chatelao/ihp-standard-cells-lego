import os
import re
import sys

# Constants based on MAPPING_RULEBOOK.md
UM_TO_LDU = 20 / 0.27
LDU_OFFSET = 10

def um_to_ldu_coord(um):
    return round(um * UM_TO_LDU)

def parse_lef_macros(lef_filepath):
    with open(lef_filepath, 'r') as f:
        content = f.read()

    macros = {}
    macro_blocks = re.finditer(r'(?<!PROPERTYDEFINITIONS\n  )MACRO\s+([\w\[\]<>]+)(.*?)END\s+\1', content, re.DOTALL)
    for block in macro_blocks:
        macro_name = block.group(1)
        body = block.group(2)

        size_match = re.search(r'SIZE\s+([\d\.]+)\s+BY\s+([\d\.]+)\s*;', body)
        width_um = float(size_match.group(1)) if size_match else 0

        pins = []
        pin_matches = re.finditer(r'PIN\s+([\w\[\]<>]+)(.*?)END\s+\1', body, re.DOTALL)
        for pin_match in pin_matches:
            pin_name = pin_match.group(1)
            pin_body = pin_match.group(2)
            rects = re.findall(r'RECT\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', pin_body)
            pins.append({'name': pin_name, 'rects': [[float(c) for c in r] for r in rects]})

        obs_rects = []
        obs_match = re.search(r'OBS\s+(.*?)END', body, re.DOTALL)
        if obs_match:
            obs_rects = re.findall(r'RECT\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)', obs_match.group(1))
            obs_rects = [[float(c) for c in r] for r in obs_rects]

        macros[macro_name] = {
            'width_um': width_um,
            'pins': pins,
            'obs': obs_rects
        }

    return macros

def get_expected_contacts(macro):
    width_ldu = round(macro['width_um'] * UM_TO_LDU / 20) * 20
    w_studs = width_ldu // 20
    d_studs = 15 # Fixed height

    expected = set() # Set of (x, z)

    all_rects = []
    for pin in macro['pins']:
        all_rects.extend(pin['rects'])
    all_rects.extend(macro['obs'])

    for r in all_rects:
        x1, y1, x2, y2 = r
        lx1, lx2 = um_to_ldu_coord(min(x1, x2)), um_to_ldu_coord(max(x1, x2))
        lz1, lz2 = um_to_ldu_coord(min(y1, y2)) + LDU_OFFSET, um_to_ldu_coord(max(y1, y2)) + LDU_OFFSET

        for sx in range(w_studs):
            cx = sx * 20 + 10
            if lx1 <= cx <= lx2:
                for sz in range(d_studs):
                    cz = sz * 20 + 10
                    if lz1 <= cz <= lz2:
                        # Apply Parity Rules
                        if sz % 2 == 0:
                            if sz in [0, 14]:
                                if sx % 2 == 0: # Rails are EVEN
                                    expected.add((sx, sz))
                            elif 2 <= sz <= 12:
                                if sx % 2 != 0: # Active/Input are ODD
                                    expected.add((sx, sz))
    return expected

def parse_md_contacts(md_filepath):
    with open(md_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Metal 1 section
    match = re.search(r'## Metal 1\n(?:GOLDEN STANDARD\n\n)?```\n(.*?)\n```', content, re.DOTALL)
    if not match:
        return set()

    grid_text = match.group(1)
    lines = grid_text.strip('\n').split('\n')
    if not lines: return set()

    scale_line = lines[0]
    width = len(scale_line[2:])
    grid_lines = lines[1:]

    contacts = set()
    # MD grid is High Z to Low Z (top to bottom)
    # Row index i corresponds to Z = (len(grid_lines) - 1 - i)
    for i, line in enumerate(grid_lines):
        z = len(grid_lines) - 1 - i
        chars = line[2:]
        for x, char in enumerate(chars):
            if char in 'iock&_': # Lowercase chars are contacts
                contacts.add((x, z))
    return contacts

def main():
    lef_file = 'specifications/sg13g2_stdcell.lef'
    design_dir = 'design'

    if not os.path.exists(lef_file):
        print(f"Error: LEF file not found: {lef_file}")
        sys.exit(1)

    macro_data = parse_lef_macros(lef_file)

    all_passed = True
    for filename in sorted(os.listdir(design_dir)):
        if filename.endswith('.md'):
            macro_name = filename[:-3]
            if macro_name not in macro_data:
                continue

            expected = get_expected_contacts(macro_data[macro_name])
            actual = parse_md_contacts(os.path.join(design_dir, filename))

            if expected != actual:
                print(f"FAIL: {macro_name}")
                missing = expected - actual
                extra = actual - expected

                if missing:
                    print(f"  Missing contacts (in LEF but not in MD): {sorted(list(missing))}")
                    # Breakdown by track
                    tracks = sorted(list(set(z for x, z in missing)))
                    for t in tracks:
                        count = len([x for x, z in missing if z == t])
                        print(f"    Track {t}: {count} missing")

                if extra:
                    print(f"  Extra contacts (in MD but not in LEF): {sorted(list(extra))}")
                    tracks = sorted(list(set(z for x, z in extra)))
                    for t in tracks:
                        count = len([x for x, z in extra if z == t])
                        print(f"    Track {t}: {count} extra")

                all_passed = False
            else:
                print(f"PASS: {macro_name} ({len(actual)} contacts)")

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
