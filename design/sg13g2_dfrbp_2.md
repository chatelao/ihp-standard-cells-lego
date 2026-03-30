# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
2 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnSSSSSnnnnnnSnnnnnnnSSnnnnnSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSnnnnnnnSnnnnn
3 SnnnnnnSnnnnnSSSSSSnnnnnnnSSnnnnnnnnnnnnnnnnnnnSnnnnn
2 SSSSSSSSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3
2   GGG G G G G G G G G G G G G G G G G G     G
1   GGG G G G G G G G G G G G G G G G G G     G
0   GGG G G G G G G G G G G G G G G G G G     G
9   GGG G G G G G G G G G G G G G G G G G     G
8   GGG G G G G G G G G G G G G G G G G G     G
7   GGG G G G G G G G G G G G G G G G G G     G G
6  GGGG G G G G G G G G G G G G G G G G G     G G
5   GGG G G G G G G G G G G G G G G G G G     G G
4   GGG G G G G G G G G G G G G G G G G G     G G
3   GG  G   G G G G G G G G G G G G G G G       G
2   GG  G   G G G G G G G G G G G G G G G       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 +++++++++++++++++++++++++++++++++++++++++++++++++++++
3  +         +                           +  +   +   +
2 &+ CcCcCcC&+  c   cCcCcCcC&CcCcCcCcCcC&+  + & + & + &
1  + C     C + CCCC                      + O+   + OO+
0  +cCcCc cCcCcCc c   cCcCcCcCcCc        + O+ cC+ oO+
9  + CC   C     C C  CCC       CCC     C   O+ CC+ OO+
8   cCc cCcCcCcCc c  CcCcCcCcCcCcCc cCcCcCoO+ cC+ oO+
7    CC C II C  C C  C CCIII   CC C C    C O   C   O
6  i cC   iIiCcCc cCcC CiIiIcCcCcCc   c cC Oo  CcC Oo
5    CCCCCCCCC CCCCC C  CIIIC  CCCCCCCCCCC  O   C   OOO
4    C  c c c   c  Cc   c c c c c        C  o   c - oOo
3  CCC- C - C CCCCCC    CCCCC CCCCCCC-  CC- O - C - O -
2   c - _ - _CcCcCcCcCcCcCcC_CcCcCc c-_ c - _ - _ - _ -
1     -   -                          -    -   -   -   -
0 -----------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VSS | VSS2 | VSS3 | VSS4 | VSS6 | CLK | D | RESET_B | Internal1 | Internal2 | Internal3 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   | X |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| PMOS1 | X | X | X | X | X |   |   |   |   |   |   |   |   | X | X | X | X | X |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   | X |   |   |
| Poly11 |   | X |   |   |   |   |   |   | X |   |   |   |   | X |   | X |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly16 |   |   |   |   |   | X |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly17 | X |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |
| Poly2 |   |   |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly20 |   |   | X |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly3 | X |   |   |   |   |   |   | X |   |   |   |   | X | X |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | W | O | O | O | E |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   | O | O | O | O | O | O | O |   | O |
| NMOS3 | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   | N |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   | O | O | O | E |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | S | O | O |
