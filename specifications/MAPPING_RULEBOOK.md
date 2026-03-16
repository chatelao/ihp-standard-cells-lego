# Mapping Rulebook: LEF to LDR Conversion

This document details the precise transformation logic used to convert IHP SG13G2 LEF specifications into LDraw (LDR) LEGO models, as implemented in `scripts/lef_to_ldr.py`.

## 1. Coordinate Transformation & Scaling

### Scale Factors
- **Physical Scale:** 1 LEGO Stud = 0.27 µm.
- **LDraw Scale:** 1 LEGO Stud = 20 LDU (Horizontal X/Z).
- **LDraw Vertical Scale:** 1 LEGO Plate = 8 LDU (Vertical Y).
- **Conversion Factor:** `LDU = round(um * (20 / 0.27))`.

### Axis Mapping
- **LEF X** → **LDraw X**
- **LEF Y** → **LDraw Z**
- **LEF Origin Shift:** A **+10 LDU (0.135 µm)** offset is added to all X and Z coordinates to align the LEF (0,0) origin with the center of LEGO Stud 0.

### Dimensions
- **Standard Cell Height:** Fixed at **15 studs (300 LDU)**.
- **Cell Width:** Calculated as `int(round(width_um / 0.48) * 2 - 1)` studs, then converted to LDU.

## 2. Layer Stacking (V3 Standard)

| Layer Name | LDraw Y Offset | LDraw Color (ID) | Part(s) Used |
| :--- | :--- | :--- | :--- |
| Substrate Low | 0 | Dark Gray (8) | Plates (Interlocked) |
| Substrate High / N-Well | -8 | Dark Gray (8) / Light Gray (7) | Plates |
| Active (NMOS/PMOS) | -16 | Dark Green (288) / Dark Orange (38) | Plates |
| Polysilicon (Gates) | -24 | Red (4) | Plates |
| Contacts (Bridge) | -48 | White (15) | 1x1 Round Brick (3062b) |
| Contacts (Active Fill) | -24 | White (15) | 1x1 Round Plate (6141) |
| Metal 1 / Rails | -56 | Varies (9, 272, 1, 14, 0) | Plates |

## 3. Tiling Algorithm (`get_best_plates_multi`)

A greedy tiling algorithm is used to fill rectangular regions with standard LEGO plates:
1. **Prioritize Area:** Plates are sorted by area (largest first: 8x2, 8x1, 6x1, 4x2, 4x1, 3x1, 2x2, 2x1, 1x1).
2. **Interlocking:**
   - The **Substrate Low (Y=0)** layer uses `prefer_rotated=True`, scanning column-by-column (X then Z) to create Z-aligned plates.
   - Higher layers default to X-aligned plates, ensuring physical interlocking between the base and subsequent layers.
3. **Boundaries:** Plates are never allowed to cross color or region boundaries.

## 4. Polysilicon Gate Placement

### Input Pin Selection
- Input pins are sorted by their average LEF X-coordinate.
- **Ideal X:** `4 * j + 1` (where `j` is the pin index).
- **Parity Rule:**
  - Small models (width ≤ 7): Input contacts (at Z=6) use **ODD** studs.
  - Big models (width > 7): Input contacts use **Symmetric Parity** (ODD if Stud X < 8, EVEN if Stud X ≥ 8).

### Gate Geometry
- **Small Models / Drive-1:** One gate finger at `Contact_X + 1`.
- **Big Models / Drive-2:** Two gate fingers at `Contact_X - 1` and `Contact_X + 1`, bridged by a 3-stud wide plate (`3623.dat`) at Stud `Contact_X`.
- **Vertical Span:** Gates span Studs 1 to 13 (Z=20 to 280).

## 5. Contact Generation & Parity

Contacts are generated only if a Metal 1 rectangle overlaps an active region or power rail.

### Parity Rules
- **VDD Rail (Z=14):** EVEN studs.
- **VSS Rail (Z=0):** ODD studs.
- **NMOS Active (Z=2-4):** EVEN studs.
- **PMOS Active (Z=8-12):**
  - Drive-1: ODD studs.
  - Drive-2 / Big Models: EVEN studs.

### Multi-Part Assembly
- **Active Contacts:** Composed of a 1x1 Round Brick (`3062b.dat`) at Y=-48 AND a 1x1 Round Plate (`6141.dat`) at Y=-24 to fill the gap between Metal 1 and Diffusion.
- **Poly Contacts:** Only use the 1x1 Round Brick at Y=-48.

## 6. Metal 1 & Rails

- **Clamping:** Metal 1 geometries are clamped to the cell boundaries [0, width_ldu] and [0, height_ldu] to prevent bounding box expansion.
- **Colors:**
  - Input: Light Blue (9)
  - Output: Dark Blue (272)
  - Internal: Blue (1)
  - VDD: Yellow (14)
  - VSS: Black (0)
