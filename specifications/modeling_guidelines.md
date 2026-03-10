# IHP SG13G2 LEGO Modeling Guidelines (V3)

To ensure consistency across all LEGO models of IHP standard cells, the following guidelines must be followed.

## 1. Scale and Dimensions
The models are designed on a grid where LEGO studs represent the physical dimensions of the semiconductor cell.

- **Horizontal Scale (X and Z):** 1 LEGO Stud = 0.48 µm.
  - Matches the `CoreSite` width defined in the LEF.
  - Cell height of 3.78 µm ≈ 8 LEGO studs. We use **8 studs** as the standard cell height (Z-axis).
- **Vertical Scale (Y):** Each physical layer is represented by a LEGO Plate or Brick.
  - In LDraw, the negative Y direction is "up".
  - Standard stacking offsets (V3):
    - **Layer 1 (Y=0):** Substrate base (Dark Gray).
    - **Layer 2 (Y=-8):** Substrate high (Dark Gray) and N-Well (Light Gray).
    - **Layer 3 (Y=-16):** Active Regions (NMOS: Dark Green, PMOS: Dark Orange).
    - **Layer 4 (Y=-32):** Contacts (White round bricks, 3062b.dat) - Bridges Active to Metal 1.
    - **Layer 5 (Y=-32):** Metal 1 (Blue) and Power Rails (VDD: Yellow, VSS: Black).
    - **Layer 6 (Y=-56):** Via 1 (Black round bricks, 3062b.dat) - Bridges Metal 1 to Metal 2.
    - **Layer 7 (Y=-56):** Metal 2 (Green).

## 2. Layer to Color Mapping (V3)

| Layer | LEGO Color | LDU Range | LDraw Color ID | LDraw Y Offset | Description |
|-------|------------|-----------|----------------|----------------|-------------|
| Substrate (low) | Dark Gray | 8 | 8 | 0 | Bottom substrate layer. |
| Substrate (high) | Dark Gray | 8 | 8 | -8 | Top substrate layer (NMOS region). |
| N-Well | Light Gray | 8 | 7 | -8 | N-Well region (PMOS region). |
| Diffusion (NMOS) | Dark Green | 8 | 288 | -16 | Active area in P-substrate. |
| Diffusion (PMOS) | Dark Orange | 8 | 38 | -16 | Active area in N-Well. |
| Contacts | White | 24 | 15 | -32 | 1x1 round brick bridging Active to Metal 1. |
| Metal 1 (Pins) | Blue | 8 | 1 | -32 | Signal pins and first metal layer. |
| VDD Rail | Yellow | 8 | 14 | -32 | Power supply rail on Metal 1. |
| VSS Rail | Black | 8 | 0 | -32 | Ground rail on Metal 1. |
| Via 1 | Black | 24 | 0 | -56 | 1x1 round brick bridging Metal 1 to Metal 2. |
| Metal 2 | Green | 8 | 2 | -56 | Second metal interconnect layer. |

## 3. LDraw Unit Mapping
- 1 LEGO Stud = 20 LDraw Units (LDU).
- 1 LEGO Plate = 8 LDU (Height).
- 1 LEGO Brick = 24 LDU (Height).

## 4. Modeling Principles
- **No "Lego in Lego":** Physical layers must be vertically separated to avoid overlapping parts on the same layer.
- **Active Regions:** Automatically generated as strips. NMOS at Z=1-2 studs, PMOS at Z=5-6 studs.
- **Vias and Contacts:** Use 1x1 round bricks (3062b.dat) to connect different metal or active layers.
- **Power Rails:** VDD and VSS rails are placed on the Metal 1 layer (Y=-32) at the top and bottom of the cell.
- **Header Comment:** Every LDR file must start with the comment `0 // Substrate low (V3)` for verification.
