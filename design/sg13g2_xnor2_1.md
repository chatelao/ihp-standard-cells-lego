# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 SNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 NNNNNNNNNNNNNN
2 NNNNNNpppppppN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SnnnnnnnnnnnnS
4 Snnnnnnnnnnnnn
3 Snnnnnnnnnnnnn
2 SSSSSSnnnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2    G   G G G
1    G G G G G
0    G G G G G
9    G G G G G
8   GG G G G G
7   GG G G G G
6   GGGGGGGGGGG
5   GGG  G GGG
4   GGG  G GGG
3   GGG  G GGG
2   GGGGGG GGG
1   GGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3 ++++++++++++++
2  ++   &+  o+&
1  ++ C ++ OO++
0  &+Cc &+ Oo+&
9  ++CC    OOO
8    C IIIIOoOOO
7    CIIIIII COO
6    CIiIiIiCcOO
5  --CCCCCCCCCOO
4  _-CcCcCCCc oO
3  --CC CCCCCCOO
2  --     _-  o
1 --------------
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Y | VSS | Internal1 | A |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 | X | X | X |   |
| PMOS1 | X |   | X |   |
| PMOS2 | X |   |   |   |
| Poly1 |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

