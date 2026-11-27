import os
import sys
from collections import defaultdict

PLATE_DIMS = {
    "91405.dat": (16, 16), "92438.dat": (16, 8), "3027.dat": (16, 6), "3456.dat": (14, 6),
    "3028.dat": (12, 6), "3033.dat": (10, 6), "3029.dat": (12, 4), "3036.dat": (8, 6),
    "3030.dat": (10, 4), "3958.dat": (6, 6), "4282.dat": (16, 2), "3035.dat": (8, 4),
    "2445.dat": (12, 2), "3032.dat": (6, 4), "3832.dat": (10, 2), "3034.dat": (8, 2),
    "3031.dat": (4, 4), "60479.dat": (12, 1), "3795.dat": (6, 2), "4477.dat": (10, 1),
    "3460.dat": (8, 1), "3020.dat": (4, 2), "3666.dat": (6, 1), "3021.dat": (3, 2),
    "3710.dat": (4, 1), "3022.dat": (2, 2), "3623.dat": (3, 1), "3023.dat": (2, 1),
    "3024.dat": (1, 1), "3070.dat": (1, 1), "3070b.dat": (1, 1), "6141.dat": (1, 1),
    "3062b.dat": (1, 1),
}

PART_HEIGHT = defaultdict(lambda: 8)
PART_HEIGHT["3062b.dat"] = 24

NO_TOP_STUDS = {"3070.dat", "3070b.dat"}

DISCONTINUED_COLORS = {7, 8, 9}
DISCONTINUED_PARTS = {"3070.dat"}

# Plates that do not exist (or are unobtainable) in specific specialized colors
UNAVAILABLE_COLOR_PARTS = {
    38: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3032.dat", "3832.dat", "3034.dat", "3031.dat", "60479.dat", "4477.dat", "3460.dat"},
    288: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3032.dat", "3832.dat", "3034.dat", "60479.dat", "4477.dat", "3460.dat"},
    212: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3832.dat", "60479.dat", "4477.dat"},
    272: {"91405.dat", "92438.dat", "3027.dat", "3456.dat", "3028.dat", "3033.dat", "3029.dat", "3036.dat", "3030.dat", "3958.dat", "4282.dat", "3035.dat", "2445.dat", "3832.dat", "60479.dat", "4477.dat"},
}


def verify_ldr_buildability(filepath):
    parts = []
    step_counts = defaultdict(int)
    current_step = 1
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("0 STEP"):
                current_step += 1
            elif line.startswith("1 "):
                toks = line.split()
                if len(toks) < 15:
                    continue
                color = int(toks[1])
                x, y, z = float(toks[2]), float(toks[3]), float(toks[4])
                rot = [float(t) for t in toks[5:14]]
                part = toks[14].lower()
                pw, pd = PLATE_DIMS.get(part, (1, 1))
                if abs(rot[0]) < 0.5:
                    pw, pd = pd, pw
                x0 = int(round((x - pw * 10) / 20))
                z0 = int(round((z - pd * 10) / 20))
                studs = [(ix, iz) for ix in range(x0, x0 + pw) for iz in range(z0, z0 + pd)]
                h = PART_HEIGHT[part]
                y_top = int(round(y))
                y_bot = y_top + h
                parts.append({
                    "id": len(parts), "part": part, "color": color,
                    "y_top": y_top, "y_bot": y_bot, "studs": studs,
                    "x0": x0, "x1": x0 + pw, "z0": z0, "z1": z0 + pd
                })
                step_counts[current_step] += 1

    errors = []
    if not parts:
        return ["Empty LDR model"]

    # 1. Voxel collision check
    voxels = defaultdict(list)
    top_stud_at = defaultdict(list)
    for p in parts:
        for ys in range(p["y_top"], p["y_bot"], 8):
            for s in p["studs"]:
                voxels[(s[0], s[1], ys)].append(p["id"])
        if p["part"] not in NO_TOP_STUDS:
            for s in p["studs"]:
                top_stud_at[(s[0], s[1], p["y_top"])].append(p["id"])

    collisions = sum(1 for pids in voxels.values() if len(pids) > 1)
    if collisions:
        errors.append(f"Voxel collisions: {collisions}")

    # 2. 3D Clutch Graph from Y=0
    adj = defaultdict(set)
    grounded = set()
    for p in parts:
        if p["y_top"] == 0:
            grounded.add(p["id"])
        for s in p["studs"]:
            for sup_id in top_stud_at.get((s[0], s[1], p["y_bot"]), []):
                adj[p["id"]].add(sup_id)
                adj[sup_id].add(p["id"])

    visited = set(grounded)
    q = list(grounded)
    while q:
        u = q.pop()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)

    floating = [p for p in parts if p["id"] not in visited]
    if floating:
        errors.append(f"Floating parts not grounded to Y=0: {len(floating)}")

    # 3. Y=-48 pillars must rest on Y=-24 stud
    y48_floating = 0
    for p in parts:
        if p["y_top"] == -48:
            if not any(top_stud_at.get((s[0], s[1], -24)) for s in p["studs"]):
                y48_floating += 1
    if y48_floating:
        errors.append(f"Y=-48 contact/support bricks floating over air: {y48_floating}")

    # 4. Metal 1 (Y=-56) support quality: zero-support, spinners, cantilevers > 3 studs
    m1_zero = 0
    m1_spinner = 0
    m1_cantilever = 0
    for p in parts:
        if p["y_top"] == -56:
            sup_studs = [s for s in p["studs"] if top_stud_at.get((s[0], s[1], -48))]
            area = len(p["studs"])
            if len(sup_studs) == 0:
                m1_zero += 1
            elif area >= 2 and len(sup_studs) == 1:
                m1_spinner += 1
            if sup_studs and area >= 4:
                max_dist = max(min(abs(sx - ux) + abs(sz - uz) for ux, uz in sup_studs) for sx, sz in p["studs"])
                if max_dist > 3:
                    m1_cantilever += 1
    if m1_zero:
        errors.append(f"Metal 1 plates with 0 pillar supports: {m1_zero}")
    if m1_spinner:
        errors.append(f"Metal 1 multi-stud spinner plates (only 1 pillar): {m1_spinner}")
    if m1_cantilever:
        errors.append(f"Metal 1 plates with cantilever overhang > 3 studs: {m1_cantilever}")

    # 5. Base foundation (Y=0, -8, -16) single connected component
    base_ids = {p["id"] for p in parts if p["y_top"] in (0, -8, -16)}
    b_vis = set()
    b_comps = 0
    for bid in base_ids:
        if bid not in b_vis:
            b_comps += 1
            bq = [bid]
            b_vis.add(bid)
            while bq:
                u = bq.pop()
                for v in adj[u]:
                    if v in base_ids and v not in b_vis:
                        b_vis.add(v)
                        bq.append(v)
    if b_comps > 1:
        errors.append(f"Base foundation (Y=0/-8/-16) split into {b_comps} disconnected chunks")

    # 6. Horizontal East/West cell-to-cell snapping tabs at Y=-8 (Z=1, 13)
    y0_parts = [p for p in parts if p["y_top"] == 0]
    w_studs = max((p["x1"] for p in y0_parts), default=0)
    y8_studs = {s for p in parts if p["y_top"] == -8 for s in p["studs"]}
    has_west_recess = (0, 1) not in y8_studs and (0, 13) not in y8_studs
    has_east_tab = (w_studs, 1) in y8_studs and (w_studs, 13) in y8_studs
    if not (has_west_recess and has_east_tab):
        errors.append("Missing Y=-8 half-lap East/West cell-to-cell snapping tabs at Z=1, 13")

    # 7. Modern BrickLink color & mold availability
    bad_colors = {p["color"] for p in parts if p["color"] in DISCONTINUED_COLORS}
    if bad_colors:
        errors.append(f"Discontinued pre-2004/vintage colors used: {sorted(bad_colors)}")
    bad_parts = {p["part"] for p in parts if p["part"] in DISCONTINUED_PARTS}
    if bad_parts:
        errors.append(f"Discontinued grooveless parts used: {sorted(bad_parts)}")
    unavail = {(p["color"], p["part"]) for p in parts if p["part"] in UNAVAILABLE_COLOR_PARTS.get(p["color"], set())}
    if unavail:
        errors.append(f"Unavailable (color, mold) combos: {len(unavail)}")

    # 8. Step size check
    big_steps = [(st, cnt) for st, cnt in step_counts.items() if cnt > 40]
    if big_steps:
        errors.append(f"Steps with >40 parts: {big_steps}")

    return errors


def main():
    models_dir = sys.argv[1] if len(sys.argv) > 1 else "models"
    files = sorted([f for f in os.listdir(models_dir) if f.endswith(".ldr")])
    passed = 0
    for f in files:
        errs = verify_ldr_buildability(os.path.join(models_dir, f))
        if errs:
            print(f"FAIL: {f}")
            for e in errs:
                print(f"  - {e}")
        else:
            passed += 1
    print(f"\nBuildability Summary: {passed}/{len(files)} PASS")
    if passed != len(files):
        sys.exit(1)


if __name__ == "__main__":
    main()
