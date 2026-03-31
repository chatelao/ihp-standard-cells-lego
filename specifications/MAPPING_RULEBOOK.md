# LEF to LDR Mapping Rulebook (Derived from Data)

This document defines the transformation rules from CIF (Caltech Intermediate Form) to LDR (LDraw) LEGO models for the IHP SG13G2 process, derived from the handmade "Golden Standard" designs.

## 1. Coordinate System Mapping
- **Scale:**
  - 1 LEGO Stud = 0.27 µm = 20 LDU.
  - 1 LDU = 0.0135 µm (13.5 nm).
  - **CIF to LDU:** 1 unit (1 nm) = 20/270 LDU.
  - **LEF to LDU:** 1 unit (1 µm) = 20/0.27 LDU.
- **Horizontal (X) and Vertical (Z):**
  - LEF/CIF X-axis maps directly to LDraw X-axis.
  - LEF/CIF Y-axis maps directly to LDraw Z-axis.
  - **Offset:** A +10 LDU offset is applied to the Z-axis (LEF Y) to center the 3.78 µm cell height (280 LDU) within the standard 15-stud (300 LDU) height of the LEGO model. No offset is applied to the X-axis.
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

| Layer | CIF Layer | LEGO Part | Color | LDraw ID | Y-Offset | Height |
|-------|-----------|-----------|-------|----------|----------|--------|
| Substrate (Low) | (None) | Plates/Baseplate | Dark Gray | 8 | 0 | 8 |
| Substrate (High)| (None) | Plates | Dark Gray | 8 | -8 | 8 |
| N-Well | (Derived) | Plates | Light Gray | 7 | -8 | 8 |
| Diffusion (NMOS)| L1D0 | Plates | Dark Green | 288 | -16 | 8 |
| Diffusion (PMOS)| L1D0 | Plates | Dark Orange | 38 | -16 | 8 |
| Substrate Fill (P)| (None) | Plates | Dark Gray | 8 | -16 | 8 |
| Substrate Fill (N)| (None) | Plates | Light Gray | 7 | -16 | 8 |
| Polysilicon | L5D0 | Plates | Red | 4 | -24 | 8 |
| Contact (Base) | L6D0 | 1x1 Round Plate (6141) | White | 15 | -24 | 8 |
| Contact (Stack) | L6D0 | 1x1 Round Brick (3062b) | White | 15 | -48 | 24 |
| Metal 1 (Input) | L8D0 | Plates | Light Blue | 9 | -56 | 8 |
| Metal 1 (Internal)| L8D0 | Plates | Blue | 1 | -56 | 8 |
| Metal 1 (Output) | L8D0 | Plates | Dark Blue | 272 | -56 | 8 |
| Metal 1 (VDD) | L8D0 | Plates | Yellow | 14 | -56 | 8 |
| Metal 1 (VSS) | L8D0 | Plates | Black | 0 | -56 | 8 |
| Metal 2 Pin | L8D2 | 1x1 Tile (3070) | Pin Color | (Var) | -64 | 8 |

## 4. Modeling Principles
- **Polysilicon Span:** Polysilicon fingers typically span from Z=1 to Z=13.
- **Metal 1 Width:** Power rails (VDD/VSS) are typically 1-stud wide.
- **Unified Parity Rules (V3):** To maintain the interleaved grid structure of the SG13G2 process:
  - **Rail Parity (Tracks 0 and 14):** Contacts for both VDD (Track 14) and VSS (Track 0) MUST be placed on **EVEN** X-studs (0, 2, 4, ...), regardless of cell width.
  - **Signal/Active Parity (Tracks 2, 4, 6, 8, 10, 12):**
    - **Small models (width <= 7 studs):** All internal contacts MUST be on **ODD** X-studs (1, 3, 5, ...).
    - **Big models (width > 7 studs):** Internal contacts follow a symmetric parity rule: **ODD** if X < 8, and **EVEN** if X >= 8.
- **Connectivity:** Every Metal 1 rectangle must have at least one contact stack connecting to the underlying Polysilicon or Active layer.
- **Refined Snapping Logic:** To handle the transition from continuous coordinates to discrete LEGO studs:
  - **9.0 LDU Threshold:** A stud is occupied if it has at least 9.0 LDU overlap with a LEF/CIF rectangle. This threshold ensures that power fingers with an 8.9 LDU overlap on adjacent studs are thinned to a single stud.
  - **Center-Based Rule (Narrow Geometries):** For narrow geometries (width or height ≤ 21.0 LDU), the 9.0 LDU threshold is bypassed. Instead, the stud containing the geometry's center point is marked as occupied. This prevents narrow wires from disappearing or occupying two studs when they straddle a boundary.

## 5. Roadmap
To achieve full library coverage and physical accuracy, the following improvements are planned:
- **Dynamic N-Well Mapping:** Transition from the fixed Track 8 split to a CIF-driven N-Well (`L14D0`) occupancy grid.
- **Metal 2 & Via 1 Integration:** Full support for Via 1 (`L7D0`) and Metal 2 (`L9D0`) layer stacks to model multi-stage cell interconnects.
- **Multi-Stage Internal Gate Detection:** Improved heuristic to identify internal gates from LEF/CIF obstruction data for complex cells like buffers and flip-flops.
- **Interlocking Tiling Algorithm:** Enhancement of the greedy plate tiling algorithm to support interlocking patterns for increased physical model stability.
- **Automatic CIF-to-Pin Mapping:** Refinement of the contact-to-net association logic to handle overlapping geometries more robustly in high-density layouts.
