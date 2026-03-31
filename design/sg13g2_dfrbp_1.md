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
3 NNNNNNNNNNNNNNNNNNNNppppppNNpppppppppppppppNNNNNNNNN
2 NppppppNNNNNNNNNNNNNppppppNNpppppppppppppppNNNNNNNNN
1 NppppppNpppppppppNNNppppppNNpppppppppppppppNNpppppNN
0 NppppppNpppppppppNNNppppppNNpppppppppppppppNNpppppNN
9 NppppppNNNNNNNNNNNNNppppppNNpppppppppppppppNNpppppNN
8 NppppppNNNNNNNNNNNNNppppppNNpppppppppppppppNNpppppNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
4
3
2   GGG G G G G G G G G G G G G G G G G G     G G G
1   GGG G G G G G G G G G G G G G G G G G     G G G
0   GGG G G G G G G G G G G G G G G G G G     G G G
9   GGG G G G G G G G G G G G G G G G G G G   G G G
8   GGG G G G G G G G G G G G G G G G G G G   G G G
7   GGG G G G G G G G G G G G G G G G G G G   G G G
6  GGGG G G G G G G G G G G G G G G G G G G   G G G
5   GGG G G G G G G G G G G G G G G G G G G   G G G
4   GGG G G G G G G G G G G G G G G G G G G   G G G
3   GG  G   G G G G G G G G G G G G G G G     G G G
2   GG  G   G G G G G G G G G G G G G G G     G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901
4 ++++++++++++++++++++++++++++++++++++++++++++++++++++
3  +         +                            +      +
2 &+ CcCcCcC&+cCcCc cCcCcCcC&CcCcCcCcCcC  + &   &+
1  + C     C +C   C                       + O  C + O
0  + CcCc cCcCc c c   cCcCcCcCcCc         + o  C +oO
9  + CC   C     C C  CCC       CCCC    C    O  C + O
8   cCc cCcCcCcCc c cCcCcCcCcCcCc c cCcCcCc o  C + O
7  I CC C II C  C C  C  C      CC C C     C O  C   O
6  i cC   iIiCcCc cCcC Ci iIcCcCcCc     c c o cCcCcOo
5  I CCCCCCCCCCCCCCC C  C   C  CCCCCCCCCC C OO C   O
4  I C  c c c   c  C CcCcCcCc c c       cCc oO C -oO
3  CCC- C - CCCCCCCC        C CCCCCCC-  CC- O  C - O
2   c - _ - _CcCcCcCcCcCcCcC_CcCcCc c-_ c - _   _-
1     -   -                          -    -      -
0 ----------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | VSS3 | VSS4 | VSS5 | CLK | D | RESET_B | Internal1 | Internal2 | Internal3 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X | X | X | X | X |   |   |   | X |   |   | X | X |
| PMOS1 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| PMOS2 |   |   | X |   |   |   |   |   |   |   |   | X |   | X |   | X |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   | X |   |   | X |   | X |   |   |
| Poly11 |   | X |   |   |   |   | X |   |   |   |   | X |   | X |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly16 |   |   |   | X |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly19 | X |   |   | X |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly3 | X |   |   |   |   | X |   |   |   |   | X | X |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |
| Poly9 |   |   |   |   |   |   |   |   | X |   |   | X |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   | O | O | O | E | O | O | O | O | O | O |   |   |   |   | O |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | W | O | O |   |   |
| PMOS4 |   |   | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |
