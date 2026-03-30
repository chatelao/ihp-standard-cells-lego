import sys
import os
import math
import re
from PIL import Image, ImageDraw

# LDraw Color ID to RGB mapping
COLOR_RGB = {
    0: (30, 30, 30),     # VSS (Black)
    1: (0, 80, 180),    # M1 Conn (Blue)
    4: (200, 0, 0),     # Poly (Red)
    7: (160, 160, 160), # N-Well (Light Grey)
    8: (80, 80, 80),    # Substrate (Dark Grey)
    9: (100, 180, 240), # M1 Input (Light Blue)
    14: (220, 180, 0),  # VDD (Yellow)
    15: (255, 255, 255),# Contact (White)
    38: (140, 90, 40),  # PMOS (Dark Orange)
    272: (0, 40, 100),  # M1 Output (Dark Blue)
    288: (0, 80, 0),    # NMOS (Dark Green)
}

# Plate/Tile dimensions (width, depth) in studs
PLATE_DIMENSIONS = {
    "91405.dat": (16, 16), "92438.dat": (16, 8), "3027.dat": (16, 6),
    "3456.dat": (14, 6), "3028.dat": (12, 6), "3033.dat": (10, 6),
    "3029.dat": (12, 4), "3036.dat": (8, 6), "3030.dat": (10, 4),
    "3958.dat": (6, 6), "4282.dat": (16, 2), "3035.dat": (8, 4),
    "2445.dat": (12, 2), "3032.dat": (6, 4), "3832.dat": (10, 2),
    "3034.dat": (8, 2), "3031.dat": (4, 4), "60479.dat": (12, 1),
    "3795.dat": (6, 2), "4477.dat": (10, 1), "3460.dat": (8, 1),
    "3020.dat": (4, 2), "3666.dat": (6, 1), "3021.dat": (3, 2),
    "3710.dat": (4, 1), "3022.dat": (2, 2), "3623.dat": (3, 1),
    "3023.dat": (2, 1), "3024.dat": (1, 1), "3070.dat": (1, 1),
    "3062b.dat": (1, 1), "6141.dat": (1, 1),
}

def parse_ldr(ldr_path, limit_step=None):
    parts = []
    if not os.path.exists(ldr_path):
        return []
    current_step = 1
    with open(ldr_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('0 STEP'):
                current_step += 1
                if limit_step is not None and current_step > limit_step:
                    break
                continue

            if not line.startswith('1 '):
                continue
            tokens = line.split()
            if len(tokens) < 15:
                continue
            try:
                parts.append({
                    'color': int(tokens[1]),
                    'x': float(tokens[2]),
                    'y': float(tokens[3]),
                    'z': float(tokens[4]),
                    'm0': float(tokens[5]),
                    'm1': float(tokens[6]),
                    'm2': float(tokens[7]),
                    'm3': float(tokens[8]),
                    'm4': float(tokens[9]),
                    'm5': float(tokens[10]),
                    'm6': float(tokens[11]),
                    'm7': float(tokens[12]),
                    'm8': float(tokens[13]),
                    'part': tokens[14].lower()
                })
            except ValueError:
                continue
    return parts

def render(ldr_path, output_path=None, limit_step=None):
    parts = parse_ldr(ldr_path, limit_step=limit_step)
    if not parts:
        if not limit_step:
            print(f"No parts found in {ldr_path}")
        return None

    # Determine bounding box
    min_x, max_x = float('inf'), float('-inf')
    min_z, max_z = float('inf'), float('-inf')

    processed_parts = []
    for p in parts:
        pw, pd = PLATE_DIMENSIONS.get(p['part'], (1, 1))
        # Rotation check (top view, we care about XZ rotation)
        # Identity: m0=1, m1=0, m2=0, m3=0, m4=1, m5=0, m6=0, m7=0, m8=1
        # Rotated 90 deg around Y: m0=0, m1=0, m2=-1, m3=0, m4=1, m5=0, m6=1, m7=0, m8=0
        if abs(p['m0']) < 0.1 and abs(p['m2']) > 0.9:
            pw, pd = pd, pw

        half_w = (pw * 20) / 2
        half_d = (pd * 20) / 2

        px_min = p['x'] - half_w
        px_max = p['x'] + half_w
        pz_min = p['z'] - half_d
        pz_max = p['z'] + half_d

        min_x = min(min_x, px_min)
        max_x = max(max_x, px_max)
        min_z = min(min_z, pz_min)
        max_z = max(max_z, pz_max)

        processed_parts.append({
            'color': p['color'],
            'y': p['y'],
            'x_min': px_min,
            'x_max': px_max,
            'z_min': pz_min,
            'z_max': pz_max,
            'pw': pw,
            'pd': pd,
            'part': p['part']
        })

    # Sort by Y descending (bottom to top).
    # In this project, smaller Y is higher.
    processed_parts.sort(key=lambda p: p['y'], reverse=True)

    # Scale for image
    scale = 4.0  # pixels per LDU (Increased for better detail)
    margin = 40 # pixels

    # Standard cell height is 300 LDU (15 studs)
    render_min_z = 0
    render_max_z = 300
    render_min_x = 0
    render_max_x = max(160, max_x) # Most small cells are up to 160 LDU

    img_w = int((render_max_x - render_min_x) * scale) + 2 * margin
    img_h = int((render_max_z - render_min_z) * scale) + 2 * margin

    img = Image.new('RGB', (img_w, img_h), (18, 18, 18))
    draw = ImageDraw.Draw(img)

    def to_img_coords(x, z):
        ix = int((x - render_min_x) * scale) + margin
        # Flip Z so high Z is at top
        iz = int((render_max_z - z) * scale) + margin
        return ix, iz

    for p in processed_parts:
        color = COLOR_RGB.get(p['color'], (128, 128, 128))
        # Need to re-map for top view with flipped Z
        # top-left of rectangle in image is (x_min, z_max) in LDU if Z is flipped
        ix1, iz1 = to_img_coords(p['x_min'], p['z_max'])
        ix2, iz2 = to_img_coords(p['x_max'], p['z_min'])

        # Draw the part body
        draw.rectangle([ix1, iz1, ix2, iz2], fill=color, outline=(0, 0, 0), width=1)

        # Draw studs if it's not a tile
        if p['part'] not in ['3070.dat']:
            stud_radius = 6 * scale / 2

            for i in range(int(round(p['pw']))):
                for j in range(int(round(p['pd']))):
                    sx_ldu = p['x_min'] + 10 + i * 20
                    sz_ldu = p['z_min'] + 10 + j * 20

                    sx, sz = to_img_coords(sx_ldu, sz_ldu)

                    # Main stud circle
                    draw.ellipse([sx - stud_radius, sz - stud_radius, sx + stud_radius, sz + stud_radius],
                                 fill=color, outline=(int(color[0]*0.7), int(color[1]*0.7), int(color[2]*0.7)), width=1)

                    # Highlight for 3D effect
                    h_rad = stud_radius * 0.6
                    draw.ellipse([sx - h_rad, sz - h_rad, sx - 1, sz - 1], fill=(int(min(255, color[0]*1.3)), int(min(255, color[1]*1.3)), int(min(255, color[2]*1.3))))

    if output_path:
        img.save(output_path)
        print(f"Rendered to {output_path}")
    return img

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python render_ldr_top.py <input.ldr> <output.png> [limit_step]")
    else:
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else None
        render(sys.argv[1], sys.argv[2], limit_step=limit)
