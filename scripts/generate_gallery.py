import os
import re

def parse_pdk_links(md_file):
    pdk_links = {}
    if not os.path.exists(md_file):
        return pdk_links

    with open(md_file, 'r') as f:
        content = f.read()
        # Regex to match [cell_name](url)
        matches = re.findall(r'\[(sg13g2_[a-z0-9_]+)\]\((https?://[^\)]+)\)', content)
        for name, url in matches:
            # Extract cell type from URL: .../cells/{cell_type}/README.html
            match = re.search(r'/cells/([^/]+)/README\.html', url)
            if match:
                cell_type = match.group(1)
                # Append anchor for GDSII layouts
                url = f"{url}#sky130-fd-sc-hd-{cell_type}-gdsii-layouts"
            pdk_links[name] = url
    return pdk_links

def generate_gallery():
    image_dir = 'images'
    instructions_dir = 'instructions'
    models_dir = 'models'
    spec_file = 'specifications/sg13g2_stdcell_details.md'
    pdk_spec_file = 'specifications/sg13g2_stdcell.md'

    pdk_links = parse_pdk_links(pdk_spec_file)

    if not os.path.exists(models_dir):
        print(f"Directory {models_dir} does not exist.")
        return

    model_files = sorted([f for f in os.listdir(models_dir) if f.endswith('.ldr')])

    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Standard Cell LEGO Gallery</title>
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            color: #bb86fc;
            margin-bottom: 30px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
            width: 100%;
            max-width: 1400px;
        }
        .card {
            background-color: #1e1e1e;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
        }
        .view-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2px;
            background-color: #1a1a1a;
        }
        .view-grid img {
            width: 100%;
            aspect-ratio: 4 / 3;
            object-fit: cover;
            display: block;
        }
        .placeholder {
            aspect-ratio: 4 / 3;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #2a2a2a;
            color: #555;
            font-size: 0.7rem;
            text-align: center;
            padding: 5px;
        }
        .card-content {
            padding: 20px;
            background-color: #252525;
        }
        .card-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: #03dac6;
            margin-bottom: 10px;
        }
        .card-links {
            display: flex;
            gap: 15px;
            font-size: 0.9rem;
        }
        .card-links a {
            color: #bb86fc;
            text-decoration: none;
        }
        .card-links a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 50px;
            color: #777;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <h1>Standard Cell LEGO Gallery</h1>
    <div class="gallery">
"""

    for ldr_file in model_files:
        name = os.path.splitext(ldr_file)[0]

        views = [
            {'suffix': '', 'label': 'Perspective'},
            {'suffix': '_top', 'label': 'Top'},
            {'suffix': '_front', 'label': 'Front'},
            {'suffix': '_side', 'label': 'Side'},
            {'suffix': '_top_angled', 'label': 'Top Angled'},
            {'suffix': '_side_angled', 'label': 'Side Angled'}
        ]

        html_content += f'        <div class="card">\n'
        html_content += f'            <div class="view-grid">\n'

        for i, view in enumerate(views):
            jpg_name = f"{name}{view['suffix']}.jpg"
            has_jpg = os.path.exists(os.path.join(image_dir, jpg_name))

            if has_jpg:
                html_content += f'                <img src="{image_dir}/{jpg_name}" alt="{name} {view["label"]}">\n'
            else:
                html_content += f'                <div class="placeholder">{view["label"]}<br>pending</div>\n'

        html_content += f'            </div>\n'
        html_content += f'            <div class="card-content">\n'
        html_content += f'                <div class="card-title">{name}</div>\n'
        html_content += f'                <div class="card-links">\n'
        html_content += f'                    <a href="viewer.html?model={name}" target="_blank" style="color: #03dac6; font-weight: bold;">3D</a>\n'
        html_content += f'                    <a href="models/{ldr_file}" target="_blank">LDR</a>\n'
        if os.path.exists(os.path.join(image_dir, f"{name}.jpg")):
            html_content += f'                    <a href="images/{name}.jpg" target="_blank">JPG</a>\n'
        if os.path.exists(os.path.join(instructions_dir, f"{name}.pdf")):
            html_content += f'                    <a href="instructions/{name}.pdf" target="_blank">PDF</a>\n'
        else:
            html_content += f'                    <span title="Instructions rendering pending" style="color: #555; cursor: help;">PDF</span>\n'
        html_content += f'                    <a href="{spec_file}#{name}" target="_blank">Spec</a>\n'
        if name in pdk_links:
            html_content += f'                    <a href="{pdk_links[name]}" target="_blank">PDK</a>\n'
        html_content += f'                </div>\n'
        html_content += f'            </div>\n'
        html_content += f'        </div>\n'

    html_content += """
    </div>
    <footer>
        <p>Generated by GEMINI Automation</p>
    </footer>
</body>
</html>
"""

    with open('index.html', 'w') as f:
        f.write(html_content)
    print("Gallery generated successfully in index.html")

if __name__ == "__main__":
    generate_gallery()
