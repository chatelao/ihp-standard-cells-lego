import os
import subprocess

def main():
    celllist_path = 'specifications/sg13g2_stdcell.celllist'
    lef_path = 'specifications/sg13g2_stdcell.lef'
    lef_to_ldr_script = 'scripts/lef_to_ldr.py'
    gen_design_docs_script = 'scripts/generate_design_docs.py'
    design_to_ldr_script = 'scripts/design_to_ldr.py'
    gen_construction_script = 'scripts/generate_construction_images.py'
    gen_top_images_script = 'scripts/generate_top_images.py'
    gen_gallery_script = 'scripts/generate_gallery.py'

    if not os.path.exists(celllist_path):
        print(f"Error: Cell list not found at {celllist_path}")
        return

    with open(celllist_path, 'r') as f:
        cells = [line.strip() for line in f if line.strip()]

    print(f"Found {len(cells)} cells. Starting initial LDR generation from LEF...")
    for cell in cells:
        print(f"  Generating {cell}...")
        try:
            subprocess.run(['python3', lef_to_ldr_script, lef_path, cell], check=True)
        except subprocess.CalledProcessError as e:
            print(f"  Error generating {cell} from LEF: {e}")

    print("Step 2: Generating design documentation (preserving GOLDEN STANDARDs)...")
    try:
        subprocess.run(['python3', gen_design_docs_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {gen_design_docs_script}: {e}")

    print("Step 3: Propagating design documentation back to LDR models...")
    try:
        subprocess.run(['python3', design_to_ldr_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {design_to_ldr_script}: {e}")

    print("Step 3.5: Generating construction pass images...")
    try:
        subprocess.run(['python3', gen_construction_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {gen_construction_script}: {e}")

    print("Step 3.6: Generating top-down images...")
    try:
        subprocess.run(['python3', gen_top_images_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {gen_top_images_script}: {e}")

    print("Step 4: Updating the HTML gallery...")
    try:
        subprocess.run(['python3', gen_gallery_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {gen_gallery_script}: {e}")

    print("Generation chain complete.")

if __name__ == "__main__":
    main()
