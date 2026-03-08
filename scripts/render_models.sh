#!/bin/bash
set -e
shopt -s nullglob

LDVIEW_BIN="ldview"
LDRAW_DIR="/usr/share/ldraw"
OUTPUT_DIR="$(pwd)/images"
MODELS_DIR="$(pwd)/models"

mkdir -p "$OUTPUT_DIR"
rm -f "$OUTPUT_DIR"/*.jpg "$OUTPUT_DIR"/*.mp4

for file in "$MODELS_DIR"/*.ldr; do
    filename=$(basename "$file" .ldr)
    echo "Processing $filename..."

    # Static image
    echo "  Rendering static image..."
    if ! "$LDVIEW_BIN" "$file" -SaveJPG="$OUTPUT_DIR/${filename}.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" 2>&1; then
        echo "  Error: Failed to render static image for $filename"
        continue
    fi

    if [ ! -f "$OUTPUT_DIR/${filename}.jpg" ]; then
        echo "  Error: Static image file not found after rendering $filename"
        continue
    fi

    # Rotation frames for video
    TEMP_DIR="$(pwd)/temp_${filename}"
    mkdir -p "$TEMP_DIR"
    echo "  Rendering 36 rotation frames..."
    for i in $(seq 0 35); do
        lon=$((i * 10))
        printf -v frame "%02d" $i
        if ! "$LDVIEW_BIN" "$file" -SaveJPG="$TEMP_DIR/frame_${frame}.jpg" -Width=800 -Height=600 -LDrawDir="$LDRAW_DIR" -Longitude=$lon -Latitude=30 2>&1; then
             echo "  Error rendering frame ${frame} for $filename"
        fi
    done

    # Verify frames and generate video
    echo "  Contents of $TEMP_DIR:"
    ls -la "$TEMP_DIR"

    if [ -f "$TEMP_DIR/frame_00.jpg" ]; then
        echo "  Generating video..."
        ffmpeg -y -r 10 -i "$TEMP_DIR/frame_%02d.jpg" -vcodec libx264 -crf 25 -pix_fmt yuv420p "$OUTPUT_DIR/${filename}.mp4"
    else
        echo "  Warning: No frames generated for $filename, skipping video."
    fi

    rm -rf "$TEMP_DIR"
done

echo "Rendering complete."
