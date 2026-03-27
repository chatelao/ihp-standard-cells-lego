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
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2 G G G GGGG   G G G         GGGG   G G G
1 G G G GGGG   G G G         G G
0 G G G GGGG   G GGG         GGGG   G   G
9 G G G GGGG   G G G         G G
8 G G GGGGGG   G G G         GGG  G       G G
7 G G G GGGG   G G G         G G
6 GGG GGGGGG   GGG G         GGG            G       G         G
5 G G G GGGG   G G G         G G
4 G G G GGGG   G G G         G G
3 G G G GGGG   G G G         G G
2 G G G GGGG   G G G         G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +       +    ++       ++     ++      +++    +    +     +
2    & cCccC +    &+       +& iIiI&+iIiIiI&+&    +    &     &
1  C + C   C + CCC++CC     ++ I  I++I    I    C  +    + OOC + O
0  cCcCc c    cCcC&+cCcCcCc+& iCiI&+i cCiIcCcCc c c c c oOc & o
9        CC  CCCCC  CC CCCC++ IC IIII CCCICC  CCC     C OOC + O
8   I Ii  c cC CcCcC C Cc cCc iCcCiCc c cIi iIcCc  Cc c oOc   o
7   I I IiC  C CII CCCCCC C C I    CC C CIIIII  C CC  C  OCC  O
6  iI  iIic  CcCiI CcCcCc cCc i c cCc c cCcCi cCc cCiIcC OcC  o
5   I  CCCCCCC CII CCCCCC CCCCCCC CC  C CCCCCCCCC CC I   OC   O
4  _   c  _ cCcC    c c c cCcCcCcCcC -c cCc _ c cCcCc _ oOc _ o
3  -      - C   CCCCCCC CCC   CC  CC -C  CC - C  CC   - OOC - O
2  _      _ cCcCc _         _ cCcCcC_-cCcCc _ cCcCc   _     _
1  -      -       -         -        -      -         -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | CLK | RESET_B | SCD | SCE | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X | X | X |   |   |   |   |   |   |   |   | X | X |
| PMOS1 | X |   | X | X | X | X | X | X | X |   | X |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly12 |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly2 |   | X | X |   |   |   | X |   |   |   |   |   | X |   |   |
| Poly3 | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly5 |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly6 |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly8 |   |   | X |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O |   |   |   | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
