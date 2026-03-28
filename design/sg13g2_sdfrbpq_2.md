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
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
4
3
2  GG  G GGGGGG G G     G  G GG G G G G   GG GG G G G G
1  GG  G GGGGGG G G     G  G GG G G G G   GG GG G G G G
0  GG GG GGGGGG G G     G  G GG G G G G   GG GG G G G G
9  GG GG GGGGGG G G     G  G GG G G G G   GG GG G G G G   G
8  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G
7  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G
6  GGGGG GGGGGG G G G   G  GGGG G G G G   GGGGG G G G G   G
5  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G
4  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G
3  GG GG GGGGGG G G G      G GG G G G G   GG GG G G G G   G
2  GG GG GGGGGG G G G      G GG G G G G   GG GG G G G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          +   +
2     +cCccCcCc+     + CcCcCcC +  c   cCcCcCcCcCcCcCcCcCcC&   &
1     +C      C+ CC  + C     C +CCCCC                     + OO+
0  c   c  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       & oO&
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   OO+
8  c   cCcc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcCoO&
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    C O
6  cIi cIii i cCcCcCcC Cc   iIc c cCcCcC CcIiIcCc cCc c  CcC Oo
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC C  O
4  c _ cIiiIi cCc c    C  c c c     cC    c c cCc c        C_ o _
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CC- O -
2    _    c    -      c _   _ cCcCcCcCcCcCcCcCcCcCcCc c-  c _   _
1    -         -        -   -                          -    -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | VSS4 | VSS5 | CLK | RESET_B | SCD | SCE | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X | X | X |   |   |   | X |   | X |
| PMOS1 | X |   | X | X |   | X |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |   |   | X |   |
| Poly10 |   |   |   | X |   | X |   |   |   |   |   |
| Poly11 |   |   |   | X |   | X | X |   |   |   |   |
| Poly12 |   |   |   | X |   | X |   |   |   |   |   |
| Poly13 |   |   |   | X |   | X |   |   |   |   |   |
| Poly14 |   |   |   | X |   | X |   |   |   |   |   |
| Poly15 |   |   |   | X | X | X |   |   |   |   |   |
| Poly16 |   |   |   | X |   |   |   |   |   |   |   |
| Poly17 |   |   |   | X |   |   |   |   |   |   |   |
| Poly2 |   |   | X |   |   |   |   |   | X |   |   |
| Poly3 |   |   | X |   |   |   |   |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   | X |   |   |   | X |   |   |   |
| Poly7 |   |   |   | X |   |   |   |   |   |   |   |
| Poly8 |   |   |   | X |   |   |   |   |   |   |   |
| Poly9 |   |   |   | X |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
