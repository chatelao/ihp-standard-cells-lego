# Design Documentation for sg13g2_and3_1

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
2 Nppppppppppp
1 Nppppppppppp
0 Nppppppppppp
9 Nppppppppppp
8 NNNNNNNNpppN
7 NNNNNNNNNNNN
6 SSSSSSSSSSSS
5 SnnnnnnnnnSS
4 SnnnnnnnnnSS
3 SnnnnnnnnnSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2   GGG G  G
1   GGG G  G
0   GGG G  G
9   GGG G  G
8   GGG G  G
7   GGGGGGGG
6   GGG GGGG
5   GGG G G
4   GGG G G
3  GGGG G G
2  GGGG G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3 ++++++++++++
2  c &+c &&+o
1  CC++CC+++OO
0  cC&+cC&&+oO
9  CC  CC   OO
8  CCCCCCCC oO
7  CC IIIICCOO
6  CC iIIiCcOO
5  CC      OOO
4  c  II _-oO
3  IIIII --O
2  iIiII --
1 ------------
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | X | A | B |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   |   |
| PMOS1 | X |   | X | X |   |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 | X |   | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

