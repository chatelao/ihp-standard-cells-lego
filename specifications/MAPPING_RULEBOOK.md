# LEF & CIF to LDR Mapping Rulebook

This document defines the transformation rules from CIF (Caltech Intermediate Form) and LEF (Library Exchange Format) to physically buildable LDR (LDraw) LEGO models for the IHP SG13G2 process, incorporating the `/handmade` reference designs and buildability standards.

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
  - **Track 0:** VSS Rail (P+ Substrate Tap).
  - **Track 1:** Isolation + `Y=-8` Half-Lap Cell-to-Cell Snapping Row (West recess `X=0`, East tab `X=W`).
  - **Tracks 2-5:** NMOS Active Area.
  - **Tracks 6-7:** Isolation / Polysilicon Input Track (`Z=6`).
  - **Track 7-14:** N-Well (`L31D0`, CIF-driven; typically `Z >= 7` or `8`).
  - **Tracks 8-12:** PMOS Active Area.
  - **Track 13:** Isolation + `Y=-8` Half-Lap Cell-to-Cell Snapping Row (West recess `X=0`, East tab `X=W`).
  - **Track 14:** VDD Rail (N+ Well Tap).

## 3. Layer Stacking and Color Mapping (Modern BrickLink-Available Palette)

| Layer | CIF Layer | LEGO Part | Color | LDraw ID | Y-Offset | Height |
|-------|-----------|-----------|-------|----------|----------|--------|
| Substrate (Low) | (Base) | Plates | Dark Bluish Gray | 72 | 0 | 8 |
| Substrate (High) | (Base) | Plates | Dark Bluish Gray | 72 | -8 | 8 |
| N-Well | L31D0 | Plates | Light Bluish Gray | 71 | -8 | 8 |
| Diffusion (NMOS) | L1D0 | Plates | Dark Green | 288 | -16 | 8 |
| Diffusion (PMOS) | L1D0 | Plates | Dark Orange | 38 | -16 | 8 |
| Substrate Fill (P) | (Fill) | Plates | Dark Bluish Gray | 72 | -16 | 8 |
| Substrate Fill (N) | (Fill) | Plates | Light Bluish Gray | 71 | -16 | 8 |
| Polysilicon | L5D0 | Plates | Red | 4 | -24 | 8 |
| Contact (Base) | L6D0 | 1x1 Round Plate (`6141.dat`) | White | 15 | -24 | 8 |
| Contact (Stack) | L6D0 | 1x1 Round Brick (`3062b.dat`) | White | 15 | -48 | 24 |
| Dielectric Support (Base) | (ILD) | 1x1 Round Plate (`6141.dat`) | Trans-Clear | 47 | -24 | 8 |
| Dielectric Support (Pillar) | (ILD) | 1x1 Round Brick (`3062b.dat`) | Trans-Clear | 47 | -48 | 24 |
| Metal 1 (Input) | L8D0 + LEF | Plates | Bright Light Blue | 212 | -56 | 8 |
| Metal 1 (Internal) | L8D0 | Plates | Blue | 1 | -56 | 8 |
| Metal 1 (Output) | L8D0 + LEF | Plates | Dark Blue | 272 | -56 | 8 |
| Metal 1 (VDD) | L8D0 + LEF | Plates | Yellow | 14 | -56 | 8 |
| Metal 1 (VSS) | L8D0 + LEF | Plates | Black | 0 | -56 | 8 |
| Metal 1 Pin Marker | L8D2 | 1x1 Tile w/ Groove (`3070b.dat`) | Pin Color | (Var) | -64 | 8 |
| Via 1 | L19D0 | 1x1 Round Plate (`6141.dat`) | White | 15 | -64 | 8 |
| Metal 2 | L10D0 | Plates | Orange | 25 | -72 | 8 |
| Metal 2 Pin Marker | L10D2 | 1x1 Tile w/ Groove (`3070b.dat`) | Orange | 25 | -80 | 8 |

## 4. Physical Buildability & Modeling Principles
- **Seam-Staggered ("Bricklaying") Base Foundation:**
  - `Y=0` uses `Z`-bands (`0..3`, `4..6`, `7..10`, `11..14`) and `X`-offsets (`8, 24, 40, ...` or `W//2` for narrow cells) so no vertical seam aligns with `Y=-8` (`X` at `16, 32, 48, ...`) or `Y=-16`.
  - `Y=-16` fills all non-diffusion studs with Substrate (`72`) / N-Well (`71`) so `Y=-24` Polysilicon and Contact bases sit on a 100% solid floor.
- **Cell-to-Cell Horizontal Snapping:**
  - At `Y=-8`, isolation rows `Z=1` and `Z=13` are recessed 1 stud on the West (`X=0`) and project +1 stud on the East (`X=W`), allowing adjacent cells in a standard-cell row to physically click together.
- **Dielectric Support Pillars (Zero Floating Parts / Zero Spinners):**
  - Every Metal 1 plate (`Y=-56`) of area ≥ 2 studs is supported by at least 2 pillars at `Y=-48` (and max cantilever overhang ≤ 3 studs) using real White (`15`) contacts where present and Trans-Clear (`47`) `SiO₂` dielectric pillars elsewhere.
- **Per-Color Mold Whitelisting & Instruction Chunking:**
  - Plate selection in [`lego_utils.py`](file:///home/antigravity/chatelao/ihp-standard-cells-lego/scripts/lego_utils.py) restricts large plates to molds manufactured in each LDraw color.
  - `0 STEP` blocks are chunked to ≤ 28 parts per step, with `6141.dat` (`Y=-24`) emitted before `3062b.dat` (`Y=-48`).
- **Net-Aware Tiling & LEF Semantics:**
  - Metal 1 is tiled per net (using CIF `L8D25` labels and LEF `DIRECTION` for `INPUT`/`OUTPUT`/`TRISTATE`) so distinct adjacent nets never merge into a single plate.
- **Harmonized Contact Parity Rules:**
  - **Rail Parity (Tracks 0 and 14):** Both VDD (Track 14) and VSS (Track 0) contacts MUST be placed on **EVEN** X-studs (`0, 2, 4, ...`).
  - **Internal Contacts (Tracks 2, 4, 6, 8, 10, 12):** Placed on **EVEN** Z-tracks following physical CIF `L6D0` locations snapped to the nearest Metal 1 occupied stud.
- **Refined Snapping Logic:**
  - **9.0 LDU Threshold:** A stud is occupied if it has at least 9.0 LDU overlap with a rectangle.
  - **Center-Based / Edge-Crossing Rule:** Narrow geometries (width or height ≤ 21.0 LDU) use center/sub-grid/edge-intersection checks so continuous wires and polysilicon gates never fracture into disconnected islands.
