# Design Documentation for sg13g2_ebufn_8

## Substrate
```
  01234567890123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNpNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNpNNNNNNNNNNNNNN
1 NpppppppppppppppppppppppppppppppNNNNNppppppp
0 NpppppppppppppppppppppppppppppppNNNNNppppppp
9 NpppppppppppppppppppppppppppppppNNNNNppppppp
8 NpppppppppppppppppppppppppppppppNNNNNppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSSSSnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSSSSnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSSSSnnnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2    G G GGGGGGGG   G G G G G G G G G G G G
1    G G GGGGGGGG   G G G G G G G G G G G G
0    G G GGGGGGGG   G G G G G G G G G G G G
9    G G GGGGGGGG   G G G G G G G G G G G G
8    G G GGGGGGGG   G G G G G G G G G G G G
7   GGGGGGGGGGGGG  GGGGGGGGGGGGGGGGGGGGGG G
6   GGGGGGGGGGGGG   G G G G G G G G G GGG GG
5    G G GGGGGGGG  GGGG G G G G G GGG G G G
4    G G GGGGGGGG  GGGG G G G G G GGG G G G
3    G G GGGGGGGG  GGGG G G G G G GGGGG G G
2    G G GGGGGGGG  GGGG G G G G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3                   +  +   +   +         +   +
2  cCcCcCccCcCcCcCc +  +   +   +  c      +   +
1  C  C   C   C   C +C + C + CCCCC       + C +
0  cO C O c o c o cCcCcCcCcCcCc c cCcCcCcCcC +
9  CO   O   O   O CCCCCCCCCCCCCCCCC        CCC
8  cOoOoOooOoOoOo c       c         cCcC    cC
7    O  CCCCCCCCCCC                 C        C
6    o  CccCcCcCc  CcCcCcCcCcCcCcC  c iIi iI C
5  COOOOOOOOOOOOO CCCCC  C   C   C  C        C
4  cOo  Ooo o   o c - c -C - C - Cc c cC -cCcC
3  C  C   C   C   C - C -C - C - C CCCCC - C -
2 CcCcCcCccCcCcCcCc -   -  -   -    c    -   -
1                   -   -  -   -         -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Internal2 | Internal3 | Internal4 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   | X |   |   |   | X |
| NMOS3 |   |   |   |   |   |   | X |   |   |
| PMOS1 | X |   |   |   |   |   | X |   | X |
| PMOS2 |   |   |   |   |   |   | X |   |   |
| Poly1 |   |   |   |   | X |   | X |   | X |
| Poly2 |   |   |   | X | X | X | X | X |   |
| Poly3 |   |   | X |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| NMOS3 |   | O | O |
| PMOS1 | O | O |   |
| PMOS2 |   | O | O |
