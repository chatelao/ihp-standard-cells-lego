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
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NpppppNNNpppppppppppppppppN
0 NpppppNNNpppppppppppppppppN
9 NpppppNNNpppppppppppppppppN
8 NpppppNNNpppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnSSSnnnnnnnnnnnnnnnnnS
3 SnnnnnSSSnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2    GGG GG G G G G G G G
1    GGG GG G G G G G G G
0    GGG GG G G G G G G G
9    GGG GG G G G G G G G
8    GGG GG G G G G G G G
7    GGGGGGGGGGGGGG G G G
6   GGGGGGG G G G G GGGGGG
5   GGGG GG G G G G G G G
4   GGGG GG G G G G G G G
3   GGGG GG G G G G G G G
2   GGGG GG G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +       +   +
2    +       +   + CcCcCcCcC
1  C +     C + C + C   C   C
0  cCcCcCc CcCcCc+ CoO CoO C
9  C     CCCCC C   C O   O C
8  cIi c    cCcCcCcC OoOoO
7  CI  CCCC  CCCCCCCCCCC O
6  cIi iI c     c   cCcCoO
5  C   I  CCCCCCCCCC OOOOO
4  c - i  cCc- C -cCoOo oOcC
3  C - CCCCC - C - C   C   C
2  _ -    c  -   - CcCcCcCcC
1    -       -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Z |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   |   | X | X |   |
| NMOS3 |   |   |   |   | X | X |
| PMOS1 |   |   | X |   | X |   |
| PMOS2 |   |   |   |   | X | X |
| PMOS3 | X |   |   |   |   |   |
| Poly1 |   |   | X | X | X |   |
| Poly2 |   |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 | O | O |
| PMOS1 | O |   |
| PMOS2 | O | O |
| PMOS3 |   |   |
