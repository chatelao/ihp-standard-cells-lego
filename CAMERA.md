# LDView Camera Angle Analysis

This document provides an in-depth analysis of how to control the camera angles for LDraw models using `ldview` command-line parameters, specifically focusing on generating top-down and side views.

## Coordinate System

`ldview` uses a spherical coordinate system defined by `-Latitude` and `-Longitude` when the `-UseCamera=0` flag is set. This allows for precise positioning of the camera on a virtual sphere centered around the model's bounding box.

- **Latitude**: Vertical angle in degrees.
    - `90`: Directly above the model (Top view).
    - `0`: On the horizontal plane (Front/Side views).
    - `-90`: Directly below the model (Bottom view).
- **Longitude**: Horizontal angle in degrees.
    - `0`: Facing the "Front" of the model.
    - `90`: Facing the "Right Side" of the model.
    - `180`: Facing the "Back" of the model.
    - `270` (or `-90`): Facing the "Left Side" of the model.

## Standard Orthogonal Views

To provide a complete 360-degree representation of the standard cells, we define the following standard orthogonal views:

| View Name | Latitude | Longitude | Filename Suffix |
|-----------|----------|-----------|-----------------|
| Top       | 90       | 0         | `_top`          |
| Front     | 0        | 0         | `_front`        |
| Side      | 0        | 90        | `_side`         |
| Bottom    | -90      | 0         | `_bottom`       |
| Back      | 0        | 180       | `_back`         |

## Additional Angled Views

To achieve more descriptive "down from top" and "from the side" perspectives that highlight the 3D stacking of layers (Substrate to Metal 2), angled views are used.

### Down from Top (Angled)
To see the depth of the layers while maintaining a top-down focus:
- **Latitude**: `45`
- **Longitude**: `45`
- **Command**: `ldview -UseCamera=0 -Latitude=45 -Longitude=45 ...`

### From the Side (Angled)
To better visualize the vertical interconnects (vias/contacts) between layers:
- **Latitude**: `20`
- **Longitude**: `135`
- **Command**: `ldview -UseCamera=0 -Latitude=20 -Longitude=135 ...`

## Implementation for Standard Cells

The standard cell library uses these views to generate a comprehensive gallery. The `scripts/render_models.sh` script is responsible for executing these commands for each `.ldr` file in the `models/` directory.

```bash
# Example: Rendering the Bottom view
ldview -SaveSnapshot="model_bottom.jpg" -Width=800 -Height=600 -UseCamera=0 -Latitude=-90 -Longitude=0 model.ldr
```
