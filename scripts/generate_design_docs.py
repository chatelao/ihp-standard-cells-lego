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
        if p['part'] == '3034.dat': pw, pd = 8, 2
        elif p['part'] == '3460.dat': pw, pd = 8, 1
        elif p['part'] == '3666.dat': pw, pd = 6, 1
        elif p['part'] == '3020.dat': pw, pd = 4, 2
        elif p['part'] == '3710.dat': pw, pd = 4, 1
        elif p['part'] == '3623.dat': pw, pd = 3, 1
        elif p['part'] == '3022.dat': pw, pd = 2, 2
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
    priority = {'+': 5, '-': 5, 'I': 4, 'O': 3, 'C': 2, 'S': 1, 'N': 1, 'n': 1, 'p': 1, 'G': 1, 'M': 1}

    for p in sorted(parts, key=lambda p: priority.get(color_map.get(p['color'], ' '), 0), reverse=False):
        if p['y'] in layer_y_list and p['part'] != '3062b.dat':
            # Get dimensions from part name
            pw, pd = 1, 1
            if p['part'] == '3034.dat': pw, pd = 8, 2
            elif p['part'] == '3460.dat': pw, pd = 8, 1
            elif p['part'] == '3666.dat': pw, pd = 6, 1
            elif p['part'] == '3020.dat': pw, pd = 4, 2
            elif p['part'] == '3710.dat': pw, pd = 4, 1
            elif p['part'] == '3623.dat': pw, pd = 3, 1
            elif p['part'] == '3022.dat': pw, pd = 2, 2
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
    # Vias: Y=-80 (Between Metal 1 and Metal 2)
    # Metal 2: Y=-88

    # If we are in Metal 1, check for Contact at Y=-48 (below)
    if layer_y_list[0] == -56:
        # Check for contact (below)
        has_contact = False
        for p in parts:
            if p['part'] == '3062b.dat' and p['y'] == -48:
                if abs(p['x'] - x) < 5 and abs(p['z'] - z) < 5:
                    has_contact = True
                    break
        if has_contact:
            alternatives = {'I': 'i', 'O': 'o', 'C': 'x', '+': '&', '-': '_'}
            return alternatives.get(char, 'x')

    # If we are in Metal 2, check for Via at Y=-80 (below)
    if layer_y_list[0] == -88:
        has_via = False
        for p in parts:
            if p['part'] == '3062b.dat' and p['y'] == -80:
                if abs(p['x'] - x) < 5 and abs(p['z'] - z) < 5:
                    has_via = True
                    break
        if has_via:
            return 'm'

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
    2: 'M',   # Metal 2 Green
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
    'x': 'Connection (upper side)',
    'O': 'Metal 1 Output',
    'o': 'Metal 1 Output',
    '+': 'VDD',
    '&': 'VDD',
    '-': 'VSS',
    '_': 'VSS',
    'M': 'Metal 2',
    'm': 'Connection (upper side)',
}

def generate_design_doc(cell_name, parts):
    width_studs, height_studs, min_x, min_z = get_dimensions(parts)

    doc = f"# Design Documentation for {cell_name}\n\n"

    layers = [
        ("Substrate", [0, -8]),
        ("Active", [-16]),
        ("Polysilicon", [-24]),
        ("Metal 1", [-56]),
        ("Metal 2", [-88])
    ]

    scale = "  " + "".join([str(i % 10) for i in range(width_studs)])

    for layer_name, y_list in layers:
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
            doc += "Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)\n"
        elif layer_name == "Metal 2":
            if 'm' in used_chars:
                doc += "Legend: M=Metal 2, m=Connection (upper side)\n"
            else:
                doc += "Legend: M=Metal 2\n"

        doc += "\n"

    return doc

def main():
    if not os.path.exists('design'):
        os.makedirs('design')

    for filename in os.listdir('models'):
        if filename.startswith('sg13g2_') and filename.endswith('.ldr'):
            cell_name = filename[:-4]
            filepath = os.path.join('models', filename)
            parts = parse_ldr_full(filepath)
            doc = generate_design_doc(cell_name, parts)

            output_path = os.path.join('design', f"{cell_name}.md")
            with open(output_path, 'w') as f:
                f.write(doc)
            print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
