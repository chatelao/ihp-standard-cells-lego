# Design Documentation for sg13g2_and4_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
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
2 NNNNNNNNNNNNNN
1 NNpppppppppppN
0 NNpppppppppppN
9 NNpppppppppppN
8 NNNNNNNNNNpppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSnnnnnnnnnnnS
3 SSnnnnnnnnnnnS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2    G G G  G
1    G G G  G
0    G G G  G
9    G G G  G
8    G G G  G
7    G G G  GG
6    G G G GGG
5    G G G  G
4    G G G  G
3    G G G  G
2    G G G  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3   +  +   +
2   +  +   +
1   +C + C +  OO
0   +c + c +  oO
9  CCCCCCCCCC OO
8  c   c    c oO
7  C I I IIICC O
6  c i i iiIiC O
5  C           O
4  cC      -  oO
3  CC      -  OO
2          -
1          -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | A | B | C | X |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |
| NMOS2 |   |   |   |   |   |   | X |
| PMOS1 | X |   |   |   |   |   | X |
| PMOS2 |   | X |   |   |   |   |   |
| Poly1 | X |   |   | X |   |   |   |
| Poly2 | X |   |   |   | X |   |   |
| Poly3 | X |   |   |   |   | X |   |
| Poly4 | X |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O | O | O |
| PMOS1 | O | O | O | O |
| PMOS2 |   |   |   |   |
