# LEF to LDR Mapping Rulebook

This document defines the standardized transformation rules from LEF (Library Exchange Format) to LDR (LDraw) LEGO models for the IHP SG13G2 process. It also serves as the modeling guideline to ensure consistency across all LEGO models.

## 1. Coordinate System Mapping
The models are designed on a grid where LEGO studs represent the physical dimensions of the semiconductor cell.

- **Horizontal Scale (X and Z):**
  - 1 LEGO Stud = 0.27 µm.
  - 1 LEGO Stud = 20 LDU (LDraw Units).
  - 1 LDU = 0.0135 µm.
  - LEF X maps to LDR X.
  - LEF Y maps to LDR Z.
- **Vertical Scale (Y):**
  - Each physical layer is represented by a LEGO Plate (1/3 of a brick height).
  - 1 LEGO Plate = 8 LDU.
  - 1 LEGO Brick = 24 LDU.
  - In LDraw, the negative Y direction is "up" (stacking layers from Y=0 upwards).
- **Origin Offset:**
  - A +10 LDU (0.135 µm) offset is applied to the LEF Y / LDR Z axis to align the center of Stud 0 with the LEF origin.
  - The LEF X / LDR X axis uses a direct mapping where the center of Stud 0 is located at X=10 LDU (corresponding to the LEF X=0 boundary).

## 2. Standard Cell Architecture
- **Total Height:** 15 studs (300 LDU).
- **Power Rails:** Located at Track 0 (VSS) and Track 14 (VDD), resulting in a 14-stud center-to-center distance.
- **Contact Tracks:** Contacts MUST be placed on EVEN Z-tracks only (0, 2, 4, 6, 8, 10, 12, 14).
- **Exceptions:** `sg13g2_nand2b_2` and `sg13g2_xor2_1` are hardcoded to 15 studs (300 LDU) wide to match their specialized golden designs, exceeding their 3.84 µm (14.2 stud) LEF definitions. They are also exempt from strict track alignment and parity rules.

## 3. Layer Stacking and Color Mapping (V3)

| Layer | LEGO Color | LDU Range | LDraw Color ID | LDraw Y Offset | Description |
|-------|------------|-----------|----------------|----------------|-------------|
| Substrate (low) | Dark Gray | 8 | 8 | 0 | Bottom substrate layer, cover all area out to the VDD/VSS |
| Substrate (high) | Dark Gray | 8 | 8 | -8 | Top substrate (P) layer. |
| N-Well | Light Gray | 8 | 7 | -8 | N-Well region (Studs 8-14). |
| Diffusion (NMOS) | Dark Green | 8 | 288 | -16 | Active area in P-Substrate, Studs 2-4. |
| Substrate fill (P) | Dark Gray | 8 | 8 | -16 | Substrate fill around NMOS. |
| Diffusion (PMOS) | Dark Orange | 8 | 38 | -16 | Active area in N-Well, Studs 8-12. |
| Polysilicon | Red | 8 | 4 | -24 | Gate material, 1 stud standard width. |
| Contacts | White | 32 | 15 | -48 | 1x1 round brick (3062b.dat) bridging Polysilicon to Metal 1. |
| Contacts | White | 24 | 15 | -48 | 1x1 round brick (3062b.dat) at Y=-48 and 1x1 round plate (6141.dat) at Y=-24 bridging Active to Metal 1. |
| Metal 1 | Light Blue | 8 | 9 | -56 | Inputs on the first metal layer. |
| Metal 1 | Blue | 8 | 1 | -56 | Cell internal connections. |
| Metal 1 | Dark Blue | 8 | 272 | -56 | Outputs first metal layer. |
| VDD Rail | Yellow | 8 | 14 | -56 | Power supply rail (Track 14). |
| VSS Rail | Black | 8 | 0 | -56 | Ground rail (Track 0). |
| Metal 2 Conn. | Pin Color | 8 | (Pin ID) | -64 | Metal 2 connection 1x1 tiles (3070.dat). |

## 4. Contact Placement Rules
Contacts bridge the gap between Metal 1 and underlying layers (Active or Polysilicon).

### 4.1 Track Alignment
- **0**: VSS Rail
- **2, 4**: NMOS Active Region
- **6**: Input Gates (Standard)
- **8, 10, 12**: PMOS Active Region
- **14**: VDD Rail

**Power Fingers**: VDD and VSS pins may have contacts on internal tracks (2-12). These internal contacts must follow the **Rail Parity** rule.

### 4.2 Stud Parity (X-axis)
- **VSS Contacts (All Tracks)**: MUST use ODD X-studs (1, 3, 5, ...).
- **VDD Contacts (All Tracks)**: MUST use EVEN X-studs (0, 2, 4, ...).
- **Signal Pins (Tracks 2-12)**:
  - **Small models (width <= 7)**: ODD X-studs.
  - **Big models (> 7 studs)**: Symmetric parity (ODD if X < 8, EVEN if X >= 8).

### 4.3 Generation Logic
1. **At Least One Contact Per Strip**: Every `RECT` on `Metal1` (for both `PIN`s and `OBS`tructions) MUST have at least one contact.
2. **Prioritization (Scoring)**:
   - Preferred on EVEN tracks (0, 2, 4, 6, 8, 10, 12, 14).
   - Higher score for studs matching the **Stud Parity** rules.
3. **Connectivity Guarantee**: The generator automatically ensures the appropriate material (Polysilicon for gates, Active for diffusions) is present at `Y=-24` and `Y=-16` layers to complete the connection. The `is_gate` and `is_diff` flags from LEF macro definitions take precedence over track-based heuristics (like Track 6) when determining whether to connect to Polysilicon or Active.
4. **Fallback**: If no studs satisfy strict parity/track rules, the highest-scoring available stud is selected to ensure connectivity.

## 5. Modeling Principles
- **Header Comment**: Every LDR file must start with the comment `0 // Substrate low (V3)`.
- **Interlocking**: Use **Baseplates** or large plates for the substrate. For cells wider than 8 studs, combine multiple large plates to achieve the total width.
- **Tiling**: Use the largest possible LEGO plates to represent rectangular areas to reduce part count and ensure sturdiness.
- **Rotation**: To rotate a 1xN plate from the X-axis to the Z-axis, use the rotation matrix `0 0 1 0 1 0 -1 0 0`.
- **Vertical Connectivity**:
  - Metal 1 (Y=-56) and Metal 2 connection tiles (Y=-64) must be clearly placed.
  - Contacts use 1x1 round bricks (`3062b.dat`) oriented with identity rotation (`1 0 0 0 1 0 0 0 1`) so their studs point upwards (towards negative Y).

## 6. Design Documentation (ASCII Art)
Each cell maintains a layer-by-layer ASCII art representation in `/design/*.md`. One character represents one LEGO stud.

### Character Mapping
- **Substrate**: `S` (Dark Gray), `N` (Light Gray/N-Well)
- **Active**: `n` (NMOS), `p` (PMOS)
- **Polysilicon**: `G` (Red)
- **Metal 1**:
  - `I`/`i`: Input (Light Blue)
  - `C`/`x`: Connection (Blue)
  - `O`/`o`: Output (Dark Blue)
  - `+`/`&`: VDD Rail (Yellow)
  - `-`/`_`: VSS Rail (Black)
- **Connections**: Lowercase characters (`i`, `o`, `c`, `&`, `_`) indicate the presence of a contact stack (Y=-48 brick) and a Metal 2 connection tile (Y=-64).
