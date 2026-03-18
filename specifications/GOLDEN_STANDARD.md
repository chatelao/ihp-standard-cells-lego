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

*Referenced in:* [MODELING_GUIDELINES.md](specifications/MODELING_GUIDELINES.md), [verify_macro_dimensions.py](scripts/verify_macro_dimensions.py)

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

## 7. Golden Design Examples
### sg13g2_a21o_1 - Active
GOLDEN STANDARD

```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NppppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SnnnnnnnnnnS
3 SnnnnnnnnnnS
2 SnnnnnnnnnnS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

### sg13g2_a21o_1 - Metal 1
GOLDEN STANDARD

```
  012345678901
4 &+&+&+&+&+&+
3    +     +
2  o & c c & c
1  O + C C + C
0  o + c c & c
9  O + C C   C
8  o + c cCCCc
7  O   C
6  OcCCCi i
5  O   CCC --_
4  O     C -
3  OOo   c -
2      _   -iI
1      -   -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

### sg13g2_a21o_1 - Polysilicon
GOLDEN STANDARD

```
  012345678901
4
3   G   G G G
2   G   G G G
1   G   G G G
0   G   G G G
9   G   G G G
8   G   G G G
7   G   G G G
6   GGG G G G
5     G G G G
4     G G G G
3     G G G G
2     G G G G
1     G G G G
0
```
Legend: G=Polysilicon

### sg13g2_a21o_1 - Substrate
GOLDEN STANDARD

```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

### sg13g2_inv_1 - Metal 1
GOLDEN STANDARD

```
  01234
4 &&&&&
3  +
2  & o
1  + O
0  & o
9  + O
8  & o
7    O
6  i O
5    O
4  _ o
3  - O
2  _ o
1  -
0 _____
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

### sg13g2_nand2b_2 - Active
GOLDEN STANDARD

```
  012345678901234
4 ppppppppppppppp
3 NNNNNNNNNNNNNNN
2 NpppppppppppppN
1 NpppppppppppppN
0 NpppppppppppppN
9 NpppppppppppppN
8 NpppppppppppppN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

### sg13g2_nand2b_2 - Metal 1
GOLDEN STANDARD

```
  012345678901234
4 &+&+&+&+&+&+&+&
3 +   +    +   +
2 +   & o  & o &
1 &   + O  + O +
0 + c & o  & o &
9 & C + OOOOOO +
8   c &      o &
7   C        O
6  iCc     IiO
5    C       O
4 _  c cCcCc o c
3 -    C   C   C
2 -    c _ cCCCc
1 -      -
0 _-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

### sg13g2_nand2b_2 - Polysilicon
GOLDEN STANDARD

```
  012345678901234
4
3      G G  G G
2  G   G G  G G
1  G   G G  G G
0  G   G G  G G
9  G   G G  G G
8  G   G G  G G
7  G   G G  G G
6  G  GGGG  GGG
5  G   G G  G G
4  G   G G  G G
3  G   G G  G G
2  G   G G  G G
1      G G  G G
0
```
Legend: G=Polysilicon

### sg13g2_nand2b_2 - Substrate
GOLDEN STANDARD

```
  012345678901234
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate
