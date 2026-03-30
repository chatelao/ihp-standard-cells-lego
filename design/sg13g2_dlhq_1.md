# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901234567890123456789
4
3
2    GG G G G G G G G G G G
1    GG GGG G G G G G G G G
0    GG GGG G G G G G G G G
9    GG GGG G G G G G G G G
8    GG GGG G G G G G G G G G
7    GG GGG G G G G G G G G G
6  G GG GGG G G G G G G G G G
5    GG GGG G G G G G G G G G
4    GG G G G G G G G G G G G
3    GG G G G G G G G G G G G
2    GG G G G G G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 ++++++++++++++++++++++++++++++
3  +     +           +      +
2 &+    &+cCc cC&C  &+    & +
1  + C CCCCC  C             + O
0  + CcCc cCcCc cCcCcCcCcCc + o
9  + C C  C  CC CCCCCCCCCCC + O
8    C      cCc cCcCc  CcC    o
7  IICC     CCCCCC  C  CCCIICCO
6  iIcC CccCc i cC  c cCcCiIcCo
5    CC C  CCCCCCCC C  C CC COO
4    Cc c- Cc     c c  Cc c cOo
3  - C CC-  CCCCC   CCCCCCCCCOO
2  -_    -_CcCcC_CcCc _   c _
1  -     -            -    -
0 ------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | VSS3 | D | GATE | Internal1 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X | X | X |   |   | X | X |
| PMOS1 | X | X | X |   |   |   |   |   | X | X |
| Poly1 |   |   |   |   |   |   |   |   | X |   |
| Poly10 |   |   | X |   |   |   |   | X | X |   |
| Poly11 |   |   |   |   |   | X |   |   | X |   |
| Poly12 |   |   |   |   |   |   | X |   |   |   |
| Poly2 | X |   |   | X |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   |   |   | X |   |
| Poly4 |   |   |   |   |   |   |   | X | X |   |
| Poly5 |   | X |   |   | X |   |   |   | X |   |
| Poly6 |   |   |   |   |   |   |   |   | X |   |
| Poly7 | X |   |   |   |   |   |   |   | X |   |
| Poly8 |   |   |   | X |   |   |   |   | X |   |
| Poly9 |   |   |   |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | O | O | O | O | N |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O |   |
