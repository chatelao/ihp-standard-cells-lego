# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
4
3
2 G GG   G GG G G G G   GG GG G G G     G     G G G
1 G GG   G GG G G G G   GG GG G G G     G     G G G
0 G GG   G GG G G G G   GG GG G G G     G     G G G
9 G GG   G GG G G G G   GG GG G G G     G G   G G G
8 GGGG   G GG G G G G   GG GG G G G     G G   G G G
7 GGGG   G GG G G G G   GG GG G G G     G G   G G G
6 GGGG   GGGG G G G G   GGGGG G G G     G G   G G G
5 GGGG   G GG G G G G   GG GG G G G     G G   G G G
4 GGGG   G GG G G G G   GG GG G G G     G G   G G G
3 GGGG   G GG G G G G   GG GG G G G     G     G G G
2 GGGG   G GG G G G G   GG GG G G G     G     G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                            +      +
2  & cCcCccC +cCcCc cCcCcCcCcCcCcCcCcCcC  &      +
1  + C     C +C   C                       + O  C + O
0  & cCcC cCcCc c c   cCcCcCcCcCc         & o  C +oO
9  + CC   C     C C  CCC       CCCC    C    O  C + O
8    cCcCccCcCcCc c cCcCcCcCcCcCc c cCcCcCc o  C + O
7  I CC C II C  C C  C  C      CC C C     C O  C   O
6  i cC   iIcCcCc cCcC Cc iIcCcCcCc     c c o cCcCcOo
5  I CCCCCCCCCCCCCCC C  C   C  CCCCCCCCCC C OO C   O
4  i c  Cc  c   c  C CcCcCcCc c c       cCc oO C -oO
3  CCC- C - CCCCCCCC        C CCCCCCC-  CC- O  C - O
2  c  -   _ cCcCcCcCcCcCcCcCcCcCcCc c-  c _      -
1     -   -                          -    -      -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | RESET_B | CLK | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X | X |   | X | X | X |
| PMOS1 | X |   |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   | X |   |   |
| Poly10 |   |   |   |   | X |   |   |
| Poly11 |   |   |   |   | X |   |   |
| Poly12 |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   | X |   |   |
| Poly14 |   |   |   |   | X | X |   |
| Poly15 |   |   |   |   | X |   |   |
| Poly2 |   |   |   | X | X |   |   |
| Poly3 |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   | X |   |   |
| Poly9 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
