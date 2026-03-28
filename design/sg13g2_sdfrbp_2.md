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
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3
2  GG  G GGGGGG G G     G  G GG G G G G   GG GG G G G G
1  GG  G GGGGGG G G     G  G GG G G G G   GG GG G G G G
0  GG GG GGGGGG G G     G  G GG G G G G   GG GG G G G G
9  GG GG GGGGGG G G     G  G GG G G G G   GG GG G G G G   G
8  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G
7  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G       G
6  GGGGG GGGGGG G G G   G  GGGG G G G G   GGGGG G G G G   G       G
5  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G       G
4  GG GG GGGGGG G G G   G  G GG G G G G   GG GG G G G G   G       G
3  GG GG GGGGGG G G G      G GG G G G G   GG GG G G G G   G       G
2  GG GG GGGGGG G G G      G GG G G G G   GG GG G G G G   G       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +     +         +                          +   +   +   +
2     +cCccCcCc+     + CcCcCcC +  c   cCcCcCcCcCcCcCcCcCcC&   &   &   &
1     +C      C+ CC  + C     C +CCCCC                     + O +   + O +
0  c   c  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       & o & cC& o &
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   O + CC+ O +
8  c   cCcc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcCo & cC& o &
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    CO    C  O
6  cIi cIii i cCcCcCcC Cc   iIc c cCcCcC CcIiIcCc cCc c  CcCoOo  CcCoOo
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC C  O   C  OOO
4  c _ cIiiIi cCc c    C  c c c     cC    c c cCc c        C  o   c _OoO
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CC- O - C - O-
2    _    c    -      c _   _ cCcCcCcCcCcCcCcCcCcCcCc c-  c _   _   _  -
1    -         -        -   -                          -    -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | RESET_B | SCD | SCE | D | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   | X |   | X | X | X |
| PMOS1 | X |   |   |   |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   | X | X |   |   |
| Poly10 |   |   |   |   |   |   | X |   |   |
| Poly11 |   |   | X |   |   |   | X |   |   |
| Poly12 |   |   |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   |   |   | X |   |   |
| Poly14 |   |   |   |   |   |   | X |   |   |
| Poly15 |   |   |   |   |   |   | X |   |   |
| Poly16 |   |   |   |   |   |   | X |   |   |
| Poly17 |   |   |   |   |   |   | X |   |   |
| Poly18 |   |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   | X |   | X |   |   |
| Poly3 |   |   |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   | X |   |   |
| Poly6 |   |   |   | X |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   |   |   | X |   |   |
| Poly9 |   |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | S | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
