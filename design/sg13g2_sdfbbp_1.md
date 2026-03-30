# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNppppppppppppppppppppppppppppNNNNNNNNNNNNNN
1 NpppppppppNpppNpppppppppppppppppppppppppppppppppNNpppppNpppppN
0 NpppppppppNpppNpppppppppppppppppppppppppppppppppNNpppppNpppppN
9 NNNNNNNNNNNNNNNpppppppppppppppppppppppppppppppppNNpppppNpppppN
8 NNNNNNNNNNNNNNNpppppppppppppppppppppppppppppppppNNpppppNpppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2   G G GGG G G G   G G G G   G G G G G G     G G G G     G
1   G G GGG G G G   G G G G   G G G G G G G G G G G G     G
0   G G GGG G G G   G G G G   G G G G G G G G G G G G G   G
9   G G GGG G G G G G G G G   G G G G G G G G G G G G G   G
8   G G GGG G G G G G G G G G G G G G G G G G G G G G G   G
7   G G GGG G G G G G G G G G G G G G G G G G G G G G G   G
6   GGG GGG G G G G G G G G G G G G G G G G G G G G G G   G
5   G G GGG G G G G G G G G G G G G G G G G G G G G G G   G
4   G G GG  G G G G G G G G G G G G G G G G   G G G G     G
3   G G GG  G G G G G G G G G G G G G G G G   G G G G     G
2   G G GG  G G G   G G G G   G G G G G G G   G G G G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3    +       +     +        +      +      +++    +    +     +
2    +&CcCcC&+    &+      & + iI&I&+iIiIiI+++    +&   + & & +
1  C + C   C + C C +C       + I  I +I    I    C  +    + OOC + O
0  CcCcCcC    cCcC +c cCcC  + iCiI +i cCiIcC&CcCcCcCcCc oOc + o
9        CC  CCC C  CC C  C + IC IIII CCCICC  CCC     C OOC   O
8   i i   c cC CcCcC C Cc cCc iCcCiCc c cIi  I  c  Cc c oOc   o
7   I I IiC  C C   CCCCCC C C I    CC C CIIIII  C  C  C  OCC  O
6   Ii  Iic  CcCiI CcCcCc iCc i c cCc c cCcCi cCc iCiIcC OcC  o
5   I  CCCCCCC CII  CCCCC CCCCCCC  C  C CC CCCCCC  C     OC   O
4      Cc - cC&C    c c c cC_CcCcCcC -c cCc - c c cCc - oOc - o
3  -      - C   CCCCCCC CCC          -C  C  - C   C   - OOC - O
2  -_     - _CcC_ -       _ - cC_CcC_-cCcC_ - cCcCc _ -     - _
1  -      -       -         -        -      -         -     -
0 --------------------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VDD7 | VSS | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | CLK | D | RESET_B | SCD | SCE | SET_B | Internal1 | Internal2 | Internal3 | Internal4 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | X |   |   |   |   |   | X | X | X | X | X | X | X | X | X |   |   |   |   |   |   | X | X | X | X | X | X |
| PMOS1 |   | X | X | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   | X |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly1 |   | X |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   | X | X |   | X |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X |   |   |   |   |
| Poly11 |   |   |   |   | X |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   | X | X | X |   |   |   |   |
| Poly12 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X |   |   |   |   |
| Poly13 |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   | X |   |   | X |   |   |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly19 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   |   |   |   | X |   |   |   |
| Poly21 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly23 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly24 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |   |
| Poly25 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly3 |   | X |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly4 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |   | X |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly9 |   |   |   | X |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 | Poly24 | Poly25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 |   |   |   |   | W | O | O | O | O | O | O | O | O | O | O | O | O | O | E |   |   | O | O | O |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |   |   |   | O |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |   |   |   |
| PMOS4 | O | O | E |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS5 |   |   | W | O | E |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
