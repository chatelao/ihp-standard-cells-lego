import os
import re

def get_dimensions(parts):
    if not parts:
        return 0, 0, 0, 0

    min_x, max_x = float('inf'), float('-inf')
    min_z, max_z = float('inf'), float('-inf')

    for p in parts:
        # Determine part size in studs (Standard Width x Depth)
        pw, pd = 1, 1
        if p['part'] == '91405.dat': pw, pd = 16, 16
        elif p['part'] == '92438.dat': pw, pd = 16, 8
        elif p['part'] == '3027.dat': pw, pd = 16, 6
        elif p['part'] == '3456.dat': pw, pd = 14, 6
        elif p['part'] == '3028.dat': pw, pd = 12, 6
        elif p['part'] == '3033.dat': pw, pd = 10, 6
        elif p['part'] == '3029.dat': pw, pd = 12, 4
        elif p['part'] == '3036.dat': pw, pd = 8, 6
        elif p['part'] == '3030.dat': pw, pd = 10, 4
        elif p['part'] == '3958.dat': pw, pd = 6, 6
        elif p['part'] == '4282.dat': pw, pd = 16, 2
        elif p['part'] == '3035.dat': pw, pd = 8, 4
        elif p['part'] == '2445.dat': pw, pd = 12, 2
        elif p['part'] == '3032.dat': pw, pd = 6, 4
        elif p['part'] == '3832.dat': pw, pd = 10, 2
        elif p['part'] == '3034.dat': pw, pd = 8, 2
        elif p['part'] == '3031.dat': pw, pd = 4, 4
        elif p['part'] == '60479.dat': pw, pd = 12, 1
        elif p['part'] == '3795.dat': pw, pd = 6, 2
        elif p['part'] == '4477.dat': pw, pd = 10, 1
        elif p['part'] == '3460.dat': pw, pd = 8, 1
        elif p['part'] == '3020.dat': pw, pd = 4, 2
        elif p['part'] == '3666.dat': pw, pd = 6, 1
        elif p['part'] == '3021.dat': pw, pd = 3, 2
        elif p['part'] == '3710.dat': pw, pd = 4, 1
        elif p['part'] == '3022.dat': pw, pd = 2, 2
        elif p['part'] == '3623.dat': pw, pd = 3, 1
        elif p['part'] == '3023.dat': pw, pd = 2, 1
        elif p['part'] == '3024.dat': pw, pd = 1, 1
        elif p['part'] == '6141.dat': pw, pd = 1, 1
        elif p['part'] == '3062b.dat': pw, pd = 1, 1

        # Check if rotated (simplified check for the matrix 0 0 1 0 1 0 -1 0 0)
        is_rotated = p['rot'][0] == 0
        if is_rotated:
            pw, pd = pd, pw

        half_w_ldu = (pw * 20) / 2
        half_d_ldu = (pd * 20) / 2

        min_x = min(min_x, p['x'] - half_w_ldu)
        max_x = max(max_x, p['x'] + half_w_ldu)
        min_z = min(min_z, p['z'] - half_d_ldu)
        max_z = max(max_z, p['z'] + half_d_ldu)

    # Grid is 20 LDU.
    grid_min_x = int(round(min_x / 20)) * 20
    grid_max_x = int(round(max_x / 20)) * 20
    grid_min_z = int(round(min_z / 20)) * 20
    grid_max_z = int(round(max_z / 20)) * 20

    # For very narrow cells (like fill_1), ensure we have at least one stud width.
    if grid_max_x <= grid_min_x:
        grid_max_x = grid_min_x + 20

    width_studs = (grid_max_x - grid_min_x) // 20
    height_studs = (grid_max_z - grid_min_z) // 20

    return width_studs, height_studs, grid_min_x, grid_min_z

def parse_ldr_full(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    parts = []
    for line in lines:
        line = line.strip()
        if line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                color = int(tokens[1])
                x = float(tokens[2])
                y = float(tokens[3])
                z = float(tokens[4])
                # Rot matrix
                rot = [float(t) for t in tokens[5:14]]
                part = tokens[14]
                parts.append({'color': color, 'x': x, 'y': y, 'z': z, 'rot': rot, 'part': part})
    return parts

def get_char_for_stud(parts, x, z, layer_y_list, color_map, connection_map):
    # Base layer character
    char = ' '

    # Check plates
    # Sort parts by some order to ensure deterministic behavior if multiple parts overlap
    # Metal 1 special handling: VSS/VDD/Inputs/Outputs should have priority over Connection
    # We sort by priority ascending so that higher priority characters are assigned last and "win".
    priority = {'+': 5, '-': 5, 'I': 4, 'O': 3, 'C': 2, 'S': 1, 'N': 1, 'n': 1, 'p': 1, 'G': 1}

    for p in sorted(parts, key=lambda p: priority.get(color_map.get(p['color'], ' '), 0), reverse=False):
        if p['y'] in layer_y_list and p['part'] != '3062b.dat':
            # Get dimensions from part name
            pw, pd = 1, 1
            if p['part'] == '91405.dat': pw, pd = 16, 16
            elif p['part'] == '92438.dat': pw, pd = 16, 8
            elif p['part'] == '3027.dat': pw, pd = 16, 6
            elif p['part'] == '3456.dat': pw, pd = 14, 6
            elif p['part'] == '3028.dat': pw, pd = 12, 6
            elif p['part'] == '3033.dat': pw, pd = 10, 6
            elif p['part'] == '3029.dat': pw, pd = 12, 4
            elif p['part'] == '3036.dat': pw, pd = 8, 6
            elif p['part'] == '3030.dat': pw, pd = 10, 4
            elif p['part'] == '3958.dat': pw, pd = 6, 6
            elif p['part'] == '4282.dat': pw, pd = 16, 2
            elif p['part'] == '3035.dat': pw, pd = 8, 4
            elif p['part'] == '2445.dat': pw, pd = 12, 2
            elif p['part'] == '3032.dat': pw, pd = 6, 4
            elif p['part'] == '3832.dat': pw, pd = 10, 2
            elif p['part'] == '3034.dat': pw, pd = 8, 2
            elif p['part'] == '3031.dat': pw, pd = 4, 4
            elif p['part'] == '60479.dat': pw, pd = 12, 1
            elif p['part'] == '3795.dat': pw, pd = 6, 2
            elif p['part'] == '4477.dat': pw, pd = 10, 1
            elif p['part'] == '3460.dat': pw, pd = 8, 1
            elif p['part'] == '3020.dat': pw, pd = 4, 2
            elif p['part'] == '3666.dat': pw, pd = 6, 1
            elif p['part'] == '3021.dat': pw, pd = 3, 2
            elif p['part'] == '3710.dat': pw, pd = 4, 1
            elif p['part'] == '3022.dat': pw, pd = 2, 2
            elif p['part'] == '3623.dat': pw, pd = 3, 1
            elif p['part'] == '3023.dat': pw, pd = 2, 1
            elif p['part'] == '3024.dat': pw, pd = 1, 1
            elif p['part'] == '6141.dat': pw, pd = 1, 1

            # Check if rotated (simplified check for the matrix 0 0 1 0 1 0 -1 0 0)
            is_rotated = p['rot'][0] == 0
            if is_rotated:
                pw, pd = pd, pw

            # Boundary
            half_w = (pw * 20) / 2
            half_d = (pd * 20) / 2
            if (p['x'] - half_w <= x <= p['x'] + half_w) and (p['z'] - half_d <= z <= p['z'] + half_d):
                char = color_map.get(p['color'], char)

    # Connections
    # "X for connections between layer on the lower side and x on the upper side"
    # Mapping provided by user:
    # Substrate: Y=0, -8
    # Active: Y=-16
    # Poly: Y=-24
    # Contacts: Y=-48 (Between Active/Poly and Metal 1)
    # Metal 1: Y=-56

    # If we are in Metal 1, check for Contact at Y=-48 (below) or Metal 2 Connection at Y=-64 (above)
    if layer_y_list[0] == -56:
        # Check for contact (below)
        has_contact_below = False
        for p in parts:
            if p['part'] == '3062b.dat' and p['y'] == -48:
                if abs(p['x'] - x) < 5 and abs(p['z'] - z) < 5:
                    has_contact_below = True
                    break

        # Check for Metal 2 connection plate (above)
        has_plate_above = False
        for p in parts:
            if p['part'] == '3024.dat' and p['y'] == -64:
                if abs(p['x'] - x) < 5 and abs(p['z'] - z) < 5:
                    has_plate_above = True
                    break

        if has_contact_below or has_plate_above:
            alternatives = {'I': 'i', 'O': 'o', 'C': 'c', '+': '&', '-': '_'}
            return alternatives.get(char, 'c')

    return char

COLOR_MAP = {
    8: 'S',   # Substrate Dark Gray
    7: 'N',   # N-Well Light Gray
    288: 'n', # NMOS Dark Green
    38: 'p',  # PMOS Dark Orange
    4: 'G',   # Polysilicon Red
    9: 'I',   # Metal 1 Input Light Blue
    1: 'C',   # Metal 1 Connection Blue
    272: 'O', # Metal 1 Output Dark Blue
    14: '+',  # VDD Yellow
    0: '-',   # VSS Black
}

LEGEND_DESC = {
    'S': 'Substrate',
    'N': 'N-Well',
    'n': 'NMOS Active',
    'p': 'PMOS Active',
    'G': 'Polysilicon',
    'I': 'Metal 1 Input',
    'i': 'Metal 1 Input',
    'C': 'Metal 1 Connection',
    'c': 'Connection (upper side)',
    'O': 'Metal 1 Output',
    'o': 'Metal 1 Output',
    '+': 'VDD',
    '&': 'VDD',
    '-': 'VSS',
    '_': 'VSS',
}

def extract_golden_sections(design_dir):
    golden_sections = {}

    # First, try to extract from GOLDEN_STANDARD.md to ensure no loss
    gs_path = 'specifications/GOLDEN_STANDARD.md'
    if os.path.exists(gs_path):
        with open(gs_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for the section "## 7. Golden Design Examples"
        header = "## 7. Golden Design Examples"
        if header in content:
            examples_part = content.split(header)[1]
            # Examples are in format "### {cell} - {layer}\nGOLDEN STANDARD\n\n```...```"
            # Or similar. Let's use a regex to be more robust.
            # Example: ### sg13g2_buf_1 - Active
            pattern = r'### (sg13g2_[a-z0-9_]+) - ([A-Za-z0-9 ]+)\n(.*?)(?=\n### |\n## |$)'
            matches = re.findall(pattern, examples_part, re.DOTALL)
            for cell_name, layer_name, text in matches:
                # Reconstruct the section format expected by the rest of the script
                # The text usually starts with GOLDEN STANDARD and then the code block
                full_text = f"## {layer_name}\n{text.strip()}"
                golden_sections[(cell_name, layer_name)] = full_text

    if not os.path.exists(design_dir):
        return golden_sections

    for filename in os.listdir(design_dir):
        if filename.endswith('.md'):
            cell_name = filename[:-3]
            filepath = os.path.join(design_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split by "## " to get sections.
            sections = content.split('\n## ')
            for section in sections[1:]:
                if 'GOLDEN STANDARD' in section:
                    lines = section.split('\n')
                    layer_name = lines[0].strip()
                    # Store the whole section including the header we'll use it verbatim
                    # If it was already in GOLDEN_STANDARD.md, this will overwrite it with potentially newer content from the design file
                    golden_sections[(cell_name, layer_name)] = '## ' + section.strip()
    return golden_sections

def update_golden_standard_file(all_golden):
    filepath = 'specifications/GOLDEN_STANDARD.md'
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    header = "## 7. Golden Design Examples"

    if all_golden:
        new_text = header + "\n"
        for (cell, layer), text in sorted(all_golden.items()):
            new_text += f"### {cell} - {layer}\n"
            content_lines = text.split('\n')
            new_text += '\n'.join(content_lines[1:]).strip() + "\n\n"
        new_text = new_text.strip() + "\n"
    else:
        new_text = ""

    if header in content:
        # Keep everything before the header
        before = content.split(header)[0]
        # Check if there is anything after section 7 (we'll assume anything starting with ## [8-9] or higher)
        # For simplicity in this project, we assume 7 is the last one or we manage it carefully.
        # Let's try to find if there's a "## 8." or similar.
        after_match = re.search(r'\n## [8-9]\.', content.split(header)[1])
        if after_match:
            after = content.split(header)[1][after_match.start():]
            content = before + new_text + after
        else:
            content = before + new_text
    elif new_text:
        content = content.strip() + "\n\n" + new_text

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_design_doc(cell_name, parts, golden_sections):
    width_studs, height_studs, min_x, min_z = get_dimensions(parts)

    doc = f"# Design Documentation for {cell_name}\n\n"

    layers = [
        ("Substrate", [0, -8]),
        ("Active", [-16]),
        ("Polysilicon", [-24]),
        ("Metal 1", [-56])
    ]

    scale = "  " + "".join([str(i % 10) for i in range(width_studs)])

    for layer_name, y_list in layers:
        if (cell_name, layer_name) in golden_sections:
            doc += golden_sections[(cell_name, layer_name)] + "\n\n"
            continue

        doc += f"## {layer_name}\n"
        doc += "```\n"
        doc += scale + "\n"

        used_chars = set()
        layer_lines = []
        # In ASCII art, top row is smallest Z?
        # LEF Y is LEGO Z.
        # VDD is at high Z, VSS at low Z.
        # Let's print from high Z to low Z so VDD is on top.
        for z_idx in range(height_studs - 1, -1, -1):
            line = f"{z_idx % 10} "
            for x_idx in range(width_studs):
                sx = min_x + x_idx * 20 + 10
                sz = min_z + z_idx * 20 + 10
                char = get_char_for_stud(parts, sx, sz, y_list, COLOR_MAP, {})
                line += char
                if char != ' ':
                    used_chars.add(char)
            layer_lines.append(line.rstrip())

        doc += "\n".join(layer_lines) + "\n"
        doc += "```\n"

        if layer_name == "Substrate":
            doc += "Legend: N=N-Well, S=Substrate\n"
        elif layer_name == "Active":
            legend_parts = []
            if 'n' in used_chars: legend_parts.append("n=NMOS Active")
            if 'p' in used_chars: legend_parts.append("p=PMOS Active")
            if 'S' in used_chars: legend_parts.append("S=Substrate fill (P)")
            if 'N' in used_chars: legend_parts.append("N=Substrate fill (N)")
            doc += f"Legend: {', '.join(legend_parts)}\n"
        elif layer_name == "Polysilicon":
            doc += "Legend: G=Polysilicon\n"
        elif layer_name == "Metal 1":
            doc += "Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)\n"

        doc += "\n"

    return doc

def main():
    if not os.path.exists('design'):
        os.makedirs('design')

    golden_sections = extract_golden_sections('design')
    golden_sections.update(extract_golden_sections('handmade'))

    for filename in os.listdir('models'):
        if filename.startswith('sg13g2_') and filename.endswith('.ldr'):
            cell_name = filename[:-4]
            filepath = os.path.join('models', filename)
            parts = parse_ldr_full(filepath)
            doc = generate_design_doc(cell_name, parts, golden_sections)

            output_path = os.path.join('design', f"{cell_name}.md")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(doc)
            print(f"Generated {output_path}")

    update_golden_standard_file(golden_sections)

if __name__ == "__main__":
    main()
