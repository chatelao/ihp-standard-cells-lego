# Design Documentation for sg13g2_einvn_2

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
1 SSnnnnnnnnSSSSSS
0 SSnnnnnnnnSSSSSS
9 SSnnnnnnnnSSSSSS
8 SSnnnnnnnnSSSSSS
7 SSnnnnnnnnSSSSSS
6 SSnnnnnnnnSSSSSS
5 SSnnnnnnnnSSSSSS
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
2   GGGGGGGG GGGG
1   GGGGGGGG GGGG
0   GGGGGGGG GGGG
9   GGGGGGGG GGGG
8   GGGGGGGG GGGG
7   GGGGGGGG GGGG
6   GGGGGGGG GGGG
5   GGGGGGGG GGGG
4   GGGGGGGG GGGG
3   GGGGGGGG GGGG
2   GGGGGGGG GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &&&&&&&&&&&&&&&&
3 ++++++++++++++++
2 +++&+++&++&+++&+
1 ++++++++++++++++
0 +++&+&+&++&+&+&+
9     CCOOOOOOoOO
8  iiiICOOOOOOoO
7  iiiIC      c
6  iiiIc      c i
5  iiiIC      c c
4  IIIIC-__-_-_-_
3 ----------------
2 ---_---_--_---_-
1 ----------------
0 ________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Z |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 | X |   |   | X | X | X |
| PMOS1 | X |   |   |   |   |   |
| Poly1 | X | X |   | X | X | X |
| Poly2 | X | X | X |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 |   |   |
