# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
9 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
8 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
7 SSnnnnnnSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456789012345678901234567
4
3
2    G G GG GGGGGGG GGGGGG GG
1   GGGG GGGGGGGGGGGGGGGGGGGG
0   GGGG GGGGGGGGGGGGGGGGGGGG
9   GGGG GGGGGGGGGGGGGGGGGGGG
8   GGGG GGGGGGGGGGGGGGGGGGGG
7   GGGG GGGGGGGGGGGGGGGGGGGG
6   GGGG GGGGGGGGGGGGGGGGGGGG
5   GGGG GGGGGGGGGGGGGGGGGGGG
4   GGGG GGGGGGGGGGGGGGGGGGGG
3   GGGG GGGGGGGGGGGGGGGGGGGG
2    G G GGGGGGGGGGGGGGGGGGGG
1        GG  GG  GG G GG G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++
2 ++++++++++++++++++++++&+++++
1 ++++++++++++++++++++++++++&+
0 +&+&+&++++&+++++&+++++&+++&+
9 +++++++++++++--------+++++&+
8 +&+&+&++&++++-_-_-_-_+++++&+
7  ++&+&++++++I--------IIiIIIO
6  ++&+&+&++&+i---_---_IIiiIIO
5  +++++++++++I--------IIiIIIO
4 -_---_--_-----------_-_---_-
3 ----------------------------
2 ---_------_-_---_-_-_-_---_-
1 ----------------------------
0 ____________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | RESET_B | Internal1 | Q |
| --- | --- | --- | --- | --- | --- |
| NMOS1 | X | X | X | X | X |
| NMOS2 | X | X | X | X | X |
| PMOS1 | X |   |   |   |   |
| Poly1 | X | X | X | X | X |
| Poly2 | X | X | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | O | O |
| NMOS2 | O | O |
| PMOS1 |   |   |
