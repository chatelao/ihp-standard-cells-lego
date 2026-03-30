# Design Documentation for sg13g2_sdfrbpq_2

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSnnnnnnnSSSSSnnnnnnSnnnnnnnSnnnnnSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSnnnnnS
3 SnnnnnnnnnnnnnnnnSnnnnnnnSnnnnnSSSSSSnnnnnnnSnnnnnSnnnnnnSnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
4
3
2  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G
1  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G
0  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G
9  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G G
8  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G
7  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G
6  GGG GGGG G G G G G G G G G G G G G G G G G G G G G G G G
5  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G
4  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G
3  GG  GGGG G G G G G G   G   G G G G G G G G G G G G G G G
2  GG  GGGG G G G G G G   G   G G G G G G G G G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3     +        +     +         +                          +   +
2   & +CcCcCcCc+&   &+ CcCcCcC&+  &   cCcCcCcCcCcCcCcCcCcC+ & + &
1     +C      C+ CC  + C     C +CCCCC                     + OO+
0  Cc  C  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       + oO+
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   OO+
8  C   CcCc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcCoO+
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    C O
6  cIi cIii i cCcCcCcC Cc i iIi c cCcCcC CcIiIcCc cCc c  CcC Oo
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC C  O
4  Cc- CiIiIi cCc c    C  c c c     cC    c c cCc c        C- o -
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CC- O -
2    -_   c    -_     _ -   - _CcC_CcCcCcCcCcCcCcCcCc c-_ c - _ -
1    -         -        -   -                          -    -   -
0 ----------------------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VSS | VSS2 | VSS3 | VSS4 | CLK | RESET_B | SCD | SCE | Internal1 | Internal2 | Internal3 | Internal4 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS1 | X | X | X | X | X |   |   |   |   |   |   |   |   | X | X |   | X | X |
| Poly1 |   | X |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |
| Poly10 | X |   |   |   |   |   |   | X |   |   | X |   |   |   | X |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly12 |   |   | X |   |   |   |   |   | X |   |   |   |   |   | X |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly17 |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   | X |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X |   |
| Poly23 |   |   |   |   |   | X |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly24 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly25 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly26 |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly5 | X |   |   |   |   | X |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly8 |   |   |   |   |   |   | X |   |   |   |   |   |   |   | X |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 | Poly24 | Poly25 | Poly26 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | O | E |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | E |   |   |   |   |   |
| NMOS3 | O | O | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |
| NMOS5 |   |   |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   | N |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | O |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS8 |   |   |   |   |   |   |   |   |   |   | O | O | O | E |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
