# IHP SG13G2 LEGO Modeling Guidelines

To ensure consistency across all LEGO models of IHP standard cells, the following guidelines must be followed.

## 1. Scale and Dimensions
The models are designed on a grid where LEGO studs represent the physical dimensions of the semiconductor cell.

- **Horizontal Scale (X and Z):** 1 LEGO Stud = 0.48 µm.
  - This matches the `CoreSite` width defined in the LEF.
  - LEF X-coordinate maps to LEGO X-coordinate.
  - LEF Y-coordinate maps to LEGO Z-coordinate.
  - Cell height of 3.78 µm ≈ 8 LEGO studs (Actual: 7.875 studs). We will use **8 studs** as the standard cell height (Z-axis).
- **Vertical Scale (Y):** Each physical layer is represented by a LEGO Plate (1/3 of a brick height).
  - Layers are stacked from bottom to top.
  - In LDraw, the negative Y direction is "up".
  - Standard stacking offsets (for visual clarity):
    - **Substrate:** Y=0
    - **Power/Ground Rails (Metal 1):** Y=-8
    - **Signal Pins (Metal 1):** Y=-16
  - Higher layers typically follow a pattern of an additional -8 LDU (one plate height) offset per layer.

## 2. Layer to Color Mapping
We use standard LDraw colors to represent different semiconductor layers.

| Layer | LEGO Color | LDraw Color ID | LDraw Y Offset | Description |
|-------|------------|----------------|----------------|-------------|
| Substrate | Light Gray | 7 | 0 | The base of the model (NMOS region). |
| N-Well | Tan | 19 | 0 | The base of the model (PMOS region). |
| Diffusion (Active) | Dark Orange | 38 | -8 | Transistor active areas. |
| Polysilicon | Red | 4 | -16 | Gate material. |
| Metal 1 | Blue | 1 | -16 | First metal interconnect layer. |
| Metal 2 | Green | 2 | -24 | Second metal interconnect layer. |
| VDD Rail | Yellow | 14 | -8 | Power supply rail (usually on Metal 1). |
| VSS Rail | Black | 0 | -8 | Ground rail (usually on Metal 1). |
| Vias / Contacts | White | 15 | Pattern-based | Vertical connections between layers. |

## 3. LDraw Unit Mapping
- 1 LEGO Stud = 20 LDraw Units (LDU).
- 1 LEGO Plate = 8 LDU (Height).
- 1 LEGO Brick = 24 LDU (Height).

Based on 1 Stud = 0.48 µm:
- **0.48 µm = 20 LDU**
- **0.024 µm = 1 LDU**

## 4. Modeling Principles
- Use **Baseplates** or large plates for the substrate. For cells wider than 8 studs (160 LDU), combine multiple large plates (e.g., 2x8 3034.dat and 1x8 3460.dat) to achieve the total width.
- Use **Plates** (e.g., 1x1, 1x2, 2x4) to represent rectangular areas defined in the LEF.
- If a geometry is not a multiple of 0.48 µm, round to the nearest LDraw unit or use the closest LEGO plate size.
- **Multi-Rectangle Geometries:** When a pin or obstruction is defined by multiple rectangles in the LEF, model them as a collection of LEGO plates. Ensure they are logically connected or stacked at the same Y-offset.
- **Vertical Orientation:** To rotate a 1xN plate from the X-axis (horizontal) to the Z-axis (vertical height in the cell), use the rotation matrix `0 0 1 0 1 0 -1 0 0`.
- VDD and VSS rails should be clearly visible at the top and bottom of the cell (along the Z-axis). Full rail representation requires both a main horizontal rail and any vertical spurs/branches defined in the LEF.
