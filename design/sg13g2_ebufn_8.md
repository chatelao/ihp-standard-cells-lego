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
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2        GG G G G     G G G G G G   GG GG  G
1        GG G G G     G G G G G G   GG GG  G
0        GG G G G   G G G G G G G   GG GGG G
9        GG G G G   G G G G G G G   GG GGG G
8        GG G G G   G G G G G G G   GG GGG G
7        GG G G G   G G G G G G G   GG GGG G
6        GG G G G   G G G G G G G   GGGGGGGG
5        GG G G G   G G G G G G G   GG GGG G
4        GG G G G     G   G G G G   GG GG  G
3        GG G G G     G   G G G G   GG GG  G
2        GG G G G     G   G G G G   GG GG  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3                   +  +   +   +         +   +
2  cCcCcCccCcCcCcCc &  +   +   +  c      +   +
1  C  C   C   C   C +C + C + CCCCC       + C +
0  cO C O c o c o cCcCcCcCcCcCc c cCcCcCcCcC +
9  CO   O   O   O CCCCCCCCCCCCCCCCC        CCC
8  cOoOoOooOoOoOo c       c         cCcC    cC
7    O  CCCCCCCCCCC                 C        C
6    o  CccCcCcCc  CcCcCcCcCcCcCcC  c iIi iI C
5  COOOOOOOOOOOOO CCCCC  C   C   C  C        C
4  cOo  Ooo o   o c _ c _C - C - Cc c cC -cCcC
3  C  C   C   C   C - C -C - C - C CCCCC - C -
2 CcCcCcCccCcCcCcCc _   _  -   -    c    -   -
1                   -   -  -   -         -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Internal2 | Internal3 | Internal4 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   | X | X | X |   | X |
| PMOS1 | X |   |   |   |   | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   | X |   | X |
| Poly10 |   |   | X | X |   | X | X |   |   |
| Poly11 |   |   |   |   | X |   | X |   |   |
| Poly12 |   |   |   |   | X |   | X |   |   |
| Poly2 |   |   |   |   | X |   | X |   | X |
| Poly3 |   |   |   |   | X |   | X |   | X |
| Poly4 |   |   |   |   | X |   | X |   | X |
| Poly5 |   |   |   |   | X |   | X |   |   |
| Poly6 |   |   |   |   | X |   | X |   |   |
| Poly7 |   |   |   |   | X |   | X |   |   |
| Poly8 |   |   |   |   | X |   | X |   |   |
| Poly9 |   |   |   |   | X |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | N | N |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |
