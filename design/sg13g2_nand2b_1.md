# Design Documentation for sg13g2_nand2b_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
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
2 NNNNNNNNN
1 NNNppppNN
0 NppppppNN
9 NppppppNN
8 NppppppNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SnnnnnnnS
3 SnnnnnnnS
2 SSSSSSSSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2
1
0
9
8
7
6  G G  G
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3    +  +
2    +  +
1    +O +
0  C +OoOO
9  C     O
8 CCCCCC O
7      C O
6  i iICCO
5 CCCCCC O
4  C    Oo
3    -  OO
2    -
1    -
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A_N | B | Y |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   |   |   |   | X |
| PMOS1 |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   | X |   |   |
| Poly2 |   |   |   | X |   |
| Poly3 |   |   |   |   |   |

