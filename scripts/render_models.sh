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

done

rm -f "$LOG_FILE"
echo "Rendering complete."
