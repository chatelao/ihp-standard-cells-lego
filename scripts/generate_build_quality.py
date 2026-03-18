import os
import re

PART_DIMENSIONS = {
    '91405.dat': (16, 16),
    '92438.dat': (16, 8),
    '3027.dat': (16, 6),
    '3456.dat': (14, 6),
    '3028.dat': (12, 6),
    '3033.dat': (10, 6),
    '3029.dat': (12, 4),
    '3036.dat': (8, 6),
    '3030.dat': (10, 4),
    '3958.dat': (6, 6),
    '4282.dat': (16, 2),
    '3035.dat': (8, 4),
    '2445.dat': (12, 2),
    '3032.dat': (6, 4),
    '3832.dat': (10, 2),
    '3034.dat': (8, 2),
    '3031.dat': (4, 4),
    '60479.dat': (12, 1),
    '3795.dat': (6, 2),
    '4477.dat': (10, 1),
    '3460.dat': (8, 1),
    '3020.dat': (4, 2),
    '3666.dat': (6, 1),
    '3021.dat': (3, 2),
    '3710.dat': (4, 1),
    '3022.dat': (2, 2),
    '3623.dat': (3, 1),
    '3023.dat': (2, 1),
    '3024.dat': (1, 1),
    '6141.dat': (1, 1),
    '3062b.dat': (1, 1),
}

def analyze_ldr(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    layers = {0: [], -8: [], -16: []}
    for line in lines:
        if line.startswith('1 '):
            tokens = line.split()
            if len(tokens) >= 15:
                y = int(float(tokens[3]))
                if y in layers:
                    part = tokens[14].lower()
                    rot = [float(t) for t in tokens[5:14]]
                    layers[y].append({'part': part, 'rot': rot})

    results = {}
    for y, parts in layers.items():
        if not parts:
            results[y] = {'count': 0, 'area': 0, 'avg_size': 0, 'rotated_pct': 0}
            continue

        total_area = 0
        rotated_count = 0
        for p in parts:
            pw, pd = PART_DIMENSIONS.get(p['part'], (1, 1))
            total_area += pw * pd
            if p['rot'][0] == 0: # Z-aligned
                rotated_count += 1

        results[y] = {
            'count': len(parts),
            'area': total_area,
            'avg_size': total_area / len(parts),
            'rotated_pct': (rotated_count / len(parts)) * 100
        }

    return results

def main():
    models_dir = 'models'
    output_file = 'BUILD_QUALITY.md'

    if not os.path.exists(models_dir):
        print(f"Error: {models_dir} not found")
        return

    cell_data = []
    for filename in sorted(os.listdir(models_dir)):
        if filename.endswith('.ldr'):
            cell_name = filename[:-4]
            stats = analyze_ldr(os.path.join(models_dir, filename))
            cell_data.append((cell_name, stats))

    with open(output_file, 'w') as f:
        f.write("# Build Quality Assessment\n\n")
        f.write("This report evaluates the stability of the 3 base layers (Substrate Low, Substrate High, and Active) for each library cell.\n\n")
        f.write("## Stability Metrics\n")
        f.write("- **Avg Size**: Average studs per plate in that layer (higher is better).\n")
        f.write("- **Interlocking**: A 'Yes' indicates that Layer 1 (Substrate Low) and Layer 2 (Substrate High) use perpendicular plate orientations to increase structural integrity.\n")
        f.write("- **Overall Score**: Weighted average of sizes, with a bonus for interlocking.\n\n")

        f.write("| Cell Name | L1 Avg Size | L2 Avg Size | L3 Avg Size | Interlocking | Stability Score |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: |\n")

        for name, stats in cell_data:
            s0 = stats[0]['avg_size']
            s8 = stats[-8]['avg_size']
            s16 = stats[-16]['avg_size']

            # Interlocking check: L1 should be mostly rotated, L2 should be mostly non-rotated
            interlocking = stats[0]['rotated_pct'] > 70 and stats[-8]['rotated_pct'] < 30

            areas = [s for s in [s0, s8, s16] if s > 0]
            base_score = sum(areas) / len(areas) if areas else 0

            # 20% bonus for interlocking
            final_score = base_score * (1.2 if interlocking else 1.0)

            def format_score(s):
                if s == 0: return "-"
                return f"{s:.1f}"

            f.write(f"| {name} | {format_score(s0)} | {format_score(s8)} | {format_score(s16)} | {'Yes' if interlocking else 'No'} | {final_score:.1f} |\n")

    print(f"Generated {output_file}")

if __name__ == '__main__':
    main()
