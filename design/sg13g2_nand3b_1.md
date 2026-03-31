# Design Documentation for sg13g2_nand3b_1

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
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
2 NNNNNNNNNNNN
1 NNNNpppppppN
0 NNpppppppppN
9 NNpppppppppN
8 NNpppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSnnnnnnnnnS
4 SSnnnnnnnnnS
3 SSnnnnnnnnnS
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
2    G G G G
1    G G G G
0    G G G G
9    G G G G
8    G G G G
7    G G G G
6    G G G G
5    G G G G
4    G G G G
3    G G G G
2    G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3     +   +
2     +   +
1     + O + OO
0  cC + Oo+ oO
9  CC + OOOOOO
8  c      o  O
7  C I I I   O
6  c i i icCcO
5  C       C O
4  cCcCcCccCoO
3     -     OO
2     -
1     -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A_N | B | C | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | X | X |
| PMOS1 |   |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   | X |   |
| Poly2 |   |   |   |   | X | X |   |
| Poly3 |   |   |   | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O | O | O |
| PMOS1 | O | O | O | O |
| PMOS2 |   |   |   |   |
