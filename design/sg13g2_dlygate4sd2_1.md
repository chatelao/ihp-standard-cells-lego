# Design Documentation for sg13g2_dlygate4sd2_1

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
1 NppppppNpppppp
0 NppppppNpppppp
9 NppppppNpppppp
8 NNNNNNNNpppppp
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSnnnnnn
3 SnnnnnnSnnnnnn
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
2 GGG G GGG G G
1 GGG G GGG G G
0 GGG G GGG G G
9 GGG G GGG G G
8 GGG G GGG G G
7 GGG G GGG G G
6 GGGGG GGG G G
5 GGG G GGG G G
4 GGG G GGG G G
3 GGG G GGG G G
2 GGG G GGG G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 ++++++++++++++
3    +       +
2   &+  &   &+
1    +    C  + O
0 cC +  c c  +oO
9  CCCC C C    O
8   c c c cCcC O
7  II C C    C O
6  iIiC CccCcCcO
5     C C CC OOO
4 cCcCc c c   oO
3  C -  C    - O
2    -_ _   _-
1    -       -
0 --------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS2 | A | Internal1 | Internal2 | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS3 |   |   |   |   |   | X |   | X |
| PMOS1 |   |   |   |   |   | X |   | X |
| PMOS2 |   |   |   |   |   | X |   |   |
| Poly1 | X |   | X |   | X |   | X |   |
| Poly2 |   | X |   | X |   | X |   |   |
| Poly3 | X |   | X |   |   | X |   |   |
| Poly4 |   |   |   |   |   | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O |   |   |
| NMOS3 |   | O | O | O |
| PMOS1 |   | O | O | O |
| PMOS2 | O | O |   |   |
| PMOS3 |   |   |   |   |
