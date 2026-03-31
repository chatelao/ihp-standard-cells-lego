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
3 pppppppppppppppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSSSSnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSSSSnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSSSSnnnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2 G G G GGG G G G G   G G G G G G G G G G G G
1 G G G GGG G G G G   G G G G G G G G G G G G
0 G G G GGG G G G G G G G G G G G G G G G G G
9 G G G GGG G G G G G G G G G G G G G G G G G
8 G G G GGG G G G G G G G G G G G G G G G G G
7 G G G GGG G G G G G G G G G G G G G G G G G
6 G G G GGG G G G G G G G G G G G G G G G G G
5 G G G GGG G G G G G G G G G G G G G G G G G
4 G G G GGG G G G G   G   G G G G G G G G G G
3 G G G GGG G G G G   G   G G G G G G G G G G
2 G G G GGG G G G G   G   G G G G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++++++++++++
3                   +  +   +   +         +   +
2  CcCcCcCcCcCcCcC& +  +&  +&  +& c     &+  &+
1  C  C   C   C   C +C + C + CCCCC       + C +
0 cCo c o c o c o cCcCcCcCcCcCc c cCcCcCcCcC +
9  CO   O   O   O CCCCCCCCCCCCCCCCC        CCC
8  CoOoOoOoOoOoOo c       c         cCcC    cC
7    O  CCCCCCCCCCC                 C        C
6    o  CccCcCcCc  CcCcCcCcCcCcCcC  c iIi iI C
5  COOOOOOOOOOOOO CCCCC  C   C   C  C        C
4 cCo   o o o   o c - c -C - C - Cc c cC -cCcC
3  C  C   C   C   C - C -C - C - C CCCCC - C -
2 cCcCcCcCcCcCcCcC_ - _ -  -_  -_   c   _-  _-
1                   -   -  -   -         -   -
0 --------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS2 | VSS3 | A | TE_B | Internal1 | Internal2 | Internal3 | Internal4 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   |   |   | X |   |   |   | X |
| NMOS3 |   |   |   |   |   |   |   |   |   | X |   |   |
| PMOS1 | X | X |   |   |   |   |   |   | X | X | X | X |
| Poly1 |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly10 |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly11 | X |   | X |   |   |   |   | X |   | X |   |   |
| Poly12 |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly13 | X |   | X |   |   |   |   | X |   | X |   |   |
| Poly14 |   |   |   |   |   |   |   | X |   | X | X |   |
| Poly15 |   |   |   |   |   |   |   |   | X | X |   |   |
| Poly16 |   |   |   |   |   |   | X |   | X | X |   |   |
| Poly17 | X |   | X |   |   |   | X |   |   | X |   |   |
| Poly18 |   |   |   |   |   | X |   |   |   | X |   |   |
| Poly19 | X |   | X |   |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   |   |   |   | X |   | X |   | X |
| Poly20 |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly21 | X |   |   |   |   |   |   | X |   | X |   |   |
| Poly3 |   |   |   |   |   |   |   | X |   | X |   | X |
| Poly4 |   |   |   |   |   |   |   | X |   | X |   | X |
| Poly5 |   |   |   |   |   |   |   | X |   | X |   | X |
| Poly6 |   |   |   |   |   |   |   | X |   | X |   | X |
| Poly7 |   |   |   |   |   |   |   | X |   | X |   | X |
| Poly8 |   | X |   | X |   |   |   | X |   | X |   |   |
| Poly9 |   |   |   |   | X |   |   | X |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O | E |   |   |   |   |   | O | O |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | O |   |   |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
