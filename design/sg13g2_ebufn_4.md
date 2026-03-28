# Design Documentation for sg13g2_ebufn_4

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
2 NpppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2  GG GGG G     G   G G
1  GG GGG G     G   G G
0  GG GGG G     G   G G
9  GG GGG G     G   G G
8  GGGGGG G     G   G G
7  GG GGG G     G   G G
6  GG GGG G     G   G G
5  GG GGG G     G   G G
4  GG GGG G     G   G G
3  GG GGG G     G   G G
2  GG GGG G     G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +       +   +
2    &       +   + CcCcCcCcC
1  C +     C + C + C   C   C
0  cCcCcCc CcCcCc+ CoO CoO C
9  C     CCCCC C   C O   O C
8  cIi c    cCcCcCcC OoOoO
7  CI  CCCC  CCCCCCCCCCC O
6  cI  iI c     c   cCcCoO
5  C   I  CCCCCCCCCC OOOOO
4  c _ i  cCc- C -cCoOo oOcC
3  C - CCCCC - C - C   C   C
2    _    c  -   - CcCcCcCcC
1    -       -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | A | TE_B | Z |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X |   | X | X |
| PMOS1 | X |   | X | X |   | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X | X | X |   |
| Poly2 |   |   | X |   |   |   |
| Poly3 |   |   | X |   |   |   |
| Poly4 |   |   | X |   |   | X |
| Poly5 |   |   | X |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O | O |
| PMOS1 | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |
