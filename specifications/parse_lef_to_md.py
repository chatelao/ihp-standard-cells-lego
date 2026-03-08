import re
import sys

def parse_lef(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    macros = []
    # Match MACRO blocks, avoiding PROPERTYDEFINITIONS
    macro_matches = re.finditer(r'(?<!PROPERTYDEFINITIONS\n  )MACRO\s+(\w+)(.*?)END\s+\1', content, re.DOTALL)

    for match in macro_matches:
        macro_name = match.group(1)
        body = match.group(2)

        macro_data = {
            'name': macro_name,
            'size': None,
            'pins': [],
            'obs': []
        }

        # Size
        size_match = re.search(r'SIZE\s+([\d\.]+)\s+BY\s+([\d\.]+)\s*;', body)
        if size_match:
            macro_data['size'] = (float(size_match.group(1)), float(size_match.group(2)))

        # Pins
        pin_matches = re.finditer(r'PIN\s+(\w+)(.*?)END\s+\1', body, re.DOTALL)
        for pin_match in pin_matches:
            pin_name = pin_match.group(1)
            pin_body = pin_match.group(2)

            pin_data = {
                'name': pin_name,
                'layers': []
            }

            # Ports/Layers inside Pins
            port_matches = re.finditer(r'PORT\s+(.*?)END', pin_body, re.DOTALL)
            for port_match in port_matches:
                port_body = port_match.group(1)
                layer_matches = re.finditer(r'LAYER\s+(\w+)\s*;(.*?)(?=LAYER|END|$)', port_body, re.DOTALL)
                for layer_match in layer_matches:
                    layer_name = layer_match.group(1)
                    rect_content = layer_match.group(2)
                    rects = re.findall(r'RECT\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s*;', rect_content)
                    pin_data['layers'].append({
                        'name': layer_name,
                        'rects': [(float(r[0]), float(r[1]), float(r[2]), float(r[3])) for r in rects]
                    })
            macro_data['pins'].append(pin_data)

        # Obstructions (OBS)
        obs_match = re.search(r'OBS\s+(.*?)END', body, re.DOTALL)
        if obs_match:
            obs_body = obs_match.group(1)
            layer_matches = re.finditer(r'LAYER\s+(\w+)\s*;(.*?)(?=LAYER|$)', obs_body, re.DOTALL)
            for layer_match in layer_matches:
                layer_name = layer_match.group(1)
                rect_content = layer_match.group(2)
                rects = re.findall(r'RECT\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s*;', rect_content)
                macro_data['obs'].append({
                    'name': layer_name,
                    'rects': [(float(r[0]), float(r[1]), float(r[2]), float(r[3])) for r in rects]
                })

        macros.append(macro_data)

    return macros

def generate_md(macros):
    md = "# SG13G2 Standard Cell Details\n\n"
    md += "This document provides details for each standard cell, including its size, pins, and obstructions.\n\n"

    for m in macros:
        md += f"## {m['name']}\n"
        if m['size']:
            md += f"- **Size:** {m['size'][0]} µm x {m['size'][1]} µm\n"

        if m['pins']:
            md += "### Pins\n"
            md += "| Pin Name | Layer | Rectangles (x1, y1, x2, y2) |\n"
            md += "|----------|-------|-----------------------------|\n"
            for pin in m['pins']:
                for layer in pin['layers']:
                    rect_str = "<br>".join([f"({r[0]}, {r[1]}, {r[2]}, {r[3]})" for r in layer['rects']])
                    md += f"| {pin['name']} | {layer['name']} | {rect_str} |\n"

        if m['obs']:
            md += "### Obstructions\n"
            md += "| Layer | Rectangles (x1, y1, x2, y2) |\n"
            md += "|-------|-----------------------------|\n"
            for obs in m['obs']:
                rect_str = "<br>".join([f"({r[0]}, {r[1]}, {r[2]}, {r[3]})" for r in obs['rects']])
                md += f"| {obs['name']} | {rect_str} |\n"

        md += "\n"

    return md

if __name__ == "__main__":
    lef_file = "sg13g2_stdcell.lef"
    output_file = "sg13g2_stdcell_details.md"

    print(f"Parsing {lef_file}...")
    macros = parse_lef(lef_file)
    print(f"Found {len(macros)} macros.")

    print(f"Generating {output_file}...")
    md_content = generate_md(macros)

    with open(output_file, 'w') as f:
        f.write(md_content)

    print("Done.")
