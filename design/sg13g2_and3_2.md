# Design Documentation for sg13g2_and3_2

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
2 Nppppppppppp
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
2  GG GGG G
1  GG GGG G
0  GG GGG G
9  GG GGG G
8  GG GGG G
7  GG GGG G
6  GG GGGGG
5  GG GGG G
4  GG GGG G
3  GG GGG G
2  GG GGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 ++++++++++++
3    +   +   +
2    +& &+& &+
1  C + C + O +
0  C + Cc+oOo
9  C   C    O
8  CcCcCcCc o
7  C  IIIIC O
6  c  IiIi  o
5  C       OO
4  Ci iI - Oo-
3  IIIII - O -
2  IiIiI_-_ _-
1        -   -
0 ------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | B | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   | X |   | X |
| PMOS1 | X |   |   | X | X |
| Poly1 |   |   | X | X |   |
| Poly2 | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
