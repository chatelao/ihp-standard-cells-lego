# LDView Camera Angle Analysis

This document describes the spherical coordinate system used by LDView for rendering LEGO models and defines the standard viewpoints used in the GEMINI project.

## Coordinate System

LDView uses a spherical coordinate system defined by **Latitude** and **Longitude** to position the camera when the `-UseCamera=0` flag is set.

### Latitude
Latitude controls the vertical angle of the camera relative to the model's horizon.
- **90**: Top view (looking straight down).
- **0**: Eye-level view (horizontal).
- **-90**: Bottom view (looking straight up).

### Longitude
Longitude controls the horizontal rotation of the camera around the model.
- **0**: Front view.
- **90**: Right side view.
- **180**: Back view.
- **270**: Left side view.

## Standard Viewpoints

The following viewpoints are configured in `scripts/render_models.sh`:

| View | Latitude | Longitude | Description |
| :--- | :--- | :--- | :--- |
| **Perspective** | N/A | N/A | Uses `-DefaultCamera` for a standard 3/4 view. |
| **Top** | 90 | 0 | Orthographic-style top-down view. |
| **Front** | 0 | 0 | Direct front-facing view. |
| **Side** | 0 | 90 | Direct side-facing view. |
| **Top-Down Angled** | 45 | 45 | Looking down from an angle between Front and Right. |
| **Side Angled** | 20 | 135 | Looking from a lower angle between Right and Back. |

## Implementation Notes

When specifying custom camera angles via the command line, the following flag is mandatory:
- `-UseCamera=0`: Instructs LDView to ignore any camera defined within the `.ldr` file and use the provided Latitude/Longitude/Zoom parameters.

Example command for "Top-Down Angled" view:
```bash
ldview model.ldr -SaveSnapshot=output.jpg -UseCamera=0 -Latitude=45 -Longitude=45
```
