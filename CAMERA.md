# LDView Camera Angles Documentation

This document describes the camera positioning system used by LDView for rendering GEMINI LEGO models.

## Spherical Coordinate System

LDView uses a spherical coordinate system defined by **Latitude** and **Longitude** when the `-UseCamera=0` flag is set.

### Latitude (Vertical Angle)
Latitude controls the vertical tilt of the camera relative to the model's horizon.
- **90**: Directly above the model (Top view).
- **0**: Level with the model (Front/Side views).
- **-90**: Directly below the model (Bottom view).

### Longitude (Horizontal Angle)
Longitude controls the horizontal rotation of the camera around the model.
- **0**: Front of the model.
- **90**: Right side of the model.
- **180**: Back of the model.
- **270**: Left side of the model.

## Standard Viewpoints

The following viewpoints are standardized for the GEMINI gallery:

| View Name | Latitude | Longitude | Description |
| :--- | :--- | :--- | :--- |
| **Perspective** | N/A | N/A | Uses `-DefaultCamera` for a standard isometric-like view. |
| **Top** | 90 | 0 | Looking straight down at the cell layout. |
| **Front** | 0 | 0 | Looking at the front edge (length along Z-axis). |
| **Side** | 0 | 90 | Looking at the side edge (width along X-axis). |
| **Top-Down Angled** | 45 | 45 | An angled view from above, looking from the front-right corner. |
| **Side Angled** | 20 | 135 | A low-angle view looking from the back-right corner. |

## Implementation in Scripts

When rendering with `ldview`, ensure `-UseCamera=0` is included to override default camera behavior:

```bash
ldview -SaveSnapshot=output.jpg -UseCamera=0 -Latitude=45 -Longitude=45 model.ldr
```
