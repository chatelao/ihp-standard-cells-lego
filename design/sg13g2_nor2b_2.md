# Design Documentation for sg13g2_nor2b_2

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
1 Nppppppppppp
0 Nppppppppppp
9 Nppppppppppp
8 Nppppppppppp
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 Snnnnnnnnnnn
4 Snnnnnnnnnnn
3 Snnnnnnnnnnn
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
2  GG G G G
1  GG G G G
0  GG G G G
9  GG G G G
8  GG G G G G
7  GG G G G G
6  GG G G G G
5  GG G G G
4  GG G G G
3  GG G G G
2  GG G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 ++++++++++++
3    +       +
2   &+  &   &+
1  C + CCCCC +
0  C +cC OcC +
9  C +   O C +
8  C   OoO
7  CCC O  III
6  i   o  iIi
5  C - OOOOO -
4    -oOo oO -
3  I - O - O -
2  I_-  _-  _-
1    -   -   -
0 ------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | A | B_N | Internal1 | Internal2 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   |   |   | X |
| PMOS1 |   |   |   |   |   |   | X | X |
| Poly1 | X |   | X |   | X | X |   |   |
| Poly2 |   |   |   |   |   |   | X | X |
| Poly3 |   | X | X |   |   |   | X | X |
| Poly4 |   |   |   | X |   |   | X | X |
| Poly5 |   |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O | N |
| PMOS1 | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |
