# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnSSSSSnnnnnnSnnnnnnnSSnnnnnSSSSSSSSSSSSSSSSS
4 SnnnnnnSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSnnnSnnnnnS
3 SnnnnnnSnnnnnSSSSSSnnnnnnnSSnnnnnnnnnnnnnnnSnnnnnS
2 SSSSSSSSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3
2   GGG G G G G G G G G G G G G G G G G G G G
1   GGG G G G G G G G G G G G G G G G G G G G
0   GGG G G G G G G G G G G G G G G G G G G G
9   GGG G G G G G G G G G G G G G G G G G G G
8   GGG G G G G G G G G G G G G G G G G G G G
7   GGG G G G G G G G G G G G G G G G G G G G
6  GGGG G G G G G G G G G G G G G G G G G G G
5   GGG G G G G G G G G G G G G G G G G G G G
4   GGG G G G G G G G G G G G G G G G G G   G
3   GG  G   G G G G G G G G G G G G G G G   G
2   GG  G   G G G G G G G G G G G G G G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789
4 ++++++++++++++++++++++++++++++++++++++++++++++++++
3  +         +                           +    +   +
2 &+ CcCcCcC&+  c   cCcCcC&CcCcCcCcCcCcC&+    + & +
1  + C     C + CCCC                      + C  + O +
0  +cCcCc cCcCcCc c   cCcCcCcCcCc        + C  + o +
9  + CC   C     C C  CCC       CCC     C   C  + O +
8   cCc cCcCcCcCc c  CcCcCcCcCcCcCc cCcCcCcC    o
7    CC C II C  C C  C CCIII   CC C C    C C    O
6  i cC   iIiCcCc cCcC CiIiIcCcCcCc   c cC CcC  oOo
5    CCCCCCCCC CCCCC C  CIIIC  CCCCCCCCCCC  C   O
4    C  c c c   c  Cc   c c c c c        C- c - o -
3  CCC- C - C CCCCCC    CCCCC CCCCCCC-  CC- C - O -
2   c - _ - _CcCcCcCcCcCcC_CcCcCcCc c-_ c - _ - _ -
1     -   -                          -    -   -   -
0 --------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | VSS3 | VSS4 | VSS5 | CLK | D | RESET_B | Internal1 | Internal2 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |   |   |   |   | X |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| PMOS1 | X | X | X |   |   |   |   |   |   |   |   | X | X | X |
| Poly1 |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly10 |   | X |   |   |   |   | X |   | X |   |   | X | X |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly16 |   |   |   | X |   |   |   |   |   |   |   | X | X |   |
| Poly17 | X |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly18 |   |   |   |   |   |   |   | X |   |   |   | X |   |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   | X | X |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |   |   | X |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly3 | X |   |   |   |   | X |   |   |   |   | X | X |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly9 |   |   |   |   |   |   |   |   | X |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | W | O | O | O | E |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   | O | O | O | O | O | O | O |   | N |
| NMOS3 | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   | N |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   | O | O | O | E |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
