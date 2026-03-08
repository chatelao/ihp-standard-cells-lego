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

| Layer | LEGO Color | LDraw Color ID | LDraw Y Offset | Height From-To (LDU) from Base | Description |
|-------|------------|----------------|----------------|----------------------|-------------|
| Substrate (low) | Dark Gray | 8 | 0 | 0 to 8 | Base plate over the whole cell. |
| Substrate (high)| Dark Gray | 8 | -8 | 9 to 16 | Second layer where no N-Well is present. |
| N-Well | Light Gray | 7 | -8 | 9 to 16 | N-Well region (PMOS). |
| Diffusion (NMOS)| Dark Green | 288 | -16 | 17 to 24 | Active area in P-substrate. |
| Diffusion (PMOS)| Dark Blue  | 38 | -16 | 17 to 24 | Active area in N-Well. |
| Polysilicon | Red | 4 | -24 | 25 to 32 | Gate material. |
| Vias / Contacts | Black | 0 | Pattern-based | 33 to 56 | 1x1 ROUND studs or plates. |
| Metal 1 | Yellow | 1 | -16 | 57 to 64 | First metal interconnect layer. |
| VDD Rail | White | 14 | -8 | 57 to 64 | Power supply rail. |
| VSS Rail | Black | 0 | -8 | 57 to 64 | Ground rail. |

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
