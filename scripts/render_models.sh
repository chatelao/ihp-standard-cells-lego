#!/bin/bash
set -e
shopt -s nullglob

LDVIEW_BIN="ldview"
LDRAW_DIR="/usr/share/ldraw"
OUTPUT_DIR="$(pwd)/images"
INSTRUCTIONS_DIR="$(pwd)/instructions"
MODELS_DIR="$(pwd)/models"
LOG_FILE="$(pwd)/logs/ldview_render.log"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$INSTRUCTIONS_DIR"
mkdir -p "$(dirname "$LOG_FILE")"
rm -f "$OUTPUT_DIR"/*.jpg
rm -f "$INSTRUCTIONS_DIR"/*.pdf

for file in "$MODELS_DIR"/*.ldr; do
    filename=$(basename "$file" .ldr)
    echo "Processing $filename..."

    # Perspective image
    echo "  Rendering perspective image..."
    if ! "$LDVIEW_BIN" "$file" -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=30 -Longitude=45 -SaveSnapshot="$OUTPUT_DIR/${filename}.jpg" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render perspective image for $filename"
        [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
    fi

    # Top image
    echo "  Rendering top image..."
    if ! "$LDVIEW_BIN" "$file" -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=90 -Longitude=0 -SaveSnapshot="$OUTPUT_DIR/${filename}_top.jpg" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render top image for $filename"
        [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
    fi

    # Front image
    echo "  Rendering front image..."
    if ! "$LDVIEW_BIN" "$file" -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=0 -Longitude=0 -SaveSnapshot="$OUTPUT_DIR/${filename}_front.jpg" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render front image for $filename"
        [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
    fi

    # Side image
    echo "  Rendering side image..."
    if ! "$LDVIEW_BIN" "$file" -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=0 -Longitude=90 -SaveSnapshot="$OUTPUT_DIR/${filename}_side.jpg" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render side image for $filename"
        [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
    fi

    # Top-Down Angled image
    echo "  Rendering top-down angled image..."
    if ! "$LDVIEW_BIN" "$file" -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=45 -Longitude=315 -SaveSnapshot="$OUTPUT_DIR/${filename}_top_angled.jpg" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render top-down angled image for $filename"
        [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
    fi

    # Side Angled image
    echo "  Rendering side angled image..."
    if ! "$LDVIEW_BIN" "$file" -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=25 -Longitude=135 -SaveSnapshot="$OUTPUT_DIR/${filename}_side_angled.jpg" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render side angled image for $filename"
        [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
    fi

    # Verify static images
    for suffix in "" "_top" "_front" "_side" "_top_angled" "_side_angled"; do
        if [ ! -f "$OUTPUT_DIR/${filename}${suffix}.jpg" ]; then
            echo "  Error: Image file ${filename}${suffix}.jpg not found after rendering"
            [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
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
        if "$LDVIEW_BIN" "$file" -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -UseCamera=0 -Latitude=30 -Longitude=45 -Step="$s" -SaveSnapshot="$step_img" > "$LOG_FILE" 2>&1; then
            # Annotate step with parts needed
            python3 scripts/annotate_step.py "$file" "$s" "$step_img"
            step_images+=("$step_img")
        else
            echo "  Error: Failed to render step $s for $filename"
            [ -f "$LOG_FILE" ] && cat "$LOG_FILE"
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

echo "Rendering complete. Log saved to $LOG_FILE"
