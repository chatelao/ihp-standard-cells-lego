# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3
2 G GG   G GG G G G G   GG GG G G G G   G G G
1 G GG   G GG G G G G   GG GG G G G G   G G G
0 G GG   G GG G G G G   GG GG G G G G   G G G
9 G GG   G GG G G G G   GG GG G G G G   G G G
8 GGGG   G GG G G G G   GG GG G G G G   G G G
7 GGGG   G GG G G G G   GG GG G G G G   G G G G
6 GGGG   GGGG G G G G   GGGGG G G G G   G G G G
5 GGGG   G GG G G G G   GG GG G G G G   G G G G
4 GGGG   G GG G G G G   GG GG G G G G   G G G
3 GGGG   G GG G G G G   GG GG G G G G   G G G
2 GGGG   G GG G G G G   GG GG G G G G   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +
2  & cCcCccC +cCcCc cCcCcCcCcCcCcCcCcCcC +    &
1  + C     C +C   C                      +  C +OO
0  & cCcC cCcCc c c   cCcCcCcCcCc        +  c &Oo
9  + CC   C     C C  CCC       CCCC    C +  C +OO
8    cCcCccCcCcCc c cCcCcCcCcCcCc c   cCc   c &Oo
7  I CC C II C  C C  C  C      CC C CCCCCC  C   O
6  i cC   iIcCcCc cCcC Cc iIcCcCcCc c   cCc cCcCo
5  I CCCCCCCCCCCCCCC C  C   C  CCCCCCCCCCC  C   O
4  i c  Cc  c   c  C CcCcCcCc c c       cC  c _Oo
3  CCC- C - CCCCCCCC        C CCCCCCC-  CC  C -OO
2  c  -   _ cCcCcCcCcCcCcCcCcCcCcCc c-  c     _
1     -   -                          -        -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | Internal1 | Internal2 | RESET_B | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   | X |   | X | X |   | X | X |
| PMOS1 | X |   |   |   | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   | X |   |
| Poly10 |   |   |   |   |   | X | X |   |
| Poly11 |   |   |   |   |   | X | X |   |
| Poly12 |   |   |   |   |   |   | X |   |
| Poly13 |   |   |   |   |   |   | X |   |
| Poly14 |   |   |   |   | X |   |   |   |
| Poly15 |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   | X |   |
| Poly4 |   |   |   |   |   |   | X |   |
| Poly5 |   |   |   |   |   |   | X |   |
| Poly6 |   |   |   |   |   | X | X |   |
| Poly7 |   |   | X |   |   | X | X |   |
| Poly8 |   |   |   |   |   | X | X |   |
| Poly9 |   |   |   |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | N |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | S |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
