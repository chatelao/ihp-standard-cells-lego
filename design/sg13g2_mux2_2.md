# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 NNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4 pppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNppppppN
1 NppppppppppppppppppN
0 NppppppppppppppppppN
9 NppppppppppppppppppN
8 NppppppppppppppppppN
7 NNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnnnnnS
4 SnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnS
2 SSSnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789
4
3
2      G G  G G G  G
1   G GG GGGG G G  G
0   G GG GGGG G G  G
9   G GG GGGG G G  G
8   G GG GGGG G G  G
7   GGGG GGGG GGGG G
6   GGGGGGGGG GGGGGG
5   G GGG GGG G G  G
4   G GGG GG  G G  G
3   G GGG GG  G G  G
2   G GGG GG  G G  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 &+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++
2    ++CCCCCCCC++Oo +
1  C ++C      C++OOO+
0  cCC&C  cC  C&+OoO&
9  CCCCCCCCC  C++OOO+
8  c  CCCC    C&+OoO&
7  CIICC    I CC COO
6  CIiCCi i iICcCcOO
5  C  CCI   IICCCCOO
4  cC_CCIIIIIICCC oO_
3    -CCCCCCCCC-- OO-
2    _ CCcCCCC _- o _
1 --------------------
0 _-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | S | X | A0 | A1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   |   |
| PMOS1 | X |   | X | X |   |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 | X |   | X |   | X | X |
| Poly2 |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |

