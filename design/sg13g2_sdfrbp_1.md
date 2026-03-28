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
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3
2  GG  G GGGGGG G G     G  G GG G G G G   GG GG G G G G         G
1  GG  G GGGGGG G G     G  G GG G G G G   GG GG G G G G         G
0  GG GG GGGGGG G G     G  G GG G G G G   GG GG G G G G         G
9  GG GG GGGGGG G G     G  G GG G G G G   GG GG G G G G   G     G
8  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G     G
7  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G     G
6  GGGGG GGGGGG G G G   G  GGGG G G G G   GGGGG G G G G   G     G
5  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G     G
4  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G     G
3  GG GG GGGGGG G G G      G GG G G G G   GG GG G G G G   G     G
2  GG GG GGGGGG G G G      G GG G G G G   GG GG G G G G   G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          +   +   +
2     +cCccCcCc+     + CcCcCcC +  c   cCcCcCcCcCcCcCcCcCcC&   &   &
1     +C      C+ CC  + C     C +CCCCC                     + O +   + O
0  c   c  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       & o & c & o
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   O + C + O
8  c   cCcc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcCo & c   o
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    CO   C   O
6  cIi cIii i cCcCcCcC Cc   iIc c cCcCcC CcIiIcCc cCc c  CcCo   cC Oo
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC COOO C   O
4  c _ cIiiIi cCc c    C  c c c     cC    c c cCc c        CoOo c _ o
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CCO - C - O
2    _    c    -      c _   _ cCcCcCcCcCcCcCcCcCcCcCc c-  c   _   _
1    -         -        -   -                          -      -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | RESET_B | SCD | SCE | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   | X |   |   | X | X | X | X |
| PMOS1 | X |   |   |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   | X |   |   |
| Poly10 |   |   |   |   |   | X |   |   |
| Poly11 |   |   | X |   |   | X |   |   |
| Poly12 |   |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   |   | X |   |   |
| Poly14 |   |   |   |   |   | X |   |   |
| Poly15 |   |   |   |   |   | X |   |   |
| Poly16 |   |   |   |   |   | X |   |   |
| Poly17 |   |   |   |   |   | X |   |   |
| Poly18 |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   | X | X |   |   |
| Poly3 |   |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   | X |   |   |
| Poly6 |   |   |   | X |   | X |   |   |
| Poly7 |   |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   |   | X |   |   |
| Poly9 |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
