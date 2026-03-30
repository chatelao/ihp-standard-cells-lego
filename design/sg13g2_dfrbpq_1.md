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
3 NNNNNNNNNNNNNNNNNNNNppppppNNppppppppppppNNNNNNNN
2 NppppppNNNNNNNNNNNNNppppppNNppppppppppppNNNNNNNN
1 NppppppNpppppppppNNNppppppNNppppppppppppNNpppppN
0 NppppppNpppppppppNNNppppppNNppppppppppppNNpppppN
9 NppppppNNNNNNNNNNNNNppppppNNppppppppppppNNpppppN
8 NppppppNNNNNNNNNNNNNppppppNNppppppppppppNNpppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3
2   GGG G G G G G G G G G G G G G G G G G G G
1   GGG G G G G G G G G G G G G G G G G G G G
0   GGG G G G G G G G G G G G G G G G G G G G
9   GGG G G G G G G G G G G G G G G G G G G G
8   GGG G G G G G G G G G G G G G G G G G G G
7   GGG G G G G G G G G G G G G G G G G G G G G
6  GGGG G G G G G G G G G G G G G G G G G G G G
5   GGG G G G G G G G G G G G G G G G G G G G G
4   GGG G G G G G G G G G G G G G G G G G G G
3   GG  G   G G G G G G G G G G G G G G G G G
2   GG  G   G G G G G G G G G G G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
4 ++++++++++++++++++++++++++++++++++++++++++++++++
3  +         +                           +    +
2 &+ CcCcCcC&+cCcCc cCcCcC&CcCcCcCcCcCcC +& & +
1  + C     C +C   C                      +  C +OO
0  + CcCc cCcCc c c   cCcCcCcCcCc        +  c +Oo
9  + CC   C     C C  CCC       CCCC    C +  C +OO
8   cCc cCcCcCcCc c cCcCcCcCcCcCc c   cCc   c +Oo
7  I CC C II C  C C  C  C      CC C CCCCCC  C   O
6  i cC   iIiCcCc cCcC Ci iIcCcCcCc c   cCc cCcCo
5  I CCCCCCCCCCCCCCC C  C   C  CCCCCCCCCCC  C   O
4  I C  c c c   c  C CcCcCcCc c c       cC  c -Oo
3  CCC- C - CCCCCCCC        C CCCCCCC-  CC  C -OO
2   c - _ - _CcCcCcCcCcCcC_CcCcCcCc c-_ c   _ -
1     -   -                          -        -
0 ------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | VSS3 | VSS4 | VSS5 | CLK | D | RESET_B | Internal1 | Internal2 | Internal3 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X | X | X | X | X |   |   |   | X | X |   | X |
| PMOS1 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS2 |   | X |   |   |   |   |   |   |   |   |   | X |   | X |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |
| Poly10 |   | X |   |   |   |   | X |   | X |   |   | X |   | X |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly16 |   |   |   | X |   |   |   |   |   |   |   | X |   | X |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly18 | X |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly19 |   |   | X |   |   |   |   | X |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly3 | X |   |   |   |   | X |   |   |   |   | X | X |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly9 |   |   |   |   |   |   |   |   | X |   |   | X |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   | O | O | O | E | O | O | O | O | O | O | E |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   | S |
| PMOS4 |   |   | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |
