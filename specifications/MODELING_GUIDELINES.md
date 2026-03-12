# IHP SG13G2 LEGO Modeling Guidelines

To ensure consistency across all LEGO models of IHP standard cells, the following guidelines must be followed.

## 1. Scale and Dimensions
The models are designed on a grid where LEGO studs represent the physical dimensions of the semiconductor cell.

- **Horizontal Scale (X and Z):** 1 LEGO Stud = 0.24 µm.
  - LEF X-coordinate maps to LEGO X-coordinate.
  - LEF Y-coordinate maps to LEGO Z-coordinate.
  - Cell height of 3.78 µm ≈ 16 LEGO studs (Actual: 15.75 studs). We will use **16 studs** as the standard cell height (Z-axis).
- **Vertical Scale (Y):** Each physical layer is represented by a LEGO Plate (1/3 of a brick height).
  - Layers are stacked from bottom to top.
  - In LDraw, the negative Y direction is "up".
  - Standard stacking offsets (V3):
    - **Layer 1 (Y=0):** Substrate base.
    - **Layer 2 (Y=-8):** Substrate high, N-Well.
    - **Layer 3 (Y=-16):** Active Regions (Diffusion).
    - **Layer 4 (Y=-24):** Polysilicon (Gates).
    - **Layer 5 (Y=-56):** Metal 1, Rails, and Contacts.
    - **Layer 6 (Y=-88):** Metal 2 and Vias.

## 2. Layer to Color Mapping (V3)

| Layer | LEGO Color | LDU Range | LDraw Color ID | LDraw Y Offset | Description |
|-------|------------|-----------|----------------|----------------|-------------|
| Substrate (low) | Dark Gray | 8 | 8 | 0 | Bottom substrate layer, cover all area out to the VDD/VSS |
| Substrate (high) | Dark Gray | 8 | 8 | -8 | Top substrate (P) layer. |
| N-Well | Light Gray | 8 | 7 | -8 | N-Well region. |
| Diffusion (NMOS) | Dark Green | 8 | 288 | -16 | Active area in P-Substrate ~5 Stud wide. |
| Diffusion (PMOS) | Dark Orange | 8 | 38 | -16 | Active area in N-Well ~3 Stud wide. |
| Polysilicon | Red | 8 | 4 | -24 | Gate material, 1 stud standard width, there may be an additional studs where contacts hit the poly |
| Contacts | White | 24 | 15 | -48 | 1x1 round brick bridging Active to Metal 1. |
| Metal 1 | Light Blue | 8 | 9 | -56| Inputs on the first metal layer, keep at a multiple (1..N) one stud (20 LDU) distance between different signals. |
| Metal 1 | Blue  | 8 | 1 | -56| Cell internal connections on the metal layer, keep at a multiple (1..N) one stud (20 LDU) distance between different signals. |
| Metal 1 | Dark Blue  | 8 | 272 | -56| Outputs First metal layer, keep at a multiple (1..N) one stud (20 LDU) distance between different signals. |
| VDD Rail | Yellow | 8 | 14 | -56 | Power supply rail. |
| VSS Rail | Black | 8 | 0 | -56 | Ground rail. |
| Vias | Black | 24 | 0 | -80 | 1x1 round brick bridging Metal 1 to Metal 2. |
| Metal 2 | Green | 8 | 2 | -88 | Second metal interconnect layer. |

## 3. LDraw Unit Mapping
- 1 LEGO Stud  = 24 LDU (Height).
- 1 LEGO Plate =  8 LDU (Height).
- 1 LEGO Brick = 24 LDU (Height).

Based on 1 Stud = 0.24 µm:
- **0.24 µm = 20 LDU**
- **0.012 µm = 1 LDU**

## 4. Modeling Principles
- We use standard LDraw colors to represent different semiconductor layers.
- The bricks have to fit and interlock as real-world versions.
- Use **Baseplates** or large plates for the substrate. For cells wider than 8 studs (160 LDU), combine multiple large plates (e.g., 2x8 3034.dat and 1x8 3460.dat) to achieve the total width.
- Use **Plates** (e.g., 1x1, 1x2, 2x4) to represent rectangular areas defined in the LEF.
- If a geometry is not a multiple of 0.48 µm, round to the nearest LDraw unit or use the closest LEGO plate size.
- **Multi-Rectangle Geometries:** When a pin or obstruction is defined by multiple rectangles in the LEF, model them as a collection of LEGO plates. Ensure they are logically connected or stacked at the same Y-offset.
- **Vertical Orientation:** To rotate a 1xN plate from the X-axis (horizontal) to the Z-axis (vertical height in the cell), use the rotation matrix `0 0 1 0 1 0 -1 0 0`.
- VDD and VSS rails should be clearly visible at the top and bottom of the cell (along the Z-axis) at Y=-56.
- **Interconnects (Contacts and Vias):** Use 1x1 round bricks (`3062b.dat`).
  - **Contacts** are white (Color 15) and placed at Y=-48.
  - **Vias** are black (Color 0) and placed at Y=-80.
  - These bricks are oriented to bridge downwards to the lower layers (e.g., using rotation `1 0 0 0 -1 0 0 0 -1`).
- **Header Comment:** Every LDR file must start with the comment `0 // Substrate low (V3)` for verification.
