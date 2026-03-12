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

# Helper function to render with retries
render_snapshot() {
    local output="$1"
    shift
    local args=("$@")
    local max_attempts=3
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        if "$LDVIEW_BIN" -SaveSnapshot="$output" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" "${args[@]}" > "$LOG_FILE" 2>&1; then
            return 0
        fi
        echo "    Attempt $attempt failed. Retrying..."
        attempt=$((attempt + 1))
        sleep 1
    done
    return 1
}

for file in "$MODELS_DIR"/*.ldr; do
    filename=$(basename "$file" .ldr)
    echo "Processing $filename..."

    # Perspective image
    echo "  Rendering perspective image..."
    if ! render_snapshot "$OUTPUT_DIR/${filename}.jpg" -DefaultCamera "$file"; then
        echo "  Error: Failed to render perspective image for $filename"
    fi

    # Top image
    echo "  Rendering top image..."
    if ! render_snapshot "$OUTPUT_DIR/${filename}_top.jpg" -UseCamera=0 -Latitude=90 -Longitude=0 "$file"; then
        echo "  Error: Failed to render top image for $filename"
    fi

    # Front image
    echo "  Rendering front image..."
    if ! render_snapshot "$OUTPUT_DIR/${filename}_front.jpg" -UseCamera=0 -Latitude=0 -Longitude=0 "$file"; then
        echo "  Error: Failed to render front image for $filename"
    fi

    # Side image
    echo "  Rendering side image..."
    if ! render_snapshot "$OUTPUT_DIR/${filename}_side.jpg" -UseCamera=0 -Latitude=0 -Longitude=90 "$file"; then
        echo "  Error: Failed to render side image for $filename"
    fi

    # Top-Down Angled image
    echo "  Rendering top-down angled image..."
    if ! render_snapshot "$OUTPUT_DIR/${filename}_top_angled.jpg" -UseCamera=0 -Latitude=45 -Longitude=45 "$file"; then
        echo "  Error: Failed to render top-down angled image for $filename"
    fi

    # Side Angled image
    echo "  Rendering side angled image..."
    if ! render_snapshot "$OUTPUT_DIR/${filename}_side_angled.jpg" -UseCamera=0 -Latitude=20 -Longitude=135 "$file"; then
        echo "  Error: Failed to render side angled image for $filename"
    fi

    # Verify static images
    for suffix in "" "_top" "_front" "_side" "_top_angled" "_side_angled"; do
        if [ ! -f "$OUTPUT_DIR/${filename}${suffix}.jpg" ]; then
            echo "  Error: Image file ${filename}${suffix}.jpg not found after rendering"
        fi
    done

    # Building instructions PDF
    echo "  Generating building instructions..."
    TEMP_STEP_DIR="$(pwd)/temp_steps_${filename}"
    mkdir -p "$TEMP_STEP_DIR"

    # Count steps
    num_steps=$(grep -c "0 STEP" "$file" || true)
    # Total steps is num_steps + 1 (for the final model)
    total_steps=$((num_steps + 1))

    step_images=()
    for (( s=1; s<=total_steps; s++ )); do
        step_img="$TEMP_STEP_DIR/step_${s}.jpg"
        if render_snapshot "$step_img" -Step="$s" "$file"; then
            step_images+=("$step_img")
        else
            echo "  Error: Failed to render step $s for $filename"
        fi
    done

    if [ ${#step_images[@]} -gt 0 ]; then
        if command -v img2pdf >/dev/null 2>&1; then
            img2pdf "${step_images[@]}" --output "$INSTRUCTIONS_DIR/${filename}.pdf"
        else
            echo "  Warning: img2pdf not found, skipping PDF generation for $filename"
        fi
    fi
    rm -rf "$TEMP_STEP_DIR"

done

rm -f "$LOG_FILE"
echo "Rendering complete."
