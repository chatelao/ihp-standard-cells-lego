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
rm -f "$OUTPUT_DIR"/*.jpg
rm -f "$INSTRUCTIONS_DIR"/*.pdf

for file in "$MODELS_DIR"/*.ldr; do
    filename=$(basename "$file" .ldr)
    echo "Processing $filename..."

    # Perspective image
    echo "  Rendering perspective image..."
    if ! "$LDVIEW_BIN" -SaveSnapshot="$OUTPUT_DIR/${filename}.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -DefaultCamera "$file" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render perspective image for $filename"
    fi

    # Top image
    echo "  Rendering top image..."
    if ! "$LDVIEW_BIN" -SaveSnapshot="$OUTPUT_DIR/${filename}_top.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=90 -Longitude=0 "$file" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render top image for $filename"
    fi

    # Front image
    echo "  Rendering front image..."
    if ! "$LDVIEW_BIN" -SaveSnapshot="$OUTPUT_DIR/${filename}_front.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=0 -Longitude=0 "$file" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render front image for $filename"
    fi

    # Side image
    echo "  Rendering side image..."
    if ! "$LDVIEW_BIN" -SaveSnapshot="$OUTPUT_DIR/${filename}_side.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=0 -Longitude=90 "$file" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render side image for $filename"
    fi

    # Verify static images
    for suffix in "" "_top" "_front" "_side"; do
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
        if "$LDVIEW_BIN" -SaveSnapshot="$step_img" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -Step="$s" "$file" > "$LOG_FILE" 2>&1; then
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
