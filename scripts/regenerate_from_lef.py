import os
import subprocess

celllist_path = 'specifications/sg13g2_stdcell.celllist'
lef_path = 'specifications/sg13g2_stdcell.lef'
lef_to_ldr_script = 'scripts/lef_to_ldr.py'

with open(celllist_path, 'r') as f:
    cells = [line.strip() for line in f if line.strip()]

for cell in cells:
    subprocess.run(['python3', lef_to_ldr_script, lef_path, cell], check=True)
