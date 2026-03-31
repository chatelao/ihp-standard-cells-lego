# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4 ppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NpppNpppppppppppppppppppppppppppppppppN
0 NpppNpppppppppppppppppppppppppppppppppN
9 NpppNpppppppppppppppppppppppppppppppppN
8 NpppNpppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
4 SnnnSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678
4
3
2    GG G G G G G G   G G G G G G G G G
1    GG G G G G G G   G G G G G G G G G
0    GG G G G G G G   G G G G G G G G G
9    GG G G G G G G G G G G G G G G G G
8    GG GGG G G G G G G G G G G G G G G
7    GG GGG G G G G G G G G G G G G G G
6  G GG GGG G G G G G G G G G G G G G G
5    GG GGG G G G G G G G G G G G G G G
4    GG GG  G   G   G G G G G G G G G G
3    GG GG  G   G   G G G G G G G G G G
2    GG GG  G   G   G G G G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678
4 +++++++++++++++++++++++++++++++++++++++
3  +     +   +   +  +
2  +&    +& &+  &+  + &CcCcCcCcCcCcCcCc
1  + C C + C + C +CC+  C   C   C   C  C
0  + C Cc+cC +cC +cC+  C O CoO C O CoOc
9  + C C + C + C +CC   C O   O   O   OC
8  + C C   C   C  cCcCcC OoOoOoOoOoOoO
7    C CCCCCCCCCCCC      OOO
6  i c  CccCcCcCcCcCcCcC OoO IiIiIiIiIi
5  I CCCC   C   C   C  C OOO
4  - CcCc - c - c - c- CcOoOoOoOoOoOoOc
3  - CCCC - C - C - C- CCCCCCCCC   C  C
2  -_     - _ - _ -  -_     c cCcCcCcCc
1  -      -   -   -  -
0 ---------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS2 | VSS3 | A | TE_B | Internal1 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS3 |   |   |   |   |   |   |   | X | X |
| PMOS2 |   |   |   |   |   |   |   | X | X |
| Poly1 |   |   |   |   |   |   |   | X |   |
| Poly10 |   |   |   |   |   | X |   | X | X |
| Poly11 |   |   |   |   |   | X |   | X | X |
| Poly12 |   |   |   |   |   | X |   | X | X |
| Poly13 |   |   |   |   |   | X |   | X | X |
| Poly14 |   |   |   |   |   | X |   | X |   |
| Poly15 |   |   |   |   |   |   |   | X |   |
| Poly16 |   |   |   |   |   |   |   | X |   |
| Poly17 |   |   |   |   |   |   | X |   |   |
| Poly2 | X |   |   |   |   |   |   | X |   |
| Poly3 | X |   |   | X |   |   |   | X |   |
| Poly4 | X |   |   |   | X |   |   | X |   |
| Poly5 |   |   |   |   |   |   |   | X |   |
| Poly6 |   | X | X |   |   |   |   | X |   |
| Poly7 |   |   |   |   |   |   |   | X |   |
| Poly8 |   |   |   |   |   |   |   | X | X |
| Poly9 |   |   |   |   |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS3 |   | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |   |
| PMOS1 | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 | W | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
