import os
import shutil
import re
import sys

def collect_parts(models_dir, ldraw_dir, output_dir):
    """
    Recursively collects parts and primitives used in LDR models.
    """
    used_parts = set()
    to_process = set()

    if not os.path.exists(models_dir):
        print(f"Models directory {models_dir} not found.")
        return

    # 1. Find initial parts from models
    for ldr_file in os.listdir(models_dir):
        if ldr_file.endswith('.ldr'):
            with open(os.path.join(models_dir, ldr_file), 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('1 '):
                        parts = line.split()
                        if len(parts) > 14:
                            part = parts[-1].lower().replace('\\', '/')
                            to_process.add(part)

    print(f"Initial parts found: {len(to_process)}")

    # 1.5 Find and copy LDConfig.ldr
    ldconfig_paths = [
        os.path.join(ldraw_dir, 'LDConfig.ldr'),
        os.path.join(ldraw_dir, 'Config/LDConfig.ldr'),
    ]
    for p in ldconfig_paths:
        if os.path.exists(p):
            print(f"Copying {p} to {output_dir}")
            shutil.copy2(p, os.path.join(output_dir, 'LDConfig.ldr'))
            break
    else:
        print("Warning: LDConfig.ldr not found in LDraw directory.")

    # 2. Process dependencies recursively
    processed = set()
    while to_process:
        part = to_process.pop()
        if part in processed:
            continue
        processed.add(part)

        found = False
        # Try finding in parts/ and p/
        for subdir in ['parts', 'p']:
            part_path = os.path.join(ldraw_dir, subdir, part)
            if os.path.exists(part_path):
                found = True
                # Copy to output
                out_path = os.path.join(output_dir, subdir, part)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                shutil.copy2(part_path, out_path)

                # Check for dependencies
                try:
                    with open(part_path, 'r', encoding='latin-1') as f:
                        for line in f:
                            if line.startswith('1 '):
                                parts = line.split()
                                if len(parts) > 14:
                                    dep = parts[-1].lower().replace('\\', '/')
                                    if dep not in processed:
                                        to_process.add(dep)
                except Exception as e:
                    print(f"Error reading {part_path}: {e}")
                break

        if not found:
            # Maybe it's a relative path within the library or just missing
            pass

    print(f"Total parts collected: {len(processed)}")

if __name__ == "__main__":
    models_dir = 'models'
    ldraw_dir = '/usr/share/ldraw'
    output_dir = 'ldraw_lib'

    if len(sys.argv) > 1:
        ldraw_dir = sys.argv[1]
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]

    collect_parts(models_dir, ldraw_dir, output_dir)
