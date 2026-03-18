# LEF to LDR Mapping Rulebook

This document defines the standardized transformation rules from LEF (Library Exchange Format) to LDR (LDraw) LEGO models for the IHP SG13G2 process.

## 1. Coordinate System Mapping
- 1 LEGO Stud = 0.27 µm.
- 1 LEGO Stud = 20 LDU (LDraw Units).
- LEF X maps to LDR X.
- LEF Y maps to LDR Z.
- Origin Offset: A +10 LDU (0.135 µm) offset is applied to both axes to align the center of Stud 0 with the LEF origin.

## 2. Standard Cell Architecture
- Total Height: 15 studs (300 LDU).
- Power Rails: Located at Track 0 (VSS) and Track 14 (VDD), resulting in a 14-stud center-to-center distance.
- **Exceptions**:
  - `sg13g2_nand2b_2` is hardcoded to 15 studs (300 LDU) wide to match its specialized golden design, exceeding its 3.84 µm (14.2 stud) LEF definition.
  - `sg13g2_nand2b_2` utilizes a specialized active region layout with isolation gaps:
    - **PMOS (Z=8..12)**: Active at X in [0,1,2] and [4,5,6,7,8,9,10,11,12,13]. Gaps at X=3 and X=14.
    - **NMOS (Z=2..4)**: Active at X in [1,2,3] and [5,6,7,8,9,10,11,12,13]. Gaps at X=0, X=4, and X=14.
  - `sg13g2_nand2b_2` is also exempt from strict track alignment and parity rules in Section 3.

## 3. Contact Placement Rules
Contacts bridge the gap between Metal 1 and underlying layers (Active or Polysilicon). To ensure buildability and electrical consistency, contacts must follow these placement rules:

### 3.1 Track Alignment
Contacts are strictly permitted only on EVEN Z-tracks:
- **0**: VSS Rail
- **2, 4**: NMOS Active Region
- **6**: Input Gates (Standard)
- **8, 10, 12**: PMOS Active Region
- **14**: VDD Rail

### 3.2 Stud Parity (X-axis)
To maintain grid alignment and prevent illegal overlaps, contacts follow a strict parity rule on the X-axis:
- **VSS Rail (Z=0)**: MUST use ODD X-studs (1, 3, 5, ...).
- **VDD Rail (Z=14)**: MUST use EVEN X-studs (0, 2, 4, ...).
- **Active & Gate Tracks (Z=2..12)**:
  - Small models (width <= 7): Always ODD (1, 3, 5, ...).
  - Big models (> 7 studs): Symmetric parity - ODD if X < 8, EVEN if X >= 8.

### 3.3 Generation Logic
A contact is generated at a coordinate `(x_stud, z_stud)` if:
1. The track `z_stud` is valid (even).
2. The parity of `x_stud` matches the rule for that track.
3. The center of the stud `(x_stud * 20 + 10, z_stud * 20 + 10)` in LDU is geometrically contained within a LEF `RECT` defined for a `PIN` or `OBS` (Obstruction) on the `Metal1` layer.
4. For signal tracks (Z=2..12), the contact is either within an `Active` region or on the `Gate Track` (Z=6).

## 4. Layer Stacking (V3)
- Y=0: Substrate base
- Y=-8: Substrate high / N-Well
- Y=-16: Active / Diffusion
- Y=-24: Polysilicon / Gates
- Y=-48: Contact Brick (3062b.dat)
- Y=-56: Metal 1 / Rails
- Y=-64: Metal 2 Connection Plates (3070.dat)
