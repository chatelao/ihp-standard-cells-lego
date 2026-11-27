# Design Documentation for sg13g2_nand3b_1

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 SNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 NNNNNNNNNNNN
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NNNNpppppppN
1 NNpppppppppN
0 NNpppppppppN
9 NNpppppppppN
8 NNpppppppppN
7 NNNNNNNNNNNN
6 SSSSSSSSSSSS
5 Snnnnnnnnnnn
4 Snnnnnnnnnnn
3 Snnnnnnnnnnn
2 SSSSnnnnnnnS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2      G G G
1    G G G G
0    G G G G
9    G G G G
8    G G G G
7    G G G G
6   GG GGG GG
5    G G G G
4    G G G G
3    G G G G
2      G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3 ++++++++++++
2     &+o & oO
1   C ++O +OOO
0  CcC&+o &OoO
9  CCC++OOOOOO
8  Cc & oOOOoO
7  CCI I I C O
6  CCi i i cCO
5  CC      C O
4  CcCCCCCCCoO
3     -     OO
2     _     oO
1 ------------
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Y | A_N | B | C |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   |   |
| PMOS1 | X |   | X | X |   |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   |   | X | X |
| Poly2 |   |   |   | X |   |   |
| Poly3 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O | O |
| PMOS1 | O | O | O |
| PMOS2 |   |   |   |

