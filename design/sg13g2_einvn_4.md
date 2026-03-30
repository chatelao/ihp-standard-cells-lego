# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NpppNNppppppppppppppppN
0 NpppNNppppppppppppppppN
9 NpppNNppppppppppppppppN
8 NpppNNppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SnnnSSnnnnnnnnnnnnnnnnn
3 SnnnSSnnnnnnnnnnnnnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2    GG G   G G G G G G G
1    GG G   G G G G G G G
0    GG G   G G G G G G G
9    GG G   G G G G G G G
8    GG GGG G G G G G G G
7    GG GGG G G G G G G G
6  G GG GGG G G G G G G G
5    GG GGG G G G G G G G
4    GG GG  G   G G G G G
3    GG GG  G   G G G G G
2    GG GG  G   G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 +++++++++++++++++++++++
3  +      +  +
2  +&   & +  +&CcCcCcCcC
1  + C  C +C + C   C   C
0  + Cc c +Cc+ C OcCoO C
9  + C  C +C + C O   O C
8    C  c  Cc  C OoOoO
7  IIC  CCCCCCCC  OIIII
6  iIc  CccCcCcCc oIiIi
5    C  C   C   COOOOOO
4  - CcCc - c - cOo o o c
3  - CCCC - C - CCCCC   C
2  -_     - _ - _ c cCcCc
1  -      -   -
0 -----------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS2 | VSS3 | A | TE_B | Internal1 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS3 |   |   |   |   |   |   | X | X |
| PMOS2 |   |   |   |   |   |   | X | X |
| Poly1 |   |   |   |   |   |   | X |   |
| Poly10 |   |   |   |   |   | X |   |   |
| Poly2 |   | X |   |   |   |   | X |   |
| Poly3 |   |   | X |   |   |   | X |   |
| Poly4 |   |   |   | X |   |   | X |   |
| Poly5 |   |   |   |   |   |   | X | X |
| Poly6 |   |   |   |   | X |   | X | X |
| Poly7 |   |   |   |   | X |   | X | X |
| Poly8 |   |   |   |   |   |   | X |   |
| Poly9 | X |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |   |   |   |   |   |
| NMOS3 |   | O | O | O | O | O | O | O | N |   |
| PMOS1 | O |   |   |   |   |   |   |   |   |   |
| PMOS2 |   | O | O | O | O | O | O | E | O |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |
