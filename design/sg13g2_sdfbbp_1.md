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
2 G G GGGGGG  GG G  G G G G  GGGG G G G G     G G G G     G
1 G G GGGGGG  GG G  G G G G  GGGG G G G G G G G G G G     G
0 G G GGGGGG  GG G  G G G G  GGGG G G G G G G G G G G G   G
9 G G GGGGGG  GG G GG G G G  GGGG G G G G G G G G G G G   G
8 G G GGGGGG  GG G GG G G G GGGGG G G G G G G G G G G G   G
7 G G GGGGGG  GG G GG G G G GGGGG G G G G G G G G G G G   G
6 GGG GGGGGG  GGGG GG G G G GGGGG G G G G G G G G G G G   G
5 G G GGGGGG  GG G GG G G G GGGGG G G G G G G G G G G G   G
4 G G GGGG G  GG G GG G G G GGGGG G G G G G   G G G G     G
3 G G GGGG G  GG G GG G G G GGGGG G G G G G   G G G G     G
2 G G GGGG G  GG G GG G G G  GGGG G G G G G   G G G G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +       +     +        +      +      +++    +    +     +
2    & cCccC +     +        & iIiI +iIiIiI&+&    +    &     &
1  C + C   C + C C +C       + I  I +I    I    C  +    + OOC + O
0  cCcCc c    cCcC&+c cCcC  & iCiI +i cCiIcCcCcCcCcCcCc oOc & o
9        CC  CCC C  CC C  C + IC IIII CCCICC  CCC     C OOC   O
8   I Ii  c cC CcCcC C Cc cCc iCcCiCc c cIi  I  c  Cc c oOc   o
7   I I IiC  C C   CCCCCC C C I    CC C CIIIII  C  C  C  OCC  O
6  iI  iIic  CcCiI CcCcCc cCc i c cCc c cCcCi cCc cCiIcC OcC  o
5   I  CCCCCCC CII  CCCCC CCCCCCC  C  C CC CCCCCC  C     OC   O
4      c  _ cCcC    c c c cCcCcCcCcC -c cCc _ c c cCc _ oOc _ o
3  -      - C   CCCCCCC CCC          -C  C  - C   C   - OOC - O
2  _      _ cCcCc _         _ cCcCcC -cCcC  _ cCcCc   _     _
1  -      -       -         -        -      -         -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | CLK | D | RESET_B | SCD | SCE | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X | X | X | X |   |   |   |   |   |   | X | X |
| PMOS1 | X |   | X |   | X | X | X |   |   | X |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly10 |   |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly11 |   |   |   |   | X |   |   |   |   | X |   |   |   |   |
| Poly12 |   |   |   |   | X |   |   |   |   | X |   |   |   |   |
| Poly13 |   |   |   |   | X |   |   |   |   | X |   |   |   |   |
| Poly14 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly16 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly17 |   |   |   |   | X |   |   |   |   | X |   |   |   |   |
| Poly18 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly19 |   |   |   |   | X |   |   |   |   | X |   |   |   |   |
| Poly2 |   |   | X |   |   |   | X |   | X |   |   | X |   |   |
| Poly20 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   | X |   |   |   |   | X |   |   |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   | X | X |   |   |   |   |   | X |   |   |   |   |
| Poly9 |   |   | X | X |   |   |   |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | N | N |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
