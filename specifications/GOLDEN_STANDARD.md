# Gold Standard Specifications

This document defines the "Gold Standard" for IHP SG13G2 LEGO models. These rules ensure consistency, physical buildability, and accurate representation of the semiconductor process.

## 0. Rules
- **NEVER override ANY file in /handmade.** These sections are the source of truth for validated designs and must be preserved across all automated script runs.
- **Reference each GOLDEN STANDARD chapter in this file.** Every section marked as "GOLDEN STANDARD" in the individual /handmade files must be automatically mirrored to Section 7 of this document.

## 1. Physical Dimensions & Scaling
- **Total Cell Height (Z-axis):** 15 studs (300 LDU).
- **Rail-to-Rail Distance:** 14 studs center-to-center (matching the 3.78 µm LEF height).
- **Conversion Factor:** 1 LEGO stud = 20 LDU = 0.27 µm.
- **Alignment Offset:** A +10 LDU (0.135 µm) offset is applied to align LEF coordinates with LEGO stud centers.

*Referenced in:* [MAPPING_RULEBOOK.md](specifications/MAPPING_RULEBOOK.md), [verify_macro_dimensions.py](scripts/verify_macro_dimensions.py)

## 2. Layer Stacking (V3)
- **Y=0:** Substrate base (Dark Gray, 8)
- **Y=-8:** Substrate high / N-Well (Light Gray, 7)
- **Y=-16:** Active Regions / Diffusion
- **Y=-24:** Polysilicon Gates (Red, 4)
- **Y=-48:** Contact Bricks (White, 15)
- **Y=-56:** Metal 1 / Rails

*Referenced in:* [verify_models_v3.py](scripts/verify_models_v3.py)

## 3. Active Region Positioning
- **NMOS Diffusion:** Spans Studs 2 to 4 (Z=40 to 100).
- **PMOS Diffusion:** Spans Studs 8 to 12 (Z=160 to 260).
- **N-Well Split:** Occurs at Stud 8 (Z=160).

*Referenced in:* [lef_to_ldr.py](scripts/lef_to_ldr.py)

## 4. Contact Parity Rules
To ensure consistent staggered patterns:
- **VDD Rail (Z=14):** EVEN studs.
- **VSS Rail (Z=0):** ODD studs.
- **NMOS Contacts:** Always EVEN studs.
- **PMOS Contacts:**
  - Drive-1 cells: ODD studs.
  - Drive-2 and "Big" models: EVEN studs.
- **Input Contacts (Z=6):**
  - Small models (width <= 7): Always ODD.
  - Big models (width > 7): Symmetric parity (ODD if X < 8, EVEN if X >= 8).

*Referenced in:* [lef_to_ldr.py](scripts/lef_to_ldr.py), [verify_models_v3.py](scripts/verify_models_v3.py)

## 5. ASCII Art Nomenclature
Design documentation uses lowercase characters to denote contacted Metal 1:
- `i`: Contacted Input
- `o`: Contacted Output
- `c`: Contacted Internal Connection
- `&`: Contacted VDD (+ is uncontacted)
- `_`: Contacted VSS (- is uncontacted)

*Referenced in:* [generate_design_docs.py](scripts/generate_design_docs.py)

## 6. Implementation & Enforcement
These standards are strictly enforced by the following scripts:
- **Generation:** [lef_to_ldr.py](scripts/lef_to_ldr.py)
- **Documentation:** [generate_design_docs.py](scripts/generate_design_docs.py)
- **Verification:** [verify_models_v3.py](scripts/verify_models_v3.py)

