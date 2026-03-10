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
    - **Layer 1 (Substrate low):** Y=0
    - **Layer 2 (Substrate high/Rails/N-Well):** Y=-8
    - **Layer 3 (Diffusion/Metal 1/Contacts):** Y=-16
    - **Layer 4 (Polysilicon/Metal 2):** Y=-24
  - Higher layers typically follow a pattern of an additional -8 LDU (one plate height) offset per layer.

## 2. Layer to Color Mapping
We use standard LDraw colors to represent different semiconductor layers.

| Layer # | Component | LEGO Color | LDU Range | LDraw Color ID | LDraw Y Offset | Description |
|---------|-----------|------------|-----------|----------------|----------------|-------------|
| 1 | Substrate (low) | Dark Gray | 0 to 8 | 8 | 0 | Base plate over the whole cell. |
| 2 | Substrate (high)| Dark Gray | 8 to 16 | 8 | -8 | Second layer where no N-Well is present. |
| 2 | N-Well | Light Gray | 8 to 16 | 7 | -8 | N-Well region (PMOS). |
| 2 | VDD Rail | Yellow | 8 to 16 | 14 | -8 | Power supply rail (Metal 1). |
| 2 | VSS Rail | Black | 8 to 16 | 0 | -8 | Ground rail (Metal 1). |
| 3 | Diffusion (NMOS)| Dark Green | 16 to 24 | 288 | -16 | Active area in P-substrate. |
| 3 | Diffusion (PMOS)| Dark Orange| 16 to 24 | 38 | -16 | Active area in N-Well. |
| 3 | Metal 1 | Blue | 16 to 24 | 1 | -16 | First metal interconnect layer. |
| 3 | Contacts | White | 16 to 24 | 15 | -16 | Physical interface between active regions and Metal 1. |
| 4 | Polysilicon | Red | 24 to 32 | 4 | -24 | Gate material. |
| 4 | Metal 2 | Green | 24 to 32 | 2 | -24 | Second metal interconnect layer. |
| 2-4 | Vias / Contacts | Black | 8 to 32 | 0 | Bridge | 1x1 ROUND bricks (part 3062b) to bridge layers. |

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
