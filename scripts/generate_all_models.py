import os
import subprocess

def main():
    celllist_path = 'specifications/sg13g2_stdcell.celllist'
    lef_path = 'specifications/sg13g2_stdcell.lef'
    script_path = 'scripts/lef_to_ldr.py'

    if not os.path.exists(celllist_path):
        print(f"Error: Cell list not found at {celllist_path}")
        return

    with open(celllist_path, 'r') as f:
        cells = [line.strip() for line in f if line.strip()]

    print(f"Found {len(cells)} cells. Starting generation...")

    for cell in cells:
        print(f"Generating {cell}...")
        try:
            subprocess.run(['python3', script_path, lef_path, cell], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error generating {cell}: {e}")

    print("Generation complete.")

if __name__ == "__main__":
    main()
