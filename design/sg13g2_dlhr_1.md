# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2  GG   GGG   G G G   G   G G
1  GG   GGG   G G G   G   G G
0  GG G GGG G G G G G G   G G
9  GG G GGG G G G G G G G G G
8  GG G GGG G G G G G G G G G G
7  GG G GGG G G G G G G G G G G
6  GGGGGGGG G G G G G G G G G G
5  GG G GGG G G G G G G G G G G
4  GG   GGG G G G G G G   G G
3  GG   GGG G G G G G G   G G
2  GG   GGG   G G G G G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 ++++++++++++++++++++++++++++++++
3     +     +      +++  +     +
2   & +   & + cCcC&+++& + &   + &
1     +     +C   C +++ C+ OOC + O
0  CcCcCcCcCcCcC C    cC+ oOc + o
9  C      C CC C C CCCCC  OOC + O
8  C    c c cCcCcC CcCcCcCoOc   o
7  C I ICCC CCCCCCCCCC I CCOC   O
6  c i iCcc cCc c c cC IiCcOcCcCo
5  C    C CCCCCCC    C I   OC   O
4  Cc--Cc c c  Cc  - Cc - oOc - o
3    --CCCCCCC     - C  - O C - O
2   _--   _ -CcCcC_- C_ - o _ - o
1    --     -      -    -     -
0 --------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VSS | VSS2 | VSS3 | VSS4 | D | GATE | RESET_B | Internal1 | Internal2 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | X | X | X | X |   |   |   | X | X | X | X |
| PMOS1 | X | X | X | X | X |   |   |   |   |   |   |   | X | X | X | X |
| Poly1 |   | X | X |   |   | X | X |   |   | X | X |   | X |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly4 | X |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly6 | X |   |   |   |   |   |   | X |   |   |   |   | X |   |   |   |
| Poly7 |   |   |   | X |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly8 |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O |
