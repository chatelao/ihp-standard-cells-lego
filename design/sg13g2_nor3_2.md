# Design Documentation for sg13g2_nor3_2

## Substrate
```
  0123456789012345
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SnnnnnnnSSSSSSSS
0 SnnnnnnnSSSSSSSS
9 SnnnnnnnSSSSSSSS
8 SnnnnnnnSSSSSSSS
7 SnnnnnnnSSSSSSSS
6 SnnnnnnnSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456789012345
4
3
2   GGG GGGG GGG
1   GGG GGGG GGG
0   GGG GGGG GGG
9   GGG GGGG GGG
8   GGG GGGG GGG
7   GGG GGGG GGG
6   GGG GGGG GGG
5   GGG GGGG GGG
4   GGG GGGG GGG
3   GGG GGGG GGG
2   GGG GGGG  GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &&&&&&&&&&&&&&&&
3 ++++++++++++++++
2 +++&++++++++++++
1 ++++++++++++++++
0 +++&+++&&+&+&+&+
9 ++++++++++++++++
8 +++&++++&+++&+&+
7   IIIOOOOOOOII
6   iiIOoioooOii
5 ----------------
4 ---_-_-__-_-_---
3 ----------------
2 ----------------
1 ----------------
0 ________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | C | Y |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 | X |   | X | X |   | X |
| PMOS1 | X |   |   |   |   |   |
| Poly1 | X | X | X |   |   | X |
| Poly2 | X | X |   | X |   | X |
| Poly3 | X | X |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 |   |   |   |
