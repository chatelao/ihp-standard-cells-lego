# Design Documentation for sg13g2_dlhrq_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NppppppNpppppppppppppppppNN
0 NppppppNpppppppppppppppppNN
9 NppppppNpppppppppppppppppNN
8 NppppppNpppppppppppppppppNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSnnnnnnnnnnSSSSSSSSS
4 SnnnnnnSnnnnnnnnnnnnnnnnnSS
3 SnnnnnnSnnnnnnnnnnnnnnnnnSS
2 SSSSSSSSnnnnnnnnnnSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2 G G G GGG   G G G   G   G
1 G G G GGG   G G G   G   G
0 G GGG GGG G G G G G G   G
9 G GGG GGG G G G G G G   G
8 G GGG GGG G G G G G G   G
7 G GGG GGG G G G G G G   G
6 GGGGGGGGG G G G G G G G G
5 G GGG GGG G G G G G G   G
4 G GGG GGG G G G G G G   G
3 G GG  GGG G G G G G G   G
2 G GG  GGG   G G G G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 +++++++++++++++++++++++++++
3    +      +       +   +
2    +&   & + &CcC  + & + &
1  C +      + C  C  + C + OO
0  CcCcCcCcCc cCcC    c + oO
9  CCC CC C C CC C CCCC + OO
8    C  c c c cCcCcCc c   oO
7  I CIICCC CCC C   C CI   O
6  i cIiCcc c c cCc   cIiCcO
5  CCC  CCCCCCC CC   CCCCC O
4 cCc  CcCcCcC CcC  cCc   oO
3     - C    C   C - C  - OO
2   _ -   _ -C_CcC_-  _ -
1     -     -      -    -
0 ---------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VDD5 | VSS | VSS2 | VSS3 | VSS4 | VSS5 | D | GATE | RESET_B | Internal1 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   | X |   | X | X |   |   |   |   | X | X |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |
| Poly1 | X | X |   |   |   |   | X | X |   |   | X | X |   | X |   |
| Poly2 |   |   | X |   |   |   |   |   | X |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly4 |   |   |   |   |   | X |   |   |   |   |   |   |   | X |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly6 |   |   |   | X |   |   |   |   |   | X |   |   |   | X |   |
| Poly7 |   |   |   |   | X |   |   |   |   |   |   |   |   | X | X |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O |   |
| NMOS3 | O |   |   |   |   |   |   |   |   |
| PMOS1 | O |   |   |   |   |   |   |   |   |
| PMOS2 | O | O | O | O | O | O | O | O |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |
