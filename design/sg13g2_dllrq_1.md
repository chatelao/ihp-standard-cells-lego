# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456789012345678901234567
4
3
2  GG   GGG   G G G     G   G
1  GG   GGG G G G G     G   G
0  GG   GGG G G G G     G   G
9  GG   GGG G G G G G G G G G
8  GG   GGG G G G G G G G G G
7  GG   GGG G G G G G G G G G
6  GGG GGGG G G G G G G G G G
5  GG   GGG G G G G G G G G G
4  GG   GGG G G G G G G G   G
3  GG   GGG G G G G G G G   G
2  GG   GGG G G G G   G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 ++++++++++++++++++++++++++++
3     +     +       +++   +
2   & +     + & &   +++ & +
1     +             +++ C + OO
0  Cc +CcCcCcCcCcCc +++ c + oO
9  CC +CCC     CC C CCCCCCCCOO
8  Cc +CcCcCcCcCc c cCcCc cCoO
7  C I I C C  CCCCCCCC C I C O
6  c i i c CcCcCcCc  CcCcIiCcO
5  CC    C CCCCCCCC  C C I   O
4  Cc  CcCcCcC   CcCcCcC  - oO
3  CCCCCCCCCCC   C    CC  - OO
2     _ c   _   _C  _-cC_ - oO
1     -     ---      -    -
0 ----------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD2 | VDD3 | VDD4 | VDD5 | VSS | VSS2 | VSS3 | D | GATE_N | RESET_B | Internal1 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X | X | X |   |   |   | X | X |
| PMOS1 | X | X | X | X |   |   |   |   |   |   | X | X |
| Poly1 | X |   |   |   |   |   |   | X |   |   | X |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly11 |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly2 |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly3 |   |   |   |   | X |   |   |   |   |   | X |   |
| Poly4 |   | X |   |   |   |   |   |   |   |   | X |   |
| Poly5 |   |   | X |   |   | X |   |   |   |   | X |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly8 |   |   |   | X |   |   | X |   |   |   | X |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O |
