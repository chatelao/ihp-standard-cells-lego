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
2 NNNNNNNppppp
1 Nppppppppppp
0 Nppppppppppp
9 Nppppppppppp
8 NNNNNNNNNNNN
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
2  G G GGGG G
1  G G GGGG G
0  G G GGGG G
9  G G GGGG G
8  G G GGGG G
7  G GGGGGGGG
6  G G GGGG G
5  G G GGGG G
4  G G GGGG G
3  G G GGGG G
2  GGG G GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +   +   +
2    +   +   +
1  C + C + O +
0  c + c +oOo
9  C   C    O
8  cCcCcCcc o
7  C  IIIIC O
6  c  IiIi  o
5  C       OO
4  c  Ii - Oo-
3  IIIII - O -
2  iIiIi -   -
1        -   -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | C | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   | X |   | X | X |
| PMOS1 |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
