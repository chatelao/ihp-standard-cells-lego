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
| **Perspective** | 30 | 45 | Primary isometric-like view from the front-right. |
| **Top** | 90 | 0 | Looking straight down at the cell layout. |
| **Front** | 0 | 0 | Looking at the front edge (length along Z-axis). |
| **Side** | 0 | 90 | Looking at the side edge (width along X-axis). |
| **Top-Down Angled** | 45 | 315 | An angled view from above, looking from the front-left corner. |
| **Side Angled** | 25 | 135 | A low-angle view looking from the back-right corner. |

## Implementation in Scripts

When rendering with `ldview`, ensure `-UseCamera=0` is included to override default camera behavior. For best results across different environments, place the input file first and `-SaveSnapshot` last, use `-Flag=Value` format for arguments, and include stability flags like `-AllowConfig=0` to prevent interference from saved user settings:

```bash
ldview model.ldr -AllowConfig=0 -AutoRotate=0 -FixedAngle=1 -UseCamera=0 -Latitude=30 -Longitude=45 -SaveSnapshot=output.jpg
```
