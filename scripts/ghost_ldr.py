import sys
import os
import re

# Mapping of solid LDraw color IDs to their transparent equivalents
# Based on LDConfig.ldr from the official library
GHOST_MAP = {
    0: 32,     # Black -> Trans-Black (IR Lens)
    1: 41,     # Blue -> Trans-Medium-Blue
    4: 36,     # Red -> Trans-Red
    7: 47,     # Light Grey -> Trans-Clear
    8: 40,     # Dark Grey -> Trans-Brown (greyish transparent)
    9: 43,     # Light Blue -> Trans-Light-Blue
    14: 46,    # Yellow -> Trans-Yellow
    15: 47,    # White -> Trans-Clear
    38: 57,    # Trans-Neon-Orange (used for PMOS) -> Trans-Orange
    272: 33,   # Dark Blue -> Trans-Dark-Blue
    288: 34,   # Dark Green -> Trans-Green
    484: 57,   # Dark Orange -> Trans-Orange
}

FALLBACK_COLOR = 47 # Trans-Clear

def ghost_ldr(input_path, output_path, target_step):
    """
    Reads an LDR file and writes a new one where all parts in steps
    BEFORE target_step are mapped to transparent colors.
    target_step is 1-indexed.
    """
    with open(input_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    current_step = 1

    # Regex to match type 1 lines (parts): 1 <color> <x> <y> <z> ...
    part_re = re.compile(r'^(1\s+)(\d+)(\s+.*)$')

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('0 STEP'):
            current_step += 1
            new_lines.append(line)
            continue

        # If we are in a step before the target step, map colors
        if current_step < target_step:
            match = part_re.match(line)
            if match:
                prefix, color_str, suffix = match.groups()
                color_id = int(color_str)
                new_color = GHOST_MAP.get(color_id, FALLBACK_COLOR)
                new_lines.append(f"{prefix}{new_color}{suffix}\n")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(output_path, 'w') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python ghost_ldr.py <input_ldr> <output_ldr> <target_step>")
        sys.exit(1)

    input_ldr = sys.argv[1]
    output_ldr = sys.argv[2]
    target_step = int(sys.argv[3])

    if not os.path.exists(input_ldr):
        print(f"Error: {input_ldr} not found")
        sys.exit(1)

    ghost_ldr(input_ldr, output_ldr, target_step)
    print(f"Ghosted {input_ldr} up to step {target_step-1} -> {output_ldr}")
