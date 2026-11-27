# Design Documentation for sg13g2_nor2b_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 SNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 NNNNNNNNN
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 NNNppppNN
1 NpppppppN
0 ppppppppN
9 ppppppppN
8 ppppppppN
7 NNNNNNNNN
6 SSSSSSSSS
5 SnnnnnnnS
4 nnnnnnnnn
3 nnnnnnnnn
2 SSSnnnnnS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2     GGG
1   G GGG
0   G GGG
9   G GGG
8   G GGG
7   G GGG
6  GGGGGGG
5   G G G
4   G G G
3   G G G
2   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3 +++++++++
2    &+ oO
1  C ++ OO
0  c &+ oO
9  C   OOO
8  cCCCOoO
7    CCO
6  i cCOiI
5  CCCCO -
4  cCCCo _
3    --O -
2    _-o _
1 ---------
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Y | A | B_N |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   |   |
| PMOS1 | X |   | X | X |   |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

