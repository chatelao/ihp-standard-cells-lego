import os
import re

def migrate_ldr(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    new_lines = []
    substrate_plates = []

    for line in lines:
        # Match LDraw Type 1 line: 1 <color> <x> <y> <z> <m0> <m1> <m2> <m3> <m4> <m5> <m6> <m7> <m8> <part>
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+(.*)', line)
        if match:
            color = int(match.group(1))
            x = float(match.group(2))
            y = float(match.group(3))
            z = float(match.group(4))
            rest = match.group(5)

            new_color = color
            new_y = y

            # 1. Substrate and N-Well
            if y == 0 and color in [7, 19]:
                # Collect for duplication to Y=0
                substrate_plates.append((x, 0, z, rest))

                new_y = -8
                if color == 7: # Was Substrate
                    new_color = 8 # Substrate high (Dark Gray)
                elif color == 19: # Was N-Well (Tan)
                    new_color = 7 # N-Well (Light Gray)

            # 2. Diffusion (Active)
            elif y == -8 and color == 38:
                new_y = -16
                if z < 80:
                    new_color = 288 # Diffusion NMOS (Dark Green)
                else:
                    new_color = 25 # Diffusion PMOS (Orange)

            # 3. Polysilicon
            elif y == -16 and color == 4:
                new_y = -24
                new_color = 4

            # 4. Metal 1
            elif y == -16 and color == 1:
                new_y = -16
                new_color = 1

            # 5. Rails (already at -8)
            elif y == -8 and color in [14, 0]:
                new_y = -8
                new_color = color

            # 6. Metal 2 (if any, V1 didn't have much)
            elif y == -24 and color == 2:
                new_y = -24
                new_color = 2

            new_line = f"1 {new_color} {x} {new_y} {z} {rest}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # Add Substrate low (Dark Gray 8) at Y=0
    # We'll insert them after the header or at the beginning of the model part
    substrate_low_lines = []
    for x, y, z, rest in substrate_plates:
        substrate_low_lines.append(f"1 8 {x} 0 {z} {rest}\n")

    # Find a good place to insert. After the first few comments.
    insert_idx = 0
    for i, line in enumerate(new_lines):
        if line.startswith('1 '):
            insert_idx = i
            break

    final_lines = new_lines[:insert_idx] + ["0 // Substrate low (V2)\n"] + substrate_low_lines + new_lines[insert_idx:]

    with open(filepath, 'w') as f:
        f.writelines(final_lines)

def main():
    models_dir = 'models'
    for filename in os.listdir(models_dir):
        if filename.endswith('.ldr'):
            print(f"Migrating {filename}...")
            migrate_ldr(os.path.join(models_dir, filename))

if __name__ == "__main__":
    main()
