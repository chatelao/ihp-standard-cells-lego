import sys
import os
from PIL import Image, ImageDraw, ImageFont

# LDraw Color ID to Name mapping (V3)
COLOR_MAP = {
    8: 'Substrate (DG)',
    7: 'N-Well (LG)',
    288: 'NMOS (DG)',
    38: 'PMOS (DO)',
    4: 'Poly (Red)',
    9: 'M1 Input (LB)',
    1: 'M1 Conn (Blue)',
    272: 'M1 Output (DB)',
    14: 'VDD (Yellow)',
    0: 'VSS (Black)',
    15: 'Contact (White)',
}

# LDraw Part ID to Name mapping
PART_MAP = {
    '3034.dat': 'Plate 2x8',
    '3460.dat': 'Plate 1x8',
    '3666.dat': 'Plate 1x6',
    '3020.dat': 'Plate 2x4',
    '3710.dat': 'Plate 1x4',
    '3623.dat': 'Plate 1x3',
    '3022.dat': 'Plate 2x2',
    '3023.dat': 'Plate 1x2',
    '3024.dat': 'Plate 1x1',
    '6141.dat': 'Plate 1x1 Round',
    '3062b.dat': 'Brick 1x1 Round',
}

def parse_ldr_step(ldr_path, step_num):
    """
    Parses the LDR file and returns a dictionary of parts added in the specified step.
    step_num is 1-indexed.
    """
    with open(ldr_path, 'r') as f:
        lines = f.readlines()

    current_step = 1
    parts_in_step = {}

    for line in lines:
        line = line.strip()
        if line.startswith('0 STEP'):
            current_step += 1
            if current_step > step_num:
                break
            continue

        if current_step == step_num and line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                color_id = int(tokens[1])
                part_id = tokens[14].lower()

                key = (color_id, part_id)
                parts_in_step[key] = parts_in_step.get(key, 0) + 1

    return parts_in_step

def annotate_image(image_path, parts_in_step):
    if not parts_in_step:
        return

    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image {image_path}: {e}")
        return

    draw = ImageDraw.Draw(img)

    # Try to load a font, fallback to default
    try:
        # Using DejaVuSansMono as it was found in the environment
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 18)
    except:
        font = ImageFont.load_default()
        header_font = ImageFont.load_default()

    # Prepare text
    lines = ["Parts Needed:"]
    for (color_id, part_id), count in sorted(parts_in_step.items()):
        color_name = COLOR_MAP.get(color_id, f"Color {color_id}")
        part_name = PART_MAP.get(part_id, part_id)
        lines.append(f"{count}x {part_name} ({color_name})")

    # Calculate box size
    line_height = 20
    max_width = 0
    for line in lines:
        # Use getbbox instead of deprecated getsize
        bbox = draw.textbbox((0, 0), line, font=font if line != "Parts Needed:" else header_font)
        w = bbox[2] - bbox[0]
        max_width = max(max_width, w)

    padding = 10
    box_width = max_width + 2 * padding
    box_height = len(lines) * line_height + 2 * padding

    # Draw box
    draw.rectangle([10, 10, 10 + box_width, 10 + box_height], fill=(255, 255, 255, 200), outline=(0, 0, 0))

    # Draw text
    y = 10 + padding
    for i, line in enumerate(lines):
        f = header_font if i == 0 else font
        draw.text((10 + padding, y), line, fill=(0, 0, 0), font=f)
        y += line_height

    img.save(image_path)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python annotate_step.py <ldr_file> <step_num> <image_file>")
        sys.exit(1)

    ldr_file = sys.argv[1]
    step_num = int(sys.argv[2])
    image_file = sys.argv[3]

    if not os.path.exists(ldr_file):
        print(f"Error: LDR file {ldr_file} not found.")
        sys.exit(1)

    if not os.path.exists(image_file):
        print(f"Error: Image file {image_file} not found.")
        sys.exit(1)

    parts = parse_ldr_step(ldr_file, step_num)
    annotate_image(image_file, parts)
    print(f"Annotated step {step_num} of {ldr_file} on {image_file}")
