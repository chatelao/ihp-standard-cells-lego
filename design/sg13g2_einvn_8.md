# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4 ppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 ppppNNNNpNpNNNpNNNpNNNNNNpppppNNNNNNNNN
1 ppppNNNNNNNNNNNNNNNNNNNNNpppppNNNNNNNNN
0 ppppNNNNNNNNNNNNNNpNNNNNpppppppNNNpNNNN
9 ppppNNNNNNNNNNNNNNNNNNNNNpppppNNNNNNNNN
8 ppppNNNNNNNNNNNNNNNNNNNNpppppppNpNpNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnSSSSSSSSSSSSSSSnSSSSnnnnnnnSSSnSSSS
3 nnnnSSSSSSSSSSSSSSSSSSSSSnnnnnSSSSSSSSS
2 nnnnSSSSSnSnSSSnSSSnSSSSSnnnnnSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678
4
3
2 G G                       G G
1 G G                       G G
0 G G                       G G
9 G G                       G G
8 G G                       G G
7 G G                       G G
6 GGG                       GGG G G G
5 G G                       G G
4 G G                       G G
3 G G                       G G
2 G G                       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +     +   +   +  +
2  +     +& &+  &+  &  CcCcCCCCCcCcCcCc
1  + C C + C + C + C+  C   C   C   C  C
0  + C c +cC +cC +cC&  CcOoC O CoOcCoOc
9  + C C + C + C + CCCCC O   O   O   OC
8  + C cCCCCcCCCCCCCc    OoOOOOOoOoOoO
7    C                   OOO
6  I c  CccCcCcCcCcCcCcC OOO  iIiIiIiI
5    CCCC   C   C   C  C OOOOOOOOOOOOO
4  _ CCcCc- c - c - c_ CcOo  O  oO  oOc
3  - CCCC - C - C - C- CCCCCCCCC   C  C
2  _      -_ _-  _-  _    c    CcCcCcCc
1  -      -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Z | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   | X |   |   |
| NMOS8 |   |   |   | X |
| NMOS9 |   | X |   |   |
| PMOS10 |   |   | X |   |
| PMOS11 |   |   | X |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   |   | X |   |
| PMOS6 |   | X |   |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |
| PMOS9 |   |   | X |   |
| Poly2 | X |   |   |   |
| Poly3 | X |   |   |   |
| Poly4 | X |   |   |   |
| Poly5 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |
| NMOS3 |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |
| NMOS5 |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |
| NMOS7 |   | O |   |   |   |
| NMOS8 |   |   |   |   |   |
| NMOS9 |   |   |   |   |   |
| PMOS1 | O |   |   |   |   |
| PMOS2 |   | O |   |   |   |
| PMOS3 |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |
| PMOS5 |   |   |   |   |   |
| PMOS6 |   |   |   |   |   |
| PMOS7 |   |   |   |   |   |
| PMOS8 |   |   |   |   |   |
| PMOS9 |   |   |   |   |   |
| PMOS10 |   |   |   |   |   |
| PMOS11 |   |   |   |   |   |
