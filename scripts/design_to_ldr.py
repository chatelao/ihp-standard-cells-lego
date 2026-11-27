import argparse
import math
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from cif_to_ldr import is_stud_occupied_geom, parse_cif
from lego_utils import (
    COLOR_ACTIVE_NMOS,
    COLOR_ACTIVE_PMOS,
    COLOR_CONTACT,
    COLOR_DIELECTRIC,
    COLOR_METAL1_INPUT,
    COLOR_METAL1_INTERNAL,
    COLOR_METAL1_OUTPUT,
    COLOR_METAL2,
    COLOR_NWELL,
    COLOR_POLY,
    COLOR_SUBSTRATE,
    COLOR_VDD,
    COLOR_VSS,
    ROUND_BRICK,
    ROUND_PLATE,
    TILE_1X1,
    Y_ACTIVE,
    Y_CONTACT,
    Y_METAL1,
    Y_METAL2,
    Y_METAL2_PLATE,
    Y_METAL2_TILE,
    Y_POLY,
    compute_dielectric_supports,
    emit_chunked_steps,
    get_best_plates_multi,
    tile_substrate_high_with_snapping,
    tile_substrate_low,
)

COLOR_MAP_REV = {
    "S": COLOR_SUBSTRATE,
    "N": COLOR_NWELL,
    "n": COLOR_ACTIVE_NMOS,
    "p": COLOR_ACTIVE_PMOS,
    "G": COLOR_POLY,
    "I": COLOR_METAL1_INPUT,
    "C": COLOR_METAL1_INTERNAL,
    "O": COLOR_METAL1_OUTPUT,
    "+": COLOR_VDD,
    "-": COLOR_VSS,
}

CONTACT_MAP = {
    "i": "I",
    "o": "O",
    "c": "C",
    "&": "+",
    "_": "-",
}


def parse_lef_macro(lef_content, macro_name):
    pattern = rf"(?<!PROPERTYDEFINITIONS\n  )MACRO\s+{macro_name}(.*?)END\s+{macro_name}"
    match = re.search(pattern, lef_content, re.DOTALL)
    if not match:
        return None
    body = match.group(1)

    pins = []
    for pin_match in re.finditer(r"PIN\s+([\w\[\]<>]+)(.*?)END\s+\1", body, re.DOTALL):
        pin_name = pin_match.group(1)
        pin_body = pin_match.group(2)
        direction_match = re.search(r"DIRECTION\s+(\w+)\s*;", pin_body)
        direction = direction_match.group(1) if direction_match else "UNKNOWN"
        rects = []
        for port_match in re.finditer(r"PORT\s+(.*?)END", pin_body, re.DOTALL):
            port_body = port_match.group(1)
            for layer_match in re.finditer(r"LAYER\s+(\w+)\s*;(.*?)(?=LAYER|END|$)", port_body, re.DOTALL):
                layer_name = layer_match.group(1)
                for r in re.findall(r"RECT\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s+([\d\.\-]+)\s*;", layer_match.group(2)):
                    rects.append({"layer": layer_name, "coords": [float(x) for x in r]})
        pins.append({"name": pin_name, "direction": direction, "rects": rects})
    return {"pins": pins}


def parse_design_md(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    layers = {}
    pattern = r"## (.*?)\n(?:GOLDEN STANDARD\n\n)?```\n(.*?)\n```"
    for layer_name, grid_text in re.findall(pattern, content, re.DOTALL):
        lines = grid_text.strip("\n").split("\n")
        if not lines:
            continue
        scale_line = lines[0]
        width = len(scale_line[2:])
        grid_lines = lines[1:]
        parsed_grid = [list(line[2:].ljust(width)) for line in grid_lines]
        if not parsed_grid:
            continue
        parsed_grid.reverse()
        h = len(parsed_grid)
        w = width
        final_grid = [[None for _ in range(h)] for _ in range(w)]
        for z in range(h):
            for x in range(w):
                char = parsed_grid[z][x]
                if char != " ":
                    final_grid[x][z] = char
        layers[layer_name] = final_grid
    return layers


def generate_ldr_from_layers(cell_name, layers, macro_data, cif_data=None):
    ldr_lines = [
        f"0 {cell_name}.ldr",
        f"0 Name: {cell_name}.ldr",
        "0 Author: design_to_ldr.py",
        "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt",
        "0 !LPUB PLI GLOBAL ON",
        "",
    ]

    sub_grid = layers.get("Substrate")
    if sub_grid:
        w, h = len(sub_grid), len(sub_grid[0])
        y0_lines = []
        for plate, x, z, color, rot, *_ in tile_substrate_low(w, h):
            rot_str = "0 0 1 0 1 0 -1 0 0" if rot else "1 0 0 0 1 0 0 0 1"
            y0_lines.append(f"1 {color} {x} 0 {z} {rot_str} {plate}")
        for i in range(0, len(y0_lines), 28):
            if i == 0:
                ldr_lines.append("0 // Substrate low (V3)")
            else:
                ldr_lines.append("0 STEP")
                ldr_lines.append("0 // Substrate low (V3) (cont.)")
            ldr_lines.extend(y0_lines[i : i + 28])

        high_grid = [[COLOR_MAP_REV.get(sub_grid[x][z], COLOR_SUBSTRATE) for z in range(h)] for x in range(w)]
        y8_lines = []
        for plate, x, z, color, rot, *_ in tile_substrate_high_with_snapping(high_grid, w, h):
            rot_str = "0 0 1 0 1 0 -1 0 0" if rot else "1 0 0 0 1 0 0 0 1"
            y8_lines.append(f"1 {color} {x} -8 {z} {rot_str} {plate}")
        emit_chunked_steps(ldr_lines, "0 // Substrate high / N-Well", y8_lines)
    else:
        w, h = 0, 15

    if "Active" in layers:
        grid = layers["Active"]
        w, h = len(grid), len(grid[0])
        active_grid = [[COLOR_MAP_REV.get(grid[x][z]) for z in range(h)] for x in range(w)]
        # Guarantee 100% solid Y=-16 floor using Substrate/N-Well fill for empty studs
        for x in range(w):
            for z in range(h):
                if active_grid[x][z] is None:
                    if sub_grid and x < len(sub_grid) and z < len(sub_grid[x]):
                        active_grid[x][z] = COLOR_MAP_REV.get(sub_grid[x][z], COLOR_SUBSTRATE if z < 8 else COLOR_NWELL)
                    else:
                        active_grid[x][z] = COLOR_SUBSTRATE if z < 8 else COLOR_NWELL
        y16_lines = []
        if w >= 2:
            for z_anch in (1, 13):
                active_grid[0][z_anch] = active_grid[1][z_anch]
                c_anch = active_grid[0][z_anch]
                y16_lines.append(f"1 {c_anch} 20 {Y_ACTIVE} {z_anch * 20 + 10} 1 0 0 0 1 0 0 0 1 3023.dat")
                active_grid[0][z_anch] = None
                active_grid[1][z_anch] = None
        for plate, x, z, color, rot, *_ in get_best_plates_multi(active_grid):
            rot_str = "0 0 1 0 1 0 -1 0 0" if rot else "1 0 0 0 1 0 0 0 1"
            y16_lines.append(f"1 {color} {x} {Y_ACTIVE} {z} {rot_str} {plate}")
        emit_chunked_steps(ldr_lines, "0 // Active Regions", y16_lines)

    poly_grid_chars = layers.get("Polysilicon")
    if poly_grid_chars:
        pw, ph = len(poly_grid_chars), len(poly_grid_chars[0])
        poly_grid = [[COLOR_MAP_REV.get(poly_grid_chars[x][z]) for z in range(ph)] for x in range(pw)]
        y24_lines = []
        for plate, x, z, color, rot, *_ in get_best_plates_multi(poly_grid):
            rot_str = "0 0 1 0 1 0 -1 0 0" if rot else "1 0 0 0 1 0 0 0 1"
            y24_lines.append(f"1 {color} {x} {Y_POLY} {z} {rot_str} {plate}")
        emit_chunked_steps(ldr_lines, "0 // Polysilicon Gates", y24_lines)
    else:
        poly_grid = [[None for _ in range(h)] for _ in range(w)]

    if "Metal 1" in layers:
        grid = layers["Metal 1"]
        w, h = len(grid), len(grid[0])
        contact_studs = set()
        contact_base_lines = []
        contact_brick_lines = []
        metal2_tile_entries = []

        for x in range(w):
            for z in range(h):
                char = grid[x][z]
                if char in CONTACT_MAP or char == "c":
                    contact_studs.add((x, z))
                    sx, sz = x * 20 + 10, z * 20 + 10
                    real_char = CONTACT_MAP.get(char, char)
                    color = COLOR_MAP_REV.get(real_char)
                    if color is not None:
                        metal2_tile_entries.append((color, x, z))

                    # Check actual Polysilicon presence (never blindly assume z==6 has Poly)
                    has_poly = (
                        poly_grid_chars is not None
                        and x < len(poly_grid_chars)
                        and z < len(poly_grid_chars[x])
                        and poly_grid_chars[x][z] == "G"
                    )
                    if not has_poly:
                        contact_base_lines.append(
                            f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}"
                        )
                    contact_brick_lines.append(
                        f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}"
                    )

        # Tile Metal 1 per pin
        assigned = [[False for _ in range(h)] for _ in range(w)]
        m1_all_tiles = []
        m1_lines = []

        if macro_data:
            for pin in macro_data["pins"]:
                pin_grid = [[None for _ in range(h)] for _ in range(w)]
                has_pin_parts = False
                for rect in pin["rects"]:
                    if rect["layer"] == "Metal1":
                        x1 = int(math.floor(rect["coords"][0] * 20 / 0.27 / 20))
                        z1 = int(math.floor((rect["coords"][1] * 20 / 0.27 + 10) / 20))
                        x2 = int(math.ceil(rect["coords"][2] * 20 / 0.27 / 20))
                        z2 = int(math.ceil((rect["coords"][3] * 20 / 0.27 + 10) / 20))
                        for ix in range(min(x1, x2), max(x1, x2)):
                            for iz in range(min(z1, z2), max(z1, z2)):
                                if 0 <= ix < w and 0 <= iz < h and not assigned[ix][iz]:
                                    char = grid[ix][iz]
                                    if char:
                                        real_char = CONTACT_MAP.get(char, char)
                                        color = COLOR_MAP_REV.get(real_char)
                                        if color is not None:
                                            pin_grid[ix][iz] = color
                                            assigned[ix][iz] = True
                                            has_pin_parts = True
                if has_pin_parts:
                    pin_label = (
                        f"0 // {pin['name']} Rail" if pin["name"] in ["VDD", "VSS"] else f"0 // Pin {pin['name']}"
                    )
                    m1_lines.append(pin_label)
                    for plate, x, z, c, rot, x0, z0, x1, z1 in get_best_plates_multi(pin_grid):
                        rot_str = "0 0 1 0 1 0 -1 0 0" if rot else "1 0 0 0 1 0 0 0 1"
                        m1_lines.append(f"1 {c} {x} {Y_METAL1} {z} {rot_str} {plate}")
                        m1_all_tiles.append((plate, x, z, c, rot, x0, z0, x1, z1))

        rem_grid = [[None for _ in range(h)] for _ in range(w)]
        has_rem = False
        for x in range(w):
            for z in range(h):
                if not assigned[x][z] and grid[x][z]:
                    char = grid[x][z]
                    real_char = CONTACT_MAP.get(char, char)
                    color = COLOR_MAP_REV.get(real_char)
                    if color is not None:
                        rem_grid[x][z] = color
                        has_rem = True
        if has_rem:
            m1_lines.append("0 // Internal / Obstructions")
            for plate, x, z, c, rot, x0, z0, x1, z1 in get_best_plates_multi(rem_grid):
                rot_str = "0 0 1 0 1 0 -1 0 0" if rot else "1 0 0 0 1 0 0 0 1"
                m1_lines.append(f"1 {c} {x} {Y_METAL1} {z} {rot_str} {plate}")
                m1_all_tiles.append((plate, x, z, c, rot, x0, z0, x1, z1))

        # Trans-Clear (47) dielectric support pillars for uncontacted/cantilevered M1 plates
        diel_supports = compute_dielectric_supports(m1_all_tiles, contact_studs, poly_grid, w, h)
        for sx, sz, needs_plate in diel_supports:
            lx, lz = sx * 20 + 10, sz * 20 + 10
            if needs_plate:
                contact_base_lines.append(
                    f"1 {COLOR_DIELECTRIC} {lx} {Y_POLY} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}"
                )
            contact_brick_lines.append(
                f"1 {COLOR_DIELECTRIC} {lx} {Y_CONTACT} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}"
            )

        emit_chunked_steps(ldr_lines, "0 // Contact & Dielectric Bases", contact_base_lines)
        emit_chunked_steps(ldr_lines, "0 // Contact & Dielectric Pillars", contact_brick_lines)
        emit_chunked_steps(ldr_lines, "0 // Metal 1", m1_lines)

        # Via 1 (L19D0) & Metal 2 (L10D0) from CIF if present
        via1_studs = set()
        via1_lines = []
        m1_occupied = [[grid[x][z] is not None for z in range(h)] for x in range(w)]
        if cif_data and "L19D0" in cif_data["layers"]:
            for geom in cif_data["layers"]["L19D0"]:
                if geom["type"] == "box":
                    x1, z1, x2, z2 = geom["coords"]
                    cx, cz = (x1 + x2) / 2, (z1 + z2) / 2
                    best_v = None
                    min_d = float("inf")
                    for ix in range(w):
                        for iz in range(h):
                            if m1_occupied[ix][iz]:
                                d = abs(ix * 20 + 10 - cx) + abs(iz * 20 + 10 - cz)
                                if d < min_d:
                                    min_d = d
                                    best_v = (ix, iz)
                    if best_v and best_v not in via1_studs:
                        vx, vz = best_v
                        via1_studs.add((vx, vz))
                        via1_lines.append(
                            f"1 {COLOR_CONTACT} {vx * 20 + 10} {Y_METAL2_PLATE} {vz * 20 + 10} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}"
                        )

        m2_grid = [[None for _ in range(h)] for _ in range(w)]
        m2_tiles = []
        if cif_data and "L10D0" in cif_data["layers"]:
            for geom in cif_data["layers"]["L10D0"]:
                for ix in range(w):
                    for iz in range(h):
                        if is_stud_occupied_geom(ix * 20, iz * 20, geom):
                            m2_grid[ix][iz] = COLOR_METAL2
            m2_tiles = get_best_plates_multi(m2_grid)
            for _, _, _, _, _, x0, z0, x1, z1 in m2_tiles:
                p_studs = [(ix, iz) for ix in range(x0, x1) for iz in range(z0, z1)]
                if not any(s in via1_studs for s in p_studs):
                    sup = next((s for s in p_studs if m1_occupied[s[0]][s[1]]), None)
                    if sup and sup not in via1_studs:
                        via1_studs.add(sup)
                        via1_lines.append(
                            f"1 {COLOR_DIELECTRIC} {sup[0] * 20 + 10} {Y_METAL2_PLATE} {sup[1] * 20 + 10} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}"
                        )
                    elif not sup:
                        s0 = p_studs[len(p_studs) // 2]
                        lx, lz = s0[0] * 20 + 10, s0[1] * 20 + 10
                        if not (poly_grid_chars and s0[0] < len(poly_grid_chars) and s0[1] < len(poly_grid_chars[s0[0]]) and poly_grid_chars[s0[0]][s0[1]] == "G"):
                            via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_POLY} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                        via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_CONTACT} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                        via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_METAL1} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                        via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_METAL2_PLATE} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                        via1_studs.add(s0)

        m1_tile_lines = [
            f"1 {c} {bx * 20 + 10} {Y_METAL2_PLATE} {bz * 20 + 10} 1 0 0 0 1 0 0 0 1 {TILE_1X1}"
            for c, bx, bz in metal2_tile_entries
            if (bx, bz) not in via1_studs
        ]
        emit_chunked_steps(ldr_lines, "0 // Top Tile Markers & Via 1", m1_tile_lines + via1_lines)

        if m2_tiles:
            m2_lines = []
            for plate, x_off, z_off, color, rotated, *_ in m2_tiles:
                rot_str = "0 0 1 0 1 0 -1 0 0" if rotated else "1 0 0 0 1 0 0 0 1"
                m2_lines.append(f"1 {color} {x_off} {Y_METAL2} {z_off} {rot_str} {plate}")
            emit_chunked_steps(ldr_lines, "0 // Metal 2", m2_lines)
            m2_caps = [
                f"1 {COLOR_METAL2} {vx * 20 + 10} {Y_METAL2_TILE} {vz * 20 + 10} 1 0 0 0 1 0 0 0 1 {TILE_1X1}"
                for vx, vz in sorted(via1_studs)
                if m2_grid[vx][vz] is not None
            ]
            emit_chunked_steps(ldr_lines, "0 // Metal 2 Tiles", m2_caps)

    return "\n".join(ldr_lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", help="Process only a specific cell")
    args = parser.parse_args()

    lef_path = "specifications/sg13g2_stdcell.lef"
    with open(lef_path, "r", encoding="utf-8") as f:
        lef_content = f.read()
    design_dir, models_dir = "design", "models"
    os.makedirs(models_dir, exist_ok=True)

    files = sorted(os.listdir(design_dir))
    if args.cell:
        files = [f"{args.cell}.md"]

    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(design_dir, filename)
            if not os.path.exists(filepath):
                print(f"Error: {filepath} not found")
                continue
            cell_name = filename[:-3]
            print(f"Processing {cell_name}...")
            macro_data = parse_lef_macro(lef_content, cell_name)
            layers = parse_design_md(filepath)
            cif_data = parse_cif(f"specifications/cells/{cell_name}.cif")
            ldr_content = generate_ldr_from_layers(cell_name, layers, macro_data, cif_data)
            with open(os.path.join(models_dir, f"{cell_name}.ldr"), "w", encoding="utf-8") as f:
                f.write(ldr_content)


if __name__ == "__main__":
    main()
