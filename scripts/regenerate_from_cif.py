import os
import subprocess

celllist_path = 'specifications/sg13g2_stdcell.celllist'
cif_to_ldr_script = 'scripts/cif_to_ldr.py'

with open(celllist_path, 'r') as f:
    cells = [line.strip() for line in f if line.strip()]

for cell in cells:
    cif_path = f"specifications/cells/{cell}.cif"
    if os.path.exists(cif_path):
        subprocess.run(['python3', cif_to_ldr_script, cif_path], check=True)
