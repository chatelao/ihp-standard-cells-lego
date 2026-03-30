# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnSnnnnnnnnnnnnnnnnnnnSnnnnnS
3 SnnnnnnSnnnnnnnnnnnnnnnnnnnSnnnnnS
2 SSSSSSSSSSSSSSSSSSSSnnnnnnnSnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2  GG G G G   G G G G   G     G
1  GG G G G G G G G G   G     G
0  GG G G G G G G G G G G     G
9  GG G G G G G G G G G G     G
8  GG G G G G G G G G G G G   G
7  GG G G G G G G G G G G G   G G
6  GGGGGG G G G G G G G G G   G G
5  GG G G G G G G G G G G G   G G
4  GG   G G G G G G   G G     G
3  GG   G G   G G G   G G     G
2  GG   G G   G G G   G G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++
3    +      +        ++   +     +
2    +& c   + &CcC& &++ & +     + &
1  C + CCCCCCCC C C  ++ C + O C + O
0  Cc cCc c  Cc c c     c + o c + o
9  CCCCCCCCCCCC C C CCCCC + O C + O
8  Cc   c c cCcCc c    CcCc oOc + o
7  C I IC C CCCCCCCCC  C  C  OC   O
6  c i iC cCc cCcCcCcCcCiIcCoOcCcCo
5  C    C CCCCCCCCCC   C     OC   O
4  Cc - c cCcCcCcCcC- cC  -Oo c - o
3     - C C -   CCCC- CC  -OO C - O
2   _ -     - _   _ - _C_ -Oo _ - o
1     -     -       -     -     -
0 ----------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | D | GATE_N | RESET_B | Internal1 | Internal2 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   |   |   |   | X | X |   |   |   |   | X |   | X |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   | X |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS1 | X | X | X | X | X |   |   |   |   |   |   |   |   |   | X | X | X | X |
| Poly1 | X |   |   |   |   | X |   |   |   |   |   | X | X |   | X |   |   |   |
| Poly10 | X |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly3 |   | X |   |   |   |   | X |   |   |   |   |   |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly5 |   |   | X |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X |   |   |   |
| Poly7 |   |   |   | X |   |   |   |   |   | X |   |   |   | X | X |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | O | O | O | O | O | O |   | O | N | N |   |
| NMOS3 |   |   |   |   |   |   |   | O |   |   |   | N |
| NMOS4 | O |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | S |
