# Design Documentation for sg13g2_dlygate4sd1_1

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
2 NNNppppNNNNppp
1 pppppppppppppp
0 pppppppppppppp
9 NNNppppppppppp
8 NNNppppppppppp
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSnnnnnn
4 SSSSSSSnnnnnnn
3 SnnnnnnSnnnnnn
2 SSSSSSSSSSSnnn
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2   G  G    G G
1   G  G    G G
0   G  G    G G
9   G  G    G G
8   G  G    G G
7   GGGG  GGGGG
6   GGGG GGGGGG
5   GGGG    G G
4   G  G    G G
3   G  G    G G
2   G  G      G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3 ++++++++++++++
2    ++     ++ c
1  C ++ C   ++CC
0 Cc &+Cc   +&Cc
9 CCCCCCC C  +CC
8  CCCCCC cCCC c
7  II CCCCC CC C
6  Ii cCCCcCCcCC
5     CCC CCCOOO
4 CCCCCCC cC  Cc
3 CC --CC   --CC
2  c _- c   -_ c
1 --------------
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | X | A |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X |   |
| NMOS3 |   |   |   |   |
| PMOS1 | X |   | X |   |
| PMOS2 | X |   |   |   |
| Poly1 |   |   | X | X |
| Poly2 |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 |   | O |
| NMOS3 | O |   |
| PMOS1 | O | O |
| PMOS2 |   |   |

