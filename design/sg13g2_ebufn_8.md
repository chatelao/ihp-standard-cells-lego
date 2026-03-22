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
2 NNNNNNNNNNNNNNNNNNpNNNpNNNpNNNNNNNNppppppppp
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNppppppppp
0 NNNpNNNpNNpNNNpNNNNNNNNNNNNNNNNNNNNppppppppp
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNppppppppp
8 NNNpNpNppNpNpNpNNNNNNNNNNNNNNNNNNNNppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSnSSSnnSnSSSnSSSSSSSSSSnSSSnSSSSSnnnnnnnnn
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnnn
2 SSSSSSSSSSSSSSSSSnSSSnSSSnSSSnSSSSSnnnnnnnnn
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2                                     G G G G
1                                     G G G G
0                                     G G G G
9                                     G G G G
8                                     G G G G
7                                     G G G G
6                                     GGG GGG
5                                     G G G G
4                                     G G G G
3                                     G G G G
2                                     G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3                   +  +   +   +         +   +
2  cCcCcCccCcCcCcCc &  +&  +&  +  c      +   +
1  C  C   C   C   C   C+ C + CCCCC       + C +
0  cOoCcOoc o c o cCcCcCcCcCcCc c cCcCCCCCCC +
9  CO   O   O   O CCCCCCCCCCCCCCCCCC       CCC
8  cOoOoOooOoOoOo c       c         cCCC     C
7    O  CCCCCCCCCCC                 C        C
6    O  CccCcCcCc CCcCcCcCcCcCcCcC  c iIi iI C
5   OOOOOOOOOOOOO C   C   C  C   C  C        C
4  cOo  Ooo o   o c - c - c_ Cc_ Cc c  C _ CCC
3  C  C   C   C   C - C - C- C - C CCCCC - C -
2  cCcCcCccCcCcCcCc_-  _-  _   _    c    _   _
1                   -   -  -   -         -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | TE_B | Z | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS10 |   |   | X |   |   |
| NMOS11 |   |   |   |   | X |
| NMOS12 |   |   |   |   | X |
| NMOS2 |   |   |   |   | X |
| NMOS3 |   |   |   |   | X |
| NMOS4 |   |   |   |   | X |
| NMOS5 |   |   |   |   | X |
| NMOS6 |   |   |   |   | X |
| NMOS7 |   |   | X |   |   |
| NMOS8 |   |   | X |   |   |
| NMOS9 |   |   | X |   |   |
| PMOS1 |   |   | X |   |   |
| PMOS10 |   |   | X |   |   |
| PMOS11 |   |   | X |   |   |
| PMOS12 |   |   |   | X |   |
| PMOS13 |   |   |   | X |   |
| PMOS14 |   |   |   | X |   |
| PMOS15 |   |   |   | X |   |
| PMOS2 |   |   | X |   |   |
| PMOS3 |   |   | X |   |   |
| PMOS4 |   |   | X |   |   |
| PMOS5 |   |   | X |   |   |
| PMOS6 |   |   | X |   |   |
| PMOS8 |   |   | X |   |   |
| PMOS9 |   |   | X |   |   |
| Poly1 |   | X |   |   |   |
| Poly2 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 |   |   |
| NMOS3 |   |   |
| NMOS4 |   |   |
| NMOS5 |   |   |
| NMOS6 | O | O |
| NMOS7 |   |   |
| NMOS8 |   |   |
| NMOS9 |   |   |
| NMOS10 |   |   |
| NMOS11 |   |   |
| NMOS12 |   |   |
| PMOS1 |   |   |
| PMOS2 |   |   |
| PMOS3 |   |   |
| PMOS4 |   |   |
| PMOS5 |   |   |
| PMOS6 |   |   |
| PMOS7 | O | O |
| PMOS8 |   |   |
| PMOS9 |   |   |
| PMOS10 |   |   |
| PMOS11 |   |   |
| PMOS12 |   |   |
| PMOS13 |   |   |
| PMOS14 |   |   |
| PMOS15 |   |   |
