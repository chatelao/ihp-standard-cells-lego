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
2   G G G
1   G G G
0   G G G
9   G G G
8   GGG G
7   G G G
6   GGGGG               G
5   G G G
4   G GGG
3   G G G
2   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +       +   +
2    +&      +&  +&CcCcCcCcC
1  C +      C+ C + C   C   C
0  cCcCcCc  cCcCc+ CoOcCoOcC
9  C     CCCCC C   C O   O C
8  cII cCcC cCcCcCcC OoOoO
7  CI     C  CCCCCCCCCCC O
6  cIi II c     c c cCcCoO
5  C   I  C CCCCCCCC OOOOO
4  c _ i  c c_ Cc_cCoOo oOcC
3  C - CCCC C- C - C   C   C
2    _   cc  _   _ CcCcCcCcC
1    -       -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | TE_B | Internal3 | Internal1 | VDD | Internal2 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | X |
| NMOS2 |   | X | X | X |   | X |
| PMOS1 |   |   | X | X | X |   |
| PMOS2 |   |   |   |   | X |   |
| Poly1 | X | X |   |   | X |   |
| Poly2 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS2 | Poly1 |
| PMOS1 | Poly1 |
