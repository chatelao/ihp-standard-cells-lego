import os
import re

def add_steps(ldr_path):
    with open(ldr_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    step_added = False

    # Simple logic: add a STEP after each comment block that starts a new section
    # and before that section's parts.
    # In lef_to_ldr.py, sections are: Substrate low, Substrate high, Pin X, Obstructions

    for i, line in enumerate(lines):
        # If line starts with 0 // and it's not the first one, consider adding a STEP before it
        if line.startswith("0 //"):
            # Check if there was any actual content (type 1 lines) before this
            has_content_before = any(l.strip().startswith("1 ") for l in new_lines)
            if has_content_before:
                new_lines.append("0 STEP\n")

        new_lines.append(line)

    with open(ldr_path, 'w') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    models_dir = "models"
    for filename in os.listdir(models_dir):
        if filename.endswith(".ldr"):
            add_steps(os.path.join(models_dir, filename))
