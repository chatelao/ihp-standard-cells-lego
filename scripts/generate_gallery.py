import os

def generate_gallery():
    models_dir = 'models'
    images_dir = 'images'
    output_file = 'index.html'

    models = [f[:-4] for f in os.listdir(models_dir) if f.endswith('.ldr')]
    models.sort()

    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IHP Standard Cells LEGO Models</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        .card { margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .card-title { font-size: 1.1rem; font-weight: bold; }
        video { max-width: 100%; height: auto; border-radius: 4px; }
        .gallery-item { transition: transform 0.2s; }
        .gallery-item:hover { transform: scale(1.02); }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark bg-dark mb-4">
        <div class="container">
            <span class="navbar-brand mb-0 h1">IHP Standard Cells LEGO Models Gallery</span>
        </div>
    </nav>
    <div class="container">
        <div class="row">
    """

    for model in models:
        img_path = f"{images_dir}/{model}.jpg"
        video_path = f"{images_dir}/{model}.mp4"

        html_content += f"""
            <div class="col-md-6 col-lg-4 gallery-item">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title text-center">{model}</h5>
        """

        if os.path.exists(video_path):
            html_content += f"""
                        <video autoplay loop muted playsinline>
                            <source src="{video_path}" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
            """
        elif os.path.exists(img_path):
            html_content += f"""
                        <img src="{img_path}" class="img-fluid rounded" alt="{model}">
            """
        else:
            html_content += f"""
                        <div class="alert alert-warning">No image/video available</div>
            """

        html_content += """
                    </div>
                </div>
            </div>
        """

    html_content += """
        </div>
    </div>
    <footer class="text-center py-4 text-muted">
        <p>Generated automatically by GitHub Actions</p>
    </footer>
</body>
</html>
    """

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_gallery()
