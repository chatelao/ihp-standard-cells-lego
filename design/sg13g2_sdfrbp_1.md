# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNpppppppppppppppppppppppppppppppppppppppppppppppppp
2 NNNNNNNNNNNNNNNNNNpppppppppppppppppppppppppppppppppppppppppppppppppp
1 NppppppppppppppppNpppppppppppppppppppppppppppppppppppppppppppppppppp
0 NppppppppppppppppNpppppppppppppppppppppppppppppppppppppppppppppppppp
9 NppppppppppppppppNpppppppppppppppppppppppppppppppppppppppppppppppppp
8 NppppppppppppppppNpppppppppppppppppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSnnnnnnnSSSSSnnnnnnSnnnnnnnSnnnnnSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSnnnnnSnnnS
3 SnnnnnnnnnnnnnnnnSnnnnnnnSnnnnnSSSSSSnnnnnnnSnnnnnSnnnnnnSnnnnnSnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3
2  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G       G
1  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G       G
0  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G       G
9  GG  GGGG G G G G   G G G G G G G G G G G G G G G G G G G     G
8  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G
7  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G
6  GGG GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G
5  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G
4  GG  GGGG G G G G G G G G G G G G G G G G G G G G G G G G     G
3  GG  GGGG G G G G G G   G   G G G G G G G G G G G G G G G     G
2  GG  GGGG G G G G G G   G   G G G G G G G G G G G G G G G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3     +        +     +         +                          +   +   +
2   & +CcCcCcCc+&   &+ CcCcCcC&+  c & cCcCcCcCcCcCcCcCcCcC+ & + & + &
1     +C      C+ CC  + C     C +CCCCC                     + O +   + O
0  Cc  C  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       + o + c + o
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   O + C + O
8  C   CcCc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcCo + c   o
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    CO   C   O
6  cIi cIii i cCcCcCcC Cc i iIi c cCcCcC CcIiIcCc cCc c  CcCo   cC Oo
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC COOO C   O
4  Cc- CiIiIi cCc c    C  c c c     cC    c c cCc c        CoOo c - o
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CCO - C - O
2    -_   c    -_     _ -   - _CcCcC_CcCcCcCcCcCcCcCc c-_ c   - _ - _
1    -         -        -   -                          -      -   -
0 --------------------------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VDD6 | VSS | VSS2 | VSS3 | VSS4 | VSS5 | CLK | RESET_B | SCD | SCE | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| NMOS9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| PMOS2 | X |   | X | X | X | X |   |   |   |   |   |   |   |   |   |   | X |   | X | X | X | X |
| Poly1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |   |
| Poly10 | X |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   | X |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly13 |   |   | X |   |   |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   | X |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   | X |   |   |
| Poly23 |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly24 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly25 |   |   |   |   | X |   |   |   |   |   | X |   |   |   |   |   |   |   | X |   |   |   |
| Poly26 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly27 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly5 | X |   |   |   |   |   | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 | Poly24 | Poly25 | Poly26 | Poly27 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | O | E |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | E |   |   |   |   |   |   |
| NMOS3 | O | O | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |
| NMOS5 |   |   |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | N |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O | O |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |   |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS9 |   |   |   |   |   |   |   |   |   |   | O | O | O | E |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
