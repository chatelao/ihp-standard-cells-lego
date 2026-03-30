import os
import sys
from PIL import Image, ImageDraw, ImageFont
import re

# Add scripts directory to path for importing render_ldr_top
sys.path.append(os.path.dirname(__file__))
import render_ldr_top

def get_step_count(ldr_path):
    with open(ldr_path, 'r') as f:
        content = f.read()
    return content.count('0 STEP')

def generate_montage(cell_name, models_dir, output_dir):
    ldr_path = os.path.join(models_dir, f"{cell_name}.ldr")
    if not os.path.exists(ldr_path):
        return False

    num_steps = get_step_count(ldr_path)
    total_passes = num_steps + 1

    images = []
    for step in range(1, total_passes + 1):
        img = render_ldr_top.render(ldr_path, limit_step=step)
        if img:
            # Add step label to the image
            draw = ImageDraw.Draw(img)
            try:
                # Try to use a font if available, else default
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 20)
            except:
                font = ImageFont.load_default()

            label = f"Pass {step}"
            draw.text((10, 10), label, fill=(255, 255, 255), font=font)
            images.append(img)

    if not images:
        return False

    # Create montage grid
    # Determine grid size (cols, rows)
    cols = 4
    rows = (len(images) + cols - 1) // cols

    img_w, img_h = images[0].size
    montage = Image.new('RGB', (img_w * cols, img_h * rows), (30, 30, 30))

    for i, img in enumerate(images):
        c = i % cols
        r = i // cols
        montage.paste(img, (c * img_w, r * img_h))

    output_path = os.path.join(output_dir, f"{cell_name}_construction.png")
    montage.save(output_path)
    return True

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--cell', help='Process only a specific cell')
    args = parser.parse_args()

    models_dir = 'models'
    output_dir = 'images'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if args.cell:
        model_files = [f"{args.cell}.ldr"]
    else:
        model_files = sorted([f_ for f_ in os.listdir(models_dir) if f_.endswith('.ldr')])

    print(f"Generating construction montages for {len(model_files)} cells...")
    for f in model_files:
        cell_name = os.path.splitext(f)[0]
        if generate_montage(cell_name, models_dir, output_dir):
            print(f"  Generated {cell_name}_construction.png")
        else:
            print(f"  Skipped {cell_name} (no steps found)")

if __name__ == "__main__":
    main()
