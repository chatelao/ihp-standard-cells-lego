# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSnnnnnnnSSSSSnnnnnnSnnnnnnnSnnnnnSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSnnnnnnnSnnnnn
3 SnnnnnnnnnnnnnnnnSnnnnnnnSnnnnnSSSSSSnnnnnnnSnnnnnSnnnnnnSnnnnnnnSnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3
2  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G       G
1  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G       G
0  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G       G
9  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G G     G
8  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G
7  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G G
6  GGG GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G G
5  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G G
4  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G G
3  GG  GGGG G G G G G G   G   G G G G G G G G G G G G G G G       G
2  GG  GGGG G G G G G G   G   G G G G G G G G G G G G G G G       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3     +        +     +         +                          +   +   +   +
2   & +CcCcCcCc+&   &+ CcCcCcC&+  c   &CcCcCcCcCcCcCcCcCcC+ & + & + & + &
1     +C      C+ CC  + C     C +CCCCC                     + O +   + O +
0  Cc  C  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       + o + cC+ o +
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   O + CC+ O +
8  C   CcCc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcCo + cC+ o +
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    CO    C  O
6  cIi cIii i cCcCcCcC Cc i iIi c cCcCcC CcIiIcCc cCc c  CcCoOo  CcCoOo
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC C  O   C  OOO
4  Cc- CiIiIi cCc c    C  c c c     cC    c c cCc c        C  o   c -OoO
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CC- O - C - O-
2    -_   c    -_     _ -   - _CcCcCcC_CcCcCcCcCcCcCc c-_ c - _ - _ -  -_
1    -         -        -   -                          -    -   -   -  -
0 -----------------------------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VDD6 | VDD7 | VSS | VSS2 | VSS3 | VSS4 | VSS6 | CLK | RESET_B | SCD | SCE | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| NMOS9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS1 | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   |   | X | X |   | X | X | X | X |
| Poly1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |   |
| Poly10 | X |   |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   | X |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly14 |   |   | X |   |   |   |   |   |   |   | X |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   | X |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   | X |   |   |
| Poly23 |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly24 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly25 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   | X |   |   |   |
| Poly26 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly27 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   |   |   |
| Poly28 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly5 | X |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 | Poly24 | Poly25 | Poly26 | Poly27 | Poly28 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | O | E |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | E |   |   |   |   |   |   |   |
| NMOS3 | O | O | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | N |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | O |   |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |   | O |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS9 |   |   |   |   |   |   |   |   |   |   | O | O | O | E |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | S | O | O | O |
