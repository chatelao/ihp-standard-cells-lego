# LEF to LDR Mapping Rulebook

This document defines the standardized transformation rules from LEF (Library Exchange Format) to LDR (LDraw) LEGO models for the IHP SG13G2 process.

## 1. Coordinate System Mapping
- 1 LEGO Stud = 0.27 µm.
- 1 LEGO Stud = 20 LDU (LDraw Units).
- LEF X maps to LDR X.
- LEF Y maps to LDR Z.
- Origin Offset: A +10 LDU (0.135 µm) offset is applied to the LEF Y / LDR Z axis to align the center of Stud 0 with the LEF origin. The LEF X / LDR X axis uses a direct mapping where Stud 0 center is at X=10 LDU, matching the LEF X=0 boundary.

## 2. Standard Cell Architecture
- Total Height: 15 studs (300 LDU).
- Power Rails: Located at Track 0 (VSS) and Track 14 (VDD), resulting in a 14-stud center-to-center distance.
- **Exceptions**: `sg13g2_nand2b_2` and `sg13g2_xor2_1` are hardcoded to 15 studs (300 LDU) wide to match their specialized golden designs, exceeding their 3.84 µm (14.2 stud) LEF definitions. They are also exempt from strict track alignment and parity rules in Section 3.

## 3. Contact Placement Rules
Contacts bridge the gap between Metal 1 and underlying layers (Active or Polysilicon). To ensure buildability and electrical consistency, contacts must follow these placement rules:

### 3.1 Track Alignment
Contacts are strictly permitted only on EVEN Z-tracks:
- **0**: VSS Rail
- **2, 4**: NMOS Active Region
- **6**: Input Gates (Standard)
- **8, 10, 12**: PMOS Active Region
- **14**: VDD Rail

**Power Fingers**: VDD and VSS pins may have contacts on internal tracks (2-12) if their Metal 1 layout extends into the cell. These internal contacts must follow the **Rail Parity** rule defined in Section 3.2.

### 3.2 Stud Parity (X-axis)
To maintain grid alignment and prevent illegal overlaps, contacts follow a strict parity rule on the X-axis:
- **VSS Contacts (All Tracks)**: MUST use ODD X-studs (1, 3, 5, ...).
- **VDD Contacts (All Tracks)**: MUST use EVEN X-studs (0, 2, 4, ...).
- **Signal Contacts (Active & Gate Tracks Z=2..12)**:
  - Small models (width <= 7): Always ODD (1, 3, 5, ...).
  - Big models (> 7 studs): Symmetric parity - ODD if X < 8, EVEN if X >= 8.

### 3.3 Generation Logic
To ensure robust electrical connectivity, every `Metal1` strip (rectangle) MUST have at least one contact. The generation logic uses a scoring and prioritization system:

1. **At Least One Contact Per Strip**: Every `RECT` on `Metal1` (for both `PIN`s and `OBS`tructions) is evaluated to find at least one valid stud.
2. **Prioritization (Scoring)**:
   - **Track Alignment**: Preferred on EVEN tracks (0, 2, 4, 6, 8, 10, 12, 14).
   - **Target Layer Match**: Pins marked as `is_gate` (Input) prioritize Track 6. Pins marked as `is_diff` (Output/Other) prioritize Tracks 2, 4, 8, 10, or 12.
   - **Parity Match**: Studs matching the `Stud Parity` rules (Section 3.2) receive a higher score.
3. **Connectivity Guarantee**: If a contact is placed, the generator automatically ensures the appropriate material (Polysilicon for gates, Active for diffusions) is present at the `Y=-24` and `Y=-16` layers respectively to complete the connection to the substrate or channel.
4. **Fallback**: If no studs within a rectangle satisfy the strict parity and track rules, the generator will select the highest-scoring available stud (e.g., relaxing parity or track requirements) to ensure at least one contact is placed.

## 4. Layer Stacking (V3)
- Y=0: Substrate base
- Y=-8: Substrate high / N-Well
- Y=-16: Active / Diffusion
- Y=-24: Polysilicon / Gates
- Y=-48: Contact Brick (3062b.dat)
- Y=-56: Metal 1 / Rails
- Y=-64: Metal 2 Connection Plates (3070.dat)
