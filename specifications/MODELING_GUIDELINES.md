# IHP SG13G2 LEGO Modeling Guidelines

To ensure consistency across all LEGO models of IHP standard cells, the following guidelines must be followed.

## 1. Scale and Dimensions
The models are designed on a grid where LEGO studs represent the physical dimensions of the semiconductor cell.

- **Horizontal Scale (X and Z):** 1 LEGO Stud = 0.24 µm.
  - This matches the `CoreSite` grid (0.48 µm = 2 studs).
  - LEF X-coordinate maps to LEGO X-coordinate.
  - LEF Y-coordinate maps to LEGO Z-coordinate.
  - Cell height of 3.78 µm is quantized to **16 studs** (3.84 µm) as the standard cell height (Z-axis).
- **Vertical Scale (Y):** Each physical layer is represented by a LEGO Plate (1/3 of a brick height) or Brick.
  - Layers are stacked from bottom to top.
  - In LDraw, the negative Y direction is "up".
  - Standard stacking offsets (V3):
    - **Layer 1 (Y=0):** Substrate base.
    - **Layer 2 (Y=-8):** Substrate high, N-Well.
    - **Layer 3 (Y=-16):** Active Regions (Diffusion).
    - **Layer 4 (Y=-24):** Polysilicon (Gates).
    - **Layer 5 (Y=-48):** Contacts (1x1 round brick).
    - **Layer 6 (Y=-56):** Metal 1, Rails.
    - **Layer 7 (Y=-80):** Vias (1x1 round brick).
    - **Layer 8 (Y=-88):** Metal 2.

## 2. Layer to Color Mapping (V3)
We use standard LDraw colors to represent different semiconductor layers.

| Layer | LEGO Color | LDU Height | LDraw Color ID | LDraw Y Offset | Description |
|-------|------------|------------|----------------|----------------|-------------|
| Substrate (low) | Dark Gray | 8 | 8 | 0 | Bottom substrate layer. |
| Substrate (high) | Dark Gray | 8 | 8 | -8 | Top substrate layer (P-substrate). |
| N-Well | Light Gray | 8 | 7 | -8 | N-Well region (PMOS side). |
| Diffusion (NMOS) | Dark Green | 8 | 288 | -16 | Active area in P-substrate (Studs 4-5). |
| Diffusion (PMOS) | Dark Orange | 8 | 38 | -16 | Active area in N-Well (Studs 10-11). |
| Polysilicon | Red | 8 | 4 | -24 | Gate material (Vertical plates). |
| Contacts | White | 24 | 15 | -48 | 1x1 round brick bridging Poly/Active to Metal 1. |
| Metal 1 (Pins) | Blue | 8 | 1 | -56 | Signal pins and first metal layer. |
| VDD Rail | Yellow | 8 | 14 | -56 | Power supply rail. |
| VSS Rail | Black | 8 | 0 | -56 | Ground rail. |
| Vias | Black | 24 | 0 | -80 | 1x1 round brick bridging Metal 1 to Metal 2. |
| Metal 2 | Green | 8 | 2 | -88 | Second metal interconnect layer. |

## 3. LDraw Unit Mapping
- 1 LEGO Stud = 20 LDraw Units (LDU).
- 1 LEGO Plate = 8 LDU (Height).
- 1 LEGO Brick = 24 LDU (Height).

Based on 1 Stud = 0.24 µm:
- **0.24 µm = 20 LDU**
- **0.012 µm = 1 LDU**

## 4. Modeling Principles
- Use **Baseplates** or large plates for the substrate. For cells wider than 8 studs (160 LDU), combine multiple large plates to achieve the total width.
- Use **Plates** (e.g., 1x1, 1x2, 2x4) to represent rectangular areas defined in the LEF.
- **Quantization:** Geometries are quantized to the 0.24 µm stud grid or the 0.012 µm LDU grid.
- **Vertical Orientation:** To rotate a 1xN plate from the X-axis to the Z-axis, use rotation matrix `0 0 1 0 1 0 -1 0 0`.
- **Interconnects:** Use 1x1 round bricks (`3062b.dat`).
- **Header Comment:** Every LDR file must start with the comment `0 // Substrate low (V3)` for verification.
