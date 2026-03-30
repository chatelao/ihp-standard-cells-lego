import os
import sys

# Add scripts directory to path for importing render_ldr_top
sys.path.append(os.path.dirname(__file__))
import render_ldr_top

def main():
    models_dir = 'models'
    images_dir = 'images'

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    model_files = sorted([f for f in os.listdir(models_dir) if f.endswith('.ldr')])

    print(f"Generating top-down images for {len(model_files)} cells...")
    for f in model_files:
        name = os.path.splitext(f)[0]
        ldr_path = os.path.join(models_dir, f)
        output_path = os.path.join(images_dir, f"{name}_top.png")

        print(f"  Rendering {name}_top.png...")
        render_ldr_top.render(ldr_path, output_path)

if __name__ == "__main__":
    main()
