import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

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

UM_TO_LDU = 20 / 0.27
CIF_TO_LDU = 20 / 270
SNAPPING_TOLERANCE = 9.0


def parse_lef_directions(lef_path="specifications/sg13g2_stdcell.lef"):
    """Parse pin directions for all macros from LEF."""
    directions = {}
    if not os.path.exists(lef_path):
        return directions
    with open(lef_path, "r", encoding="utf-8") as f:
        content = f.read()
    for block in re.finditer(r"(?<!PROPERTYDEFINITIONS\n  )MACRO\s+([\w\[\]<>]+)(.*?)END\s+\1", content, re.DOTALL):
        macro_name = block.group(1)
        body = block.group(2)
        pin_dirs = {}
        for pm in re.finditer(r"PIN\s+([\w\[\]<>]+)(.*?)END\s+\1", body, re.DOTALL):
            pname = pm.group(1)
            pbody = pm.group(2)
            dm = re.search(r"DIRECTION\s+(\w+)\s*;", pbody)
            pin_dirs[pname] = dm.group(1) if dm else "UNKNOWN"
        directions[macro_name] = pin_dirs
    return directions


def parse_cif(cif_path):
    if not os.path.exists(cif_path):
        return None
    with open(cif_path, "r", encoding="utf-8") as f:
        cif_content = f.read()
    layers = {}
    labels = []
    boundary = None
    current_layer = None

    def to_ldr_x(val):
        return val * CIF_TO_LDU

    def to_ldr_z(val):
        return val * CIF_TO_LDU + 10

    for cmd in cif_content.split(";"):
        cmd = cmd.strip()
        if not cmd:
            continue
        if cmd.startswith("L "):
            current_layer = cmd[2:].strip()
            if current_layer not in layers:
                layers[current_layer] = []
        elif cmd.startswith("B "):
            parts = re.split(r"\s+|,", cmd[2:].strip())
            if len(parts) >= 4:
                try:
                    w_nm, h_nm, xc_nm, yc_nm = map(float, parts[:4])
                    x1, z1 = to_ldr_x(xc_nm - w_nm / 2), to_ldr_z(yc_nm - h_nm / 2)
                    x2, z2 = to_ldr_x(xc_nm + w_nm / 2), to_ldr_z(yc_nm + h_nm / 2)
                    geom = {"type": "box", "coords": [min(x1, x2), min(z1, z2), max(x1, x2), max(z1, z2)]}
                    if current_layer == "L189D4":
                        boundary = geom
                    elif current_layer:
                        layers[current_layer].append(geom)
                except ValueError:
                    continue
        elif cmd.startswith("P "):
            if current_layer:
                points = []
                for p in cmd[2:].strip().split():
                    pt = p.split(",")
                    if len(pt) == 2:
                        try:
                            points.append((to_ldr_x(float(pt[0])), to_ldr_z(float(pt[1]))))
                        except ValueError:
                            continue
                if points:
                    layers[current_layer].append({"type": "polygon", "points": points})
        elif cmd.startswith("94 "):
            parts = re.split(r"\s+", cmd[3:].strip())
            if len(parts) >= 2:
                name = parts[0]
                coords = parts[1].split(",")
                if len(coords) == 2:
                    try:
                        labels.append({"name": name, "x": to_ldr_x(float(coords[0])), "z": to_ldr_z(float(coords[1]))})
                    except ValueError:
                        pass
    return {"layers": layers, "labels": labels, "boundary": boundary}


def is_point_in_poly(x, z, poly):
    n = len(poly)
    inside = False
    p1x, p1z = poly[0]
    for i in range(n + 1):
        p2x, p2z = poly[i % n]
        if min(p1z, p2z) < z <= max(p1z, p2z) and x <= max(p1x, p2x):
            if p1z != p2z:
                xints = (z - p1z) * (p2x - p1x) / (p2z - p1z) + p1x
                if p1x == p2x or x <= xints:
                    inside = not inside
        p1x, p1z = p2x, p2z
    return inside


def is_stud_occupied(gx, gz, xmin, xmax, zmin, zmax):
    overlap_x = min(xmax, gx + 20) - max(xmin, gx)
    overlap_z = min(zmax, gz + 20) - max(zmin, gz)
    if overlap_x <= 0 or overlap_z <= 0:
        return False
    center_x, center_z = (xmin + xmax) / 2, (zmin + zmax) / 2
    width, height = xmax - xmin, zmax - zmin
    is_occ_x = (gx <= center_x < gx + 20) if width <= 21.0 else (overlap_x >= SNAPPING_TOLERANCE)
    is_occ_z = (gz <= center_z < gz + 20) if height <= 21.0 else (overlap_z >= SNAPPING_TOLERANCE)
    return is_occ_x and is_occ_z


def _segments_intersect(a1, a2, b1, b2):
    def ccw(p1, p2, p3):
        return (p3[1] - p1[1]) * (p2[0] - p1[0]) > (p2[1] - p1[1]) * (p3[0] - p1[0])

    return ccw(a1, b1, b2) != ccw(a2, b1, b2) and ccw(a1, a2, b1) != ccw(a1, a2, b2)


def is_stud_occupied_geom(gx, gz, geom):
    if geom["type"] == "box":
        xmin, zmin, xmax, zmax = geom["coords"]
        return is_stud_occupied(gx, gz, xmin, xmax, zmin, zmax)
    if geom["type"] == "polygon":
        poly = geom["points"]
        xs, zs = [p[0] for p in poly], [p[1] for p in poly]
        xmin, zmin, xmax, zmax = min(xs), min(zs), max(xs), max(zs)
        if max(xmin, gx) >= min(xmax, gx + 20) or max(zmin, gz) >= min(zmax, gz + 20):
            return False
        # 1. Center of stud inside polygon
        if is_point_in_poly(gx + 10, gz + 10, poly):
            return True
        # 2. Sample sub-grid inside stud (handles narrow Metal1/Poly wires straddling stud centers)
        hits = 0
        for dx in (5.0, 10.0, 15.0):
            for dz in (5.0, 10.0, 15.0):
                if is_point_in_poly(gx + dx, gz + dz, poly):
                    hits += 1
        if hits >= 2:
            return True
        # 3. Any polygon edge crossing the stud centerlines (handles 0.13um=9.6 LDU poly gates)
        n = len(poly)
        cx_line = ((gx + 2, gz + 10), (gx + 18, gz + 10))
        cz_line = ((gx + 10, gz + 2), (gx + 10, gz + 18))
        for i in range(n):
            p1, p2 = poly[i], poly[(i + 1) % n]
            if _segments_intersect(p1, p2, *cx_line) or _segments_intersect(p1, p2, *cz_line):
                return True
    return False


def get_net_color(net_name, pin_dirs):
    if net_name == "VDD":
        return COLOR_VDD
    if net_name == "VSS":
        return COLOR_VSS
    direction = pin_dirs.get(net_name, "UNKNOWN")
    if direction in ("OUTPUT", "TRISTATE"):
        return COLOR_METAL1_OUTPUT
    if direction in ("INPUT", "INOUT"):
        return COLOR_METAL1_INPUT
    if net_name in ("X", "Y", "Q", "Q_N", "Z", "GCLK", "L_HI", "L_LO"):
        return COLOR_METAL1_OUTPUT
    if net_name:
        return COLOR_METAL1_INPUT
    return COLOR_METAL1_INTERNAL


def generate_ldr(cif_data, cell_name, pin_dirs=None):
    pin_dirs = pin_dirs or {}
    boundary = cif_data["boundary"]
    width_ldu = int(round((boundary["coords"][2] - boundary["coords"][0]) / 20) * 20) if boundary else 240
    if not width_ldu:
        width_ldu = 240
    height_ldu = 300
    w_studs, d_studs = width_ldu // 20, height_ldu // 20

    ldr_lines = [
        f"0 {cell_name}.ldr",
        f"0 Name: {cell_name}.ldr",
        "0 Author: cif_to_ldr.py",
        "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt",
        "0 !LPUB PLI GLOBAL ON",
        "",
    ]

    # 1. Substrate Low (Y=0) — seam-staggered & chunked for readability
    y0_lines = []
    for plate, x_off, z_off, color, rotated, *_ in tile_substrate_low(w_studs, d_studs):
        rot_str = "0 0 1 0 1 0 -1 0 0" if rotated else "1 0 0 0 1 0 0 0 1"
        y0_lines.append(f"1 {color} {x_off} 0 {z_off} {rot_str} {plate}")
    for i in range(0, len(y0_lines), 28):
        if i == 0:
            ldr_lines.append("0 // Substrate low (V3)")
        else:
            ldr_lines.append("0 STEP")
            ldr_lines.append("0 // Substrate low (V3) (cont.)")
        ldr_lines.extend(y0_lines[i : i + 28])

    # 2. Substrate High / N-Well (Y=-8) — use L31D0 (NWell.drawing), NOT L14D0 (pSD)!
    grid2 = [[COLOR_SUBSTRATE for _ in range(d_studs)] for _ in range(w_studs)]
    if "L31D0" in cif_data["layers"]:
        for geom in cif_data["layers"]["L31D0"]:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i * 20, k * 20, geom):
                        grid2[i][k] = COLOR_NWELL
    else:
        for i in range(w_studs):
            for k in range(8, d_studs):
                grid2[i][k] = COLOR_NWELL

    y8_lines = []
    for plate, x_off, z_off, color, rotated, *_ in tile_substrate_high_with_snapping(grid2, w_studs, d_studs):
        rot_str = "0 0 1 0 1 0 -1 0 0" if rotated else "1 0 0 0 1 0 0 0 1"
        y8_lines.append(f"1 {color} {x_off} -8 {z_off} {rot_str} {plate}")
    emit_chunked_steps(ldr_lines, "0 // Substrate high / N-Well", y8_lines)

    # 3. Active Regions (Y=-16) — include P-Substrate / N-Well fill so Y=-16 is 100% solid floor
    active_grid = [[grid2[i][k] for k in range(d_studs)] for i in range(w_studs)]
    if "L1D0" in cif_data["layers"]:
        for geom in cif_data["layers"]["L1D0"]:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i * 20, k * 20, geom):
                        active_grid[i][k] = COLOR_ACTIVE_PMOS if grid2[i][k] == COLOR_NWELL else COLOR_ACTIVE_NMOS
    for i in range(w_studs):
        active_grid[i][0] = COLOR_ACTIVE_NMOS
        active_grid[i][14] = COLOR_ACTIVE_PMOS
    y16_lines = []
    if w_studs >= 2:
        for z_anch in (1, 13):
            active_grid[0][z_anch] = active_grid[1][z_anch]
            c_anch = active_grid[0][z_anch]
            y16_lines.append(f"1 {c_anch} 20 {Y_ACTIVE} {z_anch * 20 + 10} 1 0 0 0 1 0 0 0 1 3023.dat")
            active_grid[0][z_anch] = None
            active_grid[1][z_anch] = None

    for plate, x_off, z_off, color, rotated, *_ in get_best_plates_multi(active_grid):
        rot_str = "0 0 1 0 1 0 -1 0 0" if rotated else "1 0 0 0 1 0 0 0 1"
        y16_lines.append(f"1 {color} {x_off} {Y_ACTIVE} {z_off} {rot_str} {plate}")
    emit_chunked_steps(ldr_lines, "0 // Active Regions", y16_lines)

    # 4. Polysilicon Gates (Y=-24)
    poly_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
    if "L5D0" in cif_data["layers"]:
        for geom in cif_data["layers"]["L5D0"]:
            for i in range(w_studs):
                for k in range(1, 14):
                    if is_stud_occupied_geom(i * 20, k * 20, geom):
                        poly_grid[i][k] = COLOR_POLY

    y24_lines = []
    for plate, x_off, z_off, color, rotated, *_ in get_best_plates_multi(poly_grid):
        rot_str = "0 0 1 0 1 0 -1 0 0" if rotated else "1 0 0 0 1 0 0 0 1"
        y24_lines.append(f"1 {color} {x_off} {Y_POLY} {z_off} {rot_str} {plate}")
    emit_chunked_steps(ldr_lines, "0 // Polysilicon Gates", y24_lines)

    # 5. Map CIF Metal 1 geometries to net names via L8D25 labels
    m1_geoms = cif_data["layers"].get("L8D0", [])
    geom_to_net = {}
    for idx, geom in enumerate(m1_geoms):
        matched_net = None
        for label in cif_data["labels"]:
            lx, lz = label["x"], label["z"]
            if geom["type"] == "box":
                x1, z1, x2, z2 = geom["coords"]
                if x1 - 5 <= lx <= x2 + 5 and z1 - 5 <= lz <= z2 + 5:
                    matched_net = label["name"]
                    break
            elif geom["type"] == "polygon":
                if is_point_in_poly(lx, lz, geom["points"]):
                    matched_net = label["name"]
                    break
        geom_to_net[idx] = matched_net

    # Ensure every cell has VDD (Z=14) and VSS (Z=0) rail assignments
    net_grids = {}
    claimed = [[False for _ in range(d_studs)] for _ in range(w_studs)]

    # Process named nets first (VDD, VSS, Outputs, Inputs), then Internal
    ordered_indices = sorted(
        range(len(m1_geoms)),
        key=lambda idx: (
            0 if geom_to_net[idx] in ("VDD", "VSS") else 1 if geom_to_net[idx] else 2,
            idx,
        ),
    )
    for idx in ordered_indices:
        geom = m1_geoms[idx]
        net_name = geom_to_net[idx] or f"Internal_{idx}"
        color = get_net_color(geom_to_net[idx], pin_dirs)
        if net_name not in net_grids:
            net_grids[net_name] = (color, [[None for _ in range(d_studs)] for _ in range(w_studs)])
        _, ngrid = net_grids[net_name]
        for i in range(w_studs):
            for k in range(d_studs):
                if not claimed[i][k] and is_stud_occupied_geom(i * 20, k * 20, geom):
                    ngrid[i][k] = color
                    claimed[i][k] = True

    # 6. Contacts (L6D0): snap to nearest valid EVEN-Z stud that has Metal 1 above it; rails on EVEN X
    contact_studs = set()
    contact_base_lines = []
    contact_brick_lines = []
    metal2_tile_entries = []  # (color, sx, sz)

    if "L6D0" in cif_data["layers"]:
        for geom in cif_data["layers"]["L6D0"]:
            if geom["type"] != "box":
                continue
            x1, z1, x2, z2 = geom["coords"]
            cx, cz = (x1 + x2) / 2, (z1 + z2) / 2
            best_stud = None
            min_dist = float("inf")
            # Prefer studs occupied by Metal 1 (claimed[i][k])
            for require_m1 in (True, False):
                for i in range(w_studs):
                    for k in range(0, d_studs, 2):  # EVEN Z tracks
                        if k in (0, 14) and i % 2 != 0:
                            continue  # Rail contacts on EVEN X
                        if require_m1 and not claimed[i][k]:
                            continue
                        sx, sz = i * 20 + 10, k * 20 + 10
                        dist = abs(sx - cx) + abs(sz - cz)
                        if dist < min_dist:
                            min_dist = dist
                            best_stud = (i, k)
                if best_stud is not None:
                    break
            if best_stud and best_stud not in contact_studs:
                bx, bz = best_stud
                if not claimed[bx][bz]:
                    continue
                contact_studs.add(best_stud)
                sx, sz = bx * 20 + 10, bz * 20 + 10
                if poly_grid[bx][bz] is None:
                    contact_base_lines.append(f"1 {COLOR_CONTACT} {sx} {Y_POLY} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                contact_brick_lines.append(f"1 {COLOR_CONTACT} {sx} {Y_CONTACT} {sz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")

                # Determine Metal1 color at this contact
                c_color = COLOR_METAL1_INTERNAL
                for net_name, (nc, ngrid) in net_grids.items():
                    if ngrid[bx][bz] is not None:
                        c_color = nc
                        break
                metal2_tile_entries.append((c_color, bx, bz))

    # 7. Tile Metal 1 per net so distinct nets never merge into one plate
    m1_all_tiles = []
    m1_lines_grouped = []
    for net_name, (nc, ngrid) in net_grids.items():
        tiles = get_best_plates_multi(ngrid)
        if not tiles:
            continue
        if net_name in ("VDD", "VSS"):
            m1_lines_grouped.append(f"0 // {net_name} Rail")
        elif not net_name.startswith("Internal_"):
            m1_lines_grouped.append(f"0 // Pin {net_name}")
        else:
            m1_lines_grouped.append("0 // Internal / Obstructions")
        for plate, x_off, z_off, color, rotated, x0, z0, x1, z1 in tiles:
            rot_str = "0 0 1 0 1 0 -1 0 0" if rotated else "1 0 0 0 1 0 0 0 1"
            m1_lines_grouped.append(f"1 {color} {x_off} {Y_METAL1} {z_off} {rot_str} {plate}")
            m1_all_tiles.append((plate, x_off, z_off, color, rotated, x0, z0, x1, z1))

    # 8. Compute Trans-Clear (47) dielectric support pillars for uncontacted/cantilevered M1 plates
    diel_supports = compute_dielectric_supports(m1_all_tiles, contact_studs, poly_grid, w_studs, d_studs)
    for sx, sz, needs_plate in diel_supports:
        lx, lz = sx * 20 + 10, sz * 20 + 10
        if needs_plate:
            contact_base_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_POLY} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
        contact_brick_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_CONTACT} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")

    # Emit Contact Bases (Y=-24) BEFORE Contact Bricks (Y=-48)
    emit_chunked_steps(ldr_lines, "0 // Contact & Dielectric Bases", contact_base_lines)
    emit_chunked_steps(ldr_lines, "0 // Contact & Dielectric Pillars", contact_brick_lines)
    emit_chunked_steps(ldr_lines, "0 // Metal 1", m1_lines_grouped)

    # 9. Via 1 (L19D0 at Y=-64) & Metal 2 (L10D0 at Y=-72)
    via1_studs = set()
    via1_lines = []
    if "L19D0" in cif_data["layers"]:
        for geom in cif_data["layers"]["L19D0"]:
            if geom["type"] == "box":
                x1, z1, x2, z2 = geom["coords"]
                cx, cz = (x1 + x2) / 2, (z1 + z2) / 2
                best_v = None
                min_d = float("inf")
                for i in range(w_studs):
                    for k in range(d_studs):
                        if claimed[i][k]:
                            d = abs(i * 20 + 10 - cx) + abs(k * 20 + 10 - cz)
                            if d < min_d:
                                min_d = d
                                best_v = (i, k)
                if best_v and best_v not in via1_studs:
                    vx, vz = best_v
                    via1_studs.add((vx, vz))
                    via1_lines.append(
                        f"1 {COLOR_CONTACT} {vx * 20 + 10} {Y_METAL2_PLATE} {vz * 20 + 10} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}"
                    )

    m2_grid = [[None for _ in range(d_studs)] for _ in range(w_studs)]
    m2_tiles = []
    if "L10D0" in cif_data["layers"]:
        for geom in cif_data["layers"]["L10D0"]:
            for i in range(w_studs):
                for k in range(d_studs):
                    if is_stud_occupied_geom(i * 20, k * 20, geom):
                        m2_grid[i][k] = COLOR_METAL2
        m2_tiles = get_best_plates_multi(m2_grid)
        # Ensure every M2 plate has >=1 support on Metal 1 (Via1 or Trans-Clear 6141.dat at Y=-64)
        for _, _, _, _, _, x0, z0, x1, z1 in m2_tiles:
            p_studs = [(ix, iz) for ix in range(x0, x1) for iz in range(z0, z1)]
            if not any(s in via1_studs for s in p_studs):
                sup = next((s for s in p_studs if claimed[s[0]][s[1]]), None)
                if sup and sup not in via1_studs:
                    via1_studs.add(sup)
                    via1_lines.append(
                        f"1 {COLOR_DIELECTRIC} {sup[0] * 20 + 10} {Y_METAL2_PLATE} {sup[1] * 20 + 10} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}"
                    )
                elif not sup:
                    # Metal 2 plate is over open air (no M1 below): build Trans-Clear support from Y=-24/-16 up to Y=-64
                    s0 = p_studs[len(p_studs) // 2]
                    lx, lz = s0[0] * 20 + 10, s0[1] * 20 + 10
                    if poly_grid[s0[0]][s0[1]] is None:
                        via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_POLY} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                    via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_CONTACT} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_BRICK}")
                    via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_METAL1} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                    via1_lines.append(f"1 {COLOR_DIELECTRIC} {lx} {Y_METAL2_PLATE} {lz} 1 0 0 0 1 0 0 0 1 {ROUND_PLATE}")
                    via1_studs.add(s0)

    # Metal 2 Pin Tiles (Y=-64) — skip studs occupied by Via1 or M2 supports
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cif_to_ldr.py <cif_file>")
        sys.exit(1)
    cif_file = sys.argv[1]
    cell_name = os.path.basename(cif_file).replace(".cif", "")
    cif_data = parse_cif(cif_file)
    if not cif_data or not cif_data["boundary"]:
        print(f"Error: Could not parse CIF or missing boundary in {cif_file}")
        sys.exit(1)
    pin_dirs = parse_lef_directions().get(cell_name, {})
    ldr_content = generate_ldr(cif_data, cell_name, pin_dirs)
    os.makedirs("models", exist_ok=True)
    output_file = f"models/{cell_name}.ldr"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ldr_content)
    print(f"Generated {output_file}")
