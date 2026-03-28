# LEF to LDR Mapping Rulebook (Derived from Data)

This document defines the transformation rules from LEF (Library Exchange Format) to LDR (LDraw) LEGO models for the IHP SG13G2 process, derived from the handmade "Golden Standard" designs.

## 1. Coordinate System Mapping
- **Scale:**
  - 1 LEGO Stud = 0.27 µm = 20 LDU.
  - 1 LDU = 0.0135 µm.
- **Horizontal (X) and Vertical (Z):**
  - LEF X maps to LDR X.
  - LEF Y maps to LDR Z.
  - A +10 LDU offset is applied to both axes to align the LEF origin (0,0) with the center of Stud 0.
- **Vertical Stack (Y):**
  - LDraw Y-axis is negative "up".
  - Layer height is 8 LDU (1 LEGO Plate).

## 2. Standard Cell Architecture
- **Height:** 15 studs (300 LDU).
- **Z-Track Assignments:**
  - **Track 0:** VSS Rail.
  - **Track 1:** Substrate (P) / Isolation.
  - **Tracks 2-4:** NMOS Active Area (Standard).
  - **Tracks 5-7:** Substrate (P) / Isolation.
  - **Track 8-14:** N-Well (overwrites Substrate).
  - **Tracks 8-12:** PMOS Active Area.
  - **Track 13:** N-Well / Isolation.
  - **Track 14:** VDD Rail.

## 3. Layer Stacking and Color Mapping

| Layer | LEGO Part | Color | LDraw ID | Y-Offset | height |
|-------|-----------|-------|----------|----------|--------|
| Substrate (Low) | Plates/Baseplate | Dark Gray | 8 | 0 | 8 |
| Substrate (High) | Plates | Dark Gray | 8 | -8 | 8 |
| N-Well | Plates | Light Gray | 7 | -8 | 8 |
| Diffusion (NMOS) | Plates | Dark Green | 288 | -16 | 8 |
| Diffusion (PMOS) | Plates | Dark Orange | 38 | -16 | 8 |
| Substrate Fill (P) | Plates | Dark Gray | 8 | -16 | 8 |
| Substrate Fill (N) | Plates | Light Gray | 7 | -16 | 8 |
| Polysilicon | Plates | Red | 4 | -24 | 8 |
| Contacts (to Poly) | 1x1 Round Brick (3062b) | White | 15 | -48 | 32 (incl. stud) |
| Contacts (to Active)| 1x1 Round Brick + 1x1 Round Plate (6141) | White | 15 | -48 | 40 (incl. stud) |
| Metal 1 (Input) | Plates | Light Blue | 9 | -56 | 8 |
| Metal 1 (Internal) | Plates | Blue | 1 | -56 | 8 |
| Metal 1 (Output) | Plates | Dark Blue | 272 | -56 | 8 |
| Metal 1 (VDD) | Plates | Yellow | 14 | -56 | 8 |
| Metal 1 (VSS) | Plates | Black | 0 | -56 | 8 |
| Metal 2 Connection | 1x1 Tile (3070) | Pin Color | (Var) | -64 | 8 |

## 4. Modeling Principles
- **Polysilicon Span:** Polysilicon fingers typically span from Z=1 to Z=13.
- **Metal 1 Width:** Power rails (VDD/VSS) are typically 1-stud wide.
- **Rail Parity (Tracks 0 and 14):** Contacts for both VDD (Track 14) and VSS (Track 0) MUST be placed on **EVEN** X-studs (0, 2, 4, ...), regardless of cell width.
- **Internal Track Parity (Tracks 2, 4, 6, 8, 10, 12):**
  - **Small models (width <= 7 studs):** All internal contacts MUST be on **ODD** X-studs (1, 3, 5, ...).
  - **Big models (width > 7 studs):** Internal contacts follow a symmetric parity rule: **ODD** if X < 8, and **EVEN** if X >= 8.
- **Connectivity:** Every Metal 1 rectangle must have at least one contact stack connecting to the underlying Polysilicon or Active layer.
- **Snapping:** A stud is occupied if it has at least 9.0 LDU overlap with a LEF geometry. For narrow geometries (width or height ≤ 21.0 LDU), a center-based rule is used: the stud containing the geometry's center point is occupied. This prevents narrow wires (like 20.0 LDU power fingers) from occupying two studs when they straddle a boundary.
