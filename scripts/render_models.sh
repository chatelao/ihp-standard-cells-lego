#!/bin/bash
set -e
shopt -s nullglob

LDVIEW_BIN="ldview"
LDRAW_DIR="/usr/share/ldraw"
OUTPUT_DIR="$(pwd)/images"
MODELS_DIR="$(pwd)/models"
LOG_FILE="$(pwd)/ldview_render.log"

mkdir -p "$OUTPUT_DIR"
rm -f "$OUTPUT_DIR"/*.jpg "$OUTPUT_DIR"/*.mp4

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
    if ! "$LDVIEW_BIN" -SaveSnapshot="$OUTPUT_DIR/${filename}_top.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -Latitude=90 -Longitude=0 "$file" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render top image for $filename"
    fi

    # Front image
    echo "  Rendering front image..."
    if ! "$LDVIEW_BIN" -SaveSnapshot="$OUTPUT_DIR/${filename}_front.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -Latitude=0 -Longitude=0 "$file" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render front image for $filename"
    fi

    # Side image
    echo "  Rendering side image..."
    if ! "$LDVIEW_BIN" -SaveSnapshot="$OUTPUT_DIR/${filename}_side.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -Latitude=0 -Longitude=90 "$file" > "$LOG_FILE" 2>&1; then
        echo "  Error: Failed to render side image for $filename"
    fi

    # Verify static images
    for suffix in "" "_top" "_front" "_side"; do
        if [ ! -f "$OUTPUT_DIR/${filename}${suffix}.jpg" ]; then
            echo "  Error: Image file ${filename}${suffix}.jpg not found after rendering"
        fi
    done

    # Rotation frames for video
    TEMP_DIR="$(pwd)/temp_${filename}"
    mkdir -p "$TEMP_DIR"
    echo "  Rendering 36 rotation frames..."
    for i in $(seq 0 35); do
        lon=$((i * 10))
        printf -v frame "%02d" $i
        if ! "$LDVIEW_BIN" -SaveSnapshot="$TEMP_DIR/frame_${frame}.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -Longitude=$lon -Latitude=30 "$file" > "$LOG_FILE" 2>&1; then
             echo "  Error rendering frame ${frame} for $filename"
             cat "$LOG_FILE"
        fi
    done

    # Verify frames and generate video
    if [ -f "$TEMP_DIR/frame_00.jpg" ]; then
        echo "  Generating video..."
        ffmpeg -y -r 10 -i "$TEMP_DIR/frame_%02d.jpg" -vcodec libx264 -crf 25 -pix_fmt yuv420p "$OUTPUT_DIR/${filename}.mp4" > /dev/null 2>&1
    else
        echo "  Warning: No frames generated for $filename, skipping video."
    fi

    rm -rf "$TEMP_DIR"
done

rm -f "$LOG_FILE"
echo "Rendering complete."
