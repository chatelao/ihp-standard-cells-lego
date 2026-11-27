"""Shared LEGO palette, mold-availability whitelist, seam-staggered tiling,
and dielectric support utilities for IHP SG13G2 standard cells.
"""

PLATES = [
    (16, 16, "91405.dat"), # 256
    (16, 8, "92438.dat"),  # 128
    (16, 6, "3027.dat"),   # 96
    (14, 6, "3456.dat"),   # 84
    (12, 6, "3028.dat"),   # 72
    (10, 6, "3033.dat"),   # 60
    (12, 4, "3029.dat"),   # 48
    (8, 6, "3036.dat"),    # 48
    (10, 4, "3030.dat"),   # 40
    (6, 6, "3958.dat"),    # 36
    (16, 2, "4282.dat"),   # 32
    (8, 4, "3035.dat"),    # 32
    (12, 2, "2445.dat"),   # 24
    (6, 4, "3032.dat"),    # 24
    (10, 2, "3832.dat"),   # 20
    (8, 2, "3034.dat"),    # 16
    (4, 4, "3031.dat"),    # 16
    (12, 1, "60479.dat"),  # 12
    (6, 2, "3795.dat"),    # 12
    (10, 1, "4477.dat"),   # 10
    (8, 1, "3460.dat"),    # 8
    (4, 2, "3020.dat"),    # 8
    (6, 1, "3666.dat"),    # 6
    (3, 2, "3021.dat"),    # 6
    (4, 1, "3710.dat"),    # 4
    (2, 2, "3022.dat"),    # 4
    (3, 1, "3623.dat"),    # 3
    (2, 1, "3023.dat"),    # 2
    (1, 1, "3024.dat"),    # 1
]

PLATE_DIMENSIONS = {p[2]: (p[0], p[1]) for p in PLATES}
PLATE_DIMENSIONS.update({
    "3070.dat": (1, 1),
    "3070b.dat": (1, 1),
    "6141.dat": (1, 1),
    "3062b.dat": (1, 1),
})

ROUND_BRICK = "3062b.dat"
ROUND_PLATE = "6141.dat"
TILE_1X1 = "3070b.dat"

# Modern BrickLink-purchasable LDraw Colors
COLOR_SUBSTRATE = 72       # Dark Bluish Gray (replaces retired 8)
COLOR_NWELL = 71           # Light Bluish Gray (replaces retired 7)
COLOR_ACTIVE_NMOS = 288    # Dark Green
COLOR_ACTIVE_PMOS = 38     # Dark Orange
COLOR_POLY = 4             # Red
COLOR_METAL1_INTERNAL = 1  # Blue
COLOR_METAL1_INPUT = 212   # Bright Light Blue (replaces vintage 9)
COLOR_METAL1_OUTPUT = 272  # Dark Blue
COLOR_VDD = 14             # Yellow
COLOR_VSS = 0              # Black
COLOR_CONTACT = 15         # White
COLOR_DIELECTRIC = 47      # Trans-Clear (SiO2 ILD support pillars)
COLOR_METAL2 = 25          # Orange (Metal 2 routing)

# Y-Offsets (Negative is up in LDraw)
Y_SUBSTRATE_LOW = 0
Y_SUBSTRATE_HIGH = -8
Y_ACTIVE = -16
Y_POLY = -24
Y_CONTACT = -48
Y_METAL1 = -56
Y_METAL2_PLATE = -64
Y_METAL2 = -72
Y_METAL2_TILE = -80

# Plates not manufactured / unobtainable in specialized colors
UNAVAILABLE_COLOR_PARTS = {
    38: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3032.dat", "3832.dat", "3034.dat", "3031.dat", "60479.dat", "4477.dat", "3460.dat"},
    288: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3032.dat", "3832.dat", "3034.dat", "60479.dat", "4477.dat", "3460.dat"},
    212: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3832.dat", "60479.dat", "4477.dat"},
    272: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3832.dat", "60479.dat", "4477.dat"},
}


def is_part_available(color, pfile):
    return pfile not in UNAVAILABLE_COLOR_PARTS.get(color, set())


def get_best_plates_multi(grid, prefer_rotated=False, max_x_bounds=None, max_z_bounds=None, x_start=0):
    """
    Greedily tile a 2D color grid [x][z] with BrickLink-available LEGO plates.
    Optionally constrains plates from crossing X-boundaries (max_x_bounds) or Z-boundaries (max_z_bounds)
    to implement seam-staggered bricklaying across layers.
    Returns list of (plate_file, x_off_ldu, z_off_ldu, color, is_rotated, x0, z0, x1, z1).
    """
    if not grid:
        return []
    w_studs = len(grid)
    d_studs = len(grid[0])
    covered = [[False for _ in range(d_studs)] for _ in range(w_studs)]
    tiles = []
    sorted_plates = sorted(PLATES, key=lambda p: p[0] * p[1], reverse=True)

    outer_range = range(w_studs) if prefer_rotated else range(d_studs)
    inner_range = range(d_studs) if prefer_rotated else range(w_studs)

    for o in outer_range:
        for i in inner_range:
            x, z = (o, i) if prefer_rotated else (i, o)
            if covered[x][z]:
                continue
            color = grid[x][z]
            if color is None:
                covered[x][z] = True
                continue

            # Determine local region limits from optional seam boundaries
            lim_x = w_studs
            if max_x_bounds:
                for bx in max_x_bounds:
                    if x < bx < lim_x:
                        lim_x = bx
            lim_z = d_studs
            if max_z_bounds:
                for bz in max_z_bounds:
                    if z < bz < lim_z:
                        lim_z = bz

            best_p = None
            for pw, pd, pfile in sorted_plates:
                if not is_part_available(color, pfile):
                    continue
                configs = (
                    [(pd, pw, pfile, True), (pw, pd, pfile, False)]
                    if prefer_rotated
                    else [(pw, pd, pfile, False), (pd, pw, pfile, True)]
                )
                for cpw, cpd, cpfile, crotated in configs:
                    if x + cpw <= lim_x and z + cpd <= lim_z:
                        if all(
                            not covered[ix][iz] and grid[ix][iz] == color
                            for ix in range(x, x + cpw)
                            for iz in range(z, z + cpd)
                        ):
                            best_p = (cpw, cpd, cpfile, crotated)
                            break
                if best_p:
                    break

            if best_p:
                rw, rd, pfile, rotated = best_p
                for ix in range(x, x + rw):
                    for iz in range(z, z + rd):
                        covered[ix][iz] = True
                x_off = (x_start + x) * 20 + (rw * 20) // 2
                z_off = z * 20 + (rd * 20) // 2
                tiles.append((pfile, x_off, z_off, color, rotated, x, z, x + rw, z + rd))
            else:
                covered[x][z] = True

    return tiles


def tile_substrate_low(w_studs, d_studs=15):
    """
    Tile Y=0 Substrate Low with seam-staggering:
    - X seams at 8, 24, 40, ... (or w_studs//2 for narrow cells <= 8 studs).
    - Z bands:
      * Z=0..2 (3 studs, bridging Z=0..1..2)
      * Z=3..4 (2 studs)
      * Z=5..10 (6 studs, bridging all N-Well splits at Z=6, 7, 8, 9)
      * Z=11..14 (4 studs, bridging Z=11..12 and Z=13..14)
    """
    if w_studs <= 8:
        x_bounds = [max(1, w_studs // 2)] if w_studs >= 2 else []
    else:
        x_bounds = [bx for bx in range(8, w_studs, 16)]

    tiles = []

    def add_z_strip(z_start, depth):
        if depth == 3:
            x = 0
            while x < w_studs:
                lim_x = w_studs
                for bx in x_bounds:
                    if x < bx < lim_x:
                        lim_x = bx
                pfile, rw = ("3021.dat", 2) if x + 2 <= lim_x else ("3623.dat", 1)
                x_off = x * 20 + (rw * 20) // 2
                z_off = z_start * 20 + (depth * 20) // 2
                tiles.append((pfile, x_off, z_off, COLOR_SUBSTRATE, True, x, z_start, x + rw, z_start + depth))
                x += rw
        else:
            grid_b = [[COLOR_SUBSTRATE for _ in range(depth)] for _ in range(w_studs)]
            for pfile, x_off, z_off_local, c, rot, x0, z0, x1, z1 in get_best_plates_multi(
                grid_b, prefer_rotated=True, max_x_bounds=x_bounds
            ):
                tiles.append((pfile, x_off, z_off_local + z_start * 20, c, rot, x0, z0 + z_start, x1, z1 + z_start))

    add_z_strip(0, 4)   # Z=0..3 (bridges Z=0..3)
    add_z_strip(4, 6)   # Z=4..9 (bridges all N-Well splits Z=5..9)
    add_z_strip(10, 1)  # Z=10
    add_z_strip(11, 4)  # Z=11..14 (bridges Z=11..14)
    return tiles


def tile_substrate_high_with_snapping(grid2_base, w_studs, d_studs=15):
    """
    Tile Y=-8 Substrate High / N-Well with:
    - Z=1 and Z=13 half-lap snapping rows: West recessed at X=0, East tab projecting to X=w_studs.
      Tiled East-to-West so the East tab at X=w_studs is always anchored by a >=2-stud plate.
    - Remaining Z rows tiled across 0..w_studs-1 with X seams at 16, 32, ... (staggered vs Y=0).
    """
    tiles = []
    # 1. Tile snapping strips at Z=1 and Z=13 (spanning X=1..w_studs, East-to-West)
    one_by_n = [(12, "60479.dat"), (10, "4477.dat"), (8, "3460.dat"), (6, "3666.dat"), (4, "3710.dat"), (3, "3623.dat"), (2, "3023.dat"), (1, "3024.dat")]
    for z_snap in (1, 13):
        snap_color = grid2_base[w_studs - 1][z_snap]
        x_end = w_studs + 1 # exclusive, spans 1..w_studs
        while x_end > 1:
            rem = x_end - 1
            chosen = None
            for pw, pfile in one_by_n:
                if pw <= rem and is_part_available(snap_color, pfile):
                    # Avoid leaving a 1-stud piece at the East end; if rem >= 2, pw >= 2
                    chosen = (pw, pfile)
                    break
            rw, pfile = chosen
            x0 = x_end - rw
            x_off = x0 * 20 + (rw * 20) // 2
            z_off = z_snap * 20 + 10
            tiles.append((pfile, x_off, z_off, snap_color, False, x0, z_snap, x_end, z_snap + 1))
            x_end = x0

    # 2. Tile main body excluding Z=1 and Z=13
    body_grid = [
        [None if z in (1, 13) else grid2_base[x][z] for z in range(d_studs)]
        for x in range(w_studs)
    ]
    tiles.extend(get_best_plates_multi(body_grid, prefer_rotated=False))
    return tiles


def compute_dielectric_supports(m1_tiles, contact_studs, poly_grid, w_studs, d_studs=15):
    """
    For every placed Metal 1 plate at Y=-56, ensure:
    - area == 1: >= 1 support pillar at Y=-48
    - area >= 2: >= 2 support pillars at Y=-48 (prevents spinning)
    - area >= 4: max Manhattan distance from any stud to nearest pillar <= 3 (prevents cantilevers)
    Returns list of (sx, sz, needs_round_plate_at_y24) for Trans-Clear (47) dielectric supports.
    """
    dielectric_studs = set()
    existing_all = set(contact_studs)

    for _, _, _, _, _, x0, z0, x1, z1 in m1_tiles:
        plate_studs = [(ix, iz) for ix in range(x0, x1) for iz in range(z0, z1)]
        area = len(plate_studs)
        if area == 0:
            continue
        supports = [s for s in plate_studs if s in existing_all]
        needed_min = 1 if area == 1 else 2

        while len(supports) < needed_min:
            if not supports:
                # Pick stud closest to center or first corner
                best = plate_studs[len(plate_studs) // 2]
            else:
                # Pick stud farthest from existing supports
                best = max(
                    (s for s in plate_studs if s not in supports),
                    key=lambda s: min(abs(s[0] - u[0]) + abs(s[1] - u[1]) for u in supports),
                )
            supports.append(best)
            existing_all.add(best)
            dielectric_studs.add(best)

        if area >= 4:
            while True:
                worst = max(
                    plate_studs,
                    key=lambda s: min(abs(s[0] - u[0]) + abs(s[1] - u[1]) for u in supports),
                )
                dist = min(abs(worst[0] - u[0]) + abs(worst[1] - u[1]) for u in supports)
                if dist <= 3:
                    break
                supports.append(worst)
                existing_all.add(worst)
                dielectric_studs.add(worst)

    result = []
    for sx, sz in sorted(dielectric_studs):
        has_poly = (
            0 <= sx < len(poly_grid)
            and 0 <= sz < len(poly_grid[sx])
            and poly_grid[sx][sz] in (COLOR_POLY, "G")
        )
        result.append((sx, sz, not has_poly))
    return result


def emit_chunked_steps(ldr_lines, header_comment, part_lines, max_per_step=28):
    """Emit part_lines in chunks of <= max_per_step separated by 0 STEP for readable PDF instructions.
    Preserves active '0 // Pin ...' / '0 // ... Rail' / '0 // Internal ...' sub-comments across steps.
    """
    if not part_lines:
        return
    chunks = []
    curr = []
    count = 0
    active_sub = None
    for line in part_lines:
        if line.startswith("0 // "):
            active_sub = line
            curr.append(line)
        else:
            if count >= max_per_step:
                chunks.append(curr)
                curr = [active_sub] if active_sub else []
                count = 0
            curr.append(line)
            count += 1
    if curr:
        chunks.append(curr)

    for idx, chunk in enumerate(chunks):
        ldr_lines.append("0 STEP")
        ldr_lines.append(header_comment if idx == 0 else f"{header_comment} (cont.)")
        ldr_lines.extend(chunk)
