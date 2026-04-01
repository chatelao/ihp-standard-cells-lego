# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
9 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
8 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2      G GG GGGGGGGGGGGGGGGGGGGG
1   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
0   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
9   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
8   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
7   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
6   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
5   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
4   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
3   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
2     GGGGGGGGGGGGGGGGGGGGGGGGGG
1                   GG   GGGGG G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++
2 +++&++++++++++++++++++++&+++++&+
1 ++++++++++++++++++++++++&&----&+
0 +&++++++++&++-_---_+&+++&&_---&+
9 +++++++++++++------+++++&&----&+
8  IIIIiI+&++++-_----IiIIIIO----o
7  IIiIiI++++++------IIIIIIO----O
6  IIiIiI&++&+&-----_IIiiIiO--_-O
5  IIIIII++++++------IIiIIIO----O
4 -_---_--_-----_-_-_-_---_-_---_-
3 --------------------------------
2 -----_--------_---_-_---_-_---_-
1 --------------------------------
0 ________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | GATE | Q | Q_N |
| --- | --- | --- | --- | --- | --- |
| NMOS1 | X | X | X | X | X |
| NMOS2 | X | X | X | X | X |
| PMOS1 | X |   |   |   |   |
| Poly1 | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| NMOS2 | O |
| PMOS1 |   |
