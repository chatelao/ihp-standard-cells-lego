#!/bin/bash
set -e
shopt -s nullglob

LDVIEW_BIN="ldview"
LDRAW_DIR="/usr/share/ldraw"
OUTPUT_DIR="$(pwd)/images"
INSTRUCTIONS_DIR="$(pwd)/instructions"
MODELS_DIR="$(pwd)/models"
LOG_FILE="$(pwd)/ldview_render.log"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$INSTRUCTIONS_DIR"
# We don't want to delete images if we are incrementally building,
# but for a clean state in the sandbox, it's okay.
# However, memory says it's cleared before rendering.
rm -f "$OUTPUT_DIR"/*.jpg
rm -f "$INSTRUCTIONS_DIR"/*.pdf

render_with_retry() {
    local output="$1"
    local params="$2"
    local file="$3"
    local max_attempts=3
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        if "$LDVIEW_BIN" -SaveSnapshot="$output" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" $params "$file" > "$LOG_FILE" 2>&1; then
            return 0
        else
            echo "    Attempt $attempt failed for $(basename "$output")"
            attempt=$((attempt + 1))
            sleep 1
        fi
    done
    return 1
}

for file in "$MODELS_DIR"/*.ldr; do
    filename=$(basename "$file" .ldr)
    echo "Processing $filename..."

    # 1. Perspective image
    echo "  Rendering perspective image..."
    render_with_retry "$OUTPUT_DIR/${filename}.jpg" "-DefaultCamera" "$file" || echo "  Error: Failed to render perspective image"

    # 2. Top image
    echo "  Rendering top image..."
    render_with_retry "$OUTPUT_DIR/${filename}_top.jpg" "-UseCamera=0 -Latitude=90 -Longitude=0" "$file" || echo "  Error: Failed to render top image"

    # 3. Front image
    echo "  Rendering front image..."
    render_with_retry "$OUTPUT_DIR/${filename}_front.jpg" "-UseCamera=0 -Latitude=0 -Longitude=0" "$file" || echo "  Error: Failed to render front image"

    # 4. Side image
    echo "  Rendering side image..."
    render_with_retry "$OUTPUT_DIR/${filename}_side.jpg" "-UseCamera=0 -Latitude=0 -Longitude=90" "$file" || echo "  Error: Failed to render side image"

    # 5. Top-Down Angled
    echo "  Rendering top-down angled image..."
    render_with_retry "$OUTPUT_DIR/${filename}_top_angled.jpg" "-UseCamera=0 -Latitude=45 -Longitude=45" "$file" || echo "  Error: Failed to render top-down angled image"

    # 6. Side Angled
    echo "  Rendering side angled image..."
    render_with_retry "$OUTPUT_DIR/${filename}_side_angled.jpg" "-UseCamera=0 -Latitude=20 -Longitude=135" "$file" || echo "  Error: Failed to render side angled image"

    # 7. Bottom image
    echo "  Rendering bottom image..."
    render_with_retry "$OUTPUT_DIR/${filename}_bottom.jpg" "-UseCamera=0 -Latitude=-90 -Longitude=0" "$file" || echo "  Error: Failed to render bottom image"

    # 8. Back image
    echo "  Rendering back image..."
    render_with_retry "$OUTPUT_DIR/${filename}_back.jpg" "-UseCamera=0 -Latitude=0 -Longitude=180" "$file" || echo "  Error: Failed to render back image"

    # Verify static images (basic check)
    for suffix in "" "_top" "_front" "_side" "_top_angled" "_side_angled" "_bottom" "_back"; do
        if [ ! -f "$OUTPUT_DIR/${filename}${suffix}.jpg" ]; then
            echo "  Warning: Image file ${filename}${suffix}.jpg not found after rendering attempts"
        fi
    done

    # Building instructions PDF (Optional, depends on img2pdf presence)
    if command -v img2pdf >/dev/null 2>&1; then
        echo "  Generating building instructions..."
        TEMP_STEP_DIR="$(pwd)/temp_steps_${filename}"
        mkdir -p "$TEMP_STEP_DIR"

        # Count steps
        num_steps=$(grep -c "0 STEP" "$file" || true)
        total_steps=$((num_steps + 1))

        step_images=()
        for (( s=1; s<=total_steps; s++ )); do
            step_img="$TEMP_STEP_DIR/step_${s}.jpg"
            if render_with_retry "$step_img" "-Step=$s" "$file"; then
                step_images+=("$step_img")
            else
                echo "    Error: Failed to render step $s for $filename"
            fi
        done

        if [ ${#step_images[@]} -gt 0 ]; then
            img2pdf "${step_images[@]}" --output "$INSTRUCTIONS_DIR/${filename}.pdf"
        fi
        rm -rf "$TEMP_STEP_DIR"
    fi

done

rm -f "$LOG_FILE"
echo "Rendering complete."
