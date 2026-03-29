import os
from PIL import Image

def generate_comparison_image(name, images_dir, lef_dir, output_dir):
    lego_path = os.path.join(images_dir, f"{name}_top.jpg")
    lef_path = os.path.join(lef_dir, f"{name}.png")
    output_path = os.path.join(output_dir, f"{name}_compare.jpg")

    if not os.path.exists(lego_path) or not os.path.exists(lef_path):
        return False

    try:
        lego_img = Image.open(lego_path)
        lef_img = Image.open(lef_path)

        # Set target height
        target_height = 800

        # Resize both images to target height while maintaining aspect ratio
        def resize_to_height(img, height):
            w, h = img.size
            aspect = w / h
            new_w = int(height * aspect)
            return img.resize((new_w, height), Image.Resampling.LANCZOS)

        lego_resized = resize_to_height(lego_img, target_height)
        lef_resized = resize_to_height(lef_img, target_height)

        # Stitch horizontally
        total_width = lego_resized.width + lef_resized.width + 20 # 20px gap
        combined_img = Image.new('RGB', (total_width, target_height), (18, 18, 18)) # Background color #121212 in RGB is (18, 18, 18)

        combined_img.paste(lego_resized, (0, 0))
        combined_img.paste(lef_resized, (lego_resized.width + 20, 0))

        combined_img.save(output_path, quality=90)
        return True
    except Exception as e:
        print(f"Error processing {name}: {e}")
        return False

def main():
    images_dir = 'images'
    lef_dir = 'specifications/png'
    output_dir = 'images'
    models_dir = 'models'

    if not os.path.exists(images_dir):
        print(f"Directory {images_dir} does not exist.")
        return

    # Process all models
    model_names = [os.path.splitext(f)[0] for f in os.listdir(models_dir) if f.endswith('.ldr')]

    # Also include test cases if any
    for name in model_names:
        if generate_comparison_image(name, images_dir, lef_dir, output_dir):
            print(f"Generated comparison for {name}")

if __name__ == "__main__":
    main()
