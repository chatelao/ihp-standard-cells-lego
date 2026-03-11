# LDView Camera Angles Documentation

This document explains the spherical coordinate system used by LDView to control camera angles for rendering LDraw models.

## Spherical Coordinate System

LDView uses two main parameters to define the camera position relative to the model's center when `-UseCamera=0` is specified:

- **Latitude (`-Latitude=N`):** Controls the vertical angle in degrees.
    - `90`: Directly from the top.
    - `0`: Level with the model (equator).
    - `-90`: Directly from the bottom.
- **Longitude (`-Longitude=N`):** Controls the horizontal rotation around the model in degrees.
    - `0`: Front view.
    - `90`: Right side view.
    - `180`: Back view.
    - `270` (or `-90`): Left side view.

## Standard Views

The following parameters are used for the standard orthogonal views:

| View | Latitude | Longitude | Description |
|------|----------|-----------|-------------|
| **Front** | `0` | `0` | Standard front-facing view. |
| **Top** | `90` | `0` | Bird's-eye view from directly above. |
| **Side** | `0` | `90` | View from the right side. |
| **Back** | `0` | `180` | View from directly behind. |
| **Bottom** | `-90` | `0` | View from directly underneath. |

## Additional Angled Views

To provide better spatial understanding of the 3D LEGO models, two additional angled views are implemented:

### 1. Top-Down Angled
- **Parameters:** `-Latitude=45 -Longitude=45`
- **Analysis:** This view provides a 45-degree inclination from the top and a 45-degree rotation from the front. It effectively shows the top surface, the front face, and the right side face simultaneously, highlighting the 3D stacking of the layers.

### 2. Side Angled
- **Parameters:** `-Latitude=20 -Longitude=135`
- **Analysis:** This view uses a lower inclination (20 degrees) and a deeper rotation (135 degrees) to look at the model from a rear-side perspective. It is particularly useful for visualizing the depth and interconnects (contacts and vias) between the Metal 1 and Metal 2 layers.

## Usage in Scripts

When using these parameters in `scripts/render_models.sh`, ensure `-UseCamera=0` is included to enable the spherical coordinates, and `-DefaultCamera` is *not* used for these specific views.
