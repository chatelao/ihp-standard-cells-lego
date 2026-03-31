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
2    G G GG G G G G G G
1    G G GG G G G G G G
0    G G GG G G G G G G
9    G G GG G G G G G G
8    G G GG G G G G G G
7   GGGGGGGGGGG GGGGGGG
6  G G G GG G G GGGGG G
5    G G GGGGGGGGGGGG G
4    G G GGGGGGGGGGGG G
3    G G GGGGGGGGGGGG G
2    G G GGGGGGGGGGGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3  +      +  +
2  +      +  + CcCcCcCcC
1  + C  C +C + C   C   C
0  + c cC +Cc+ C OcCoO C
9  + C  C +C + C O   O C
8    c  C  Cc  C OoOoO
7  IIC  CCCCCCCC  OIIII
6  iIc  CccCcCcCc oIiIi
5    C  C   C   COOOOOO
4  - cCcC - c - cOo o o c
3  - CCCC - C - CCCCC   C
2  -      -   -   c cCcCc
1  -      -   -
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Z |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   |   |   | X |   |
| NMOS3 |   |   |   |   | X | X |
| PMOS1 |   |   |   |   | X |   |
| PMOS2 |   |   |   |   | X | X |
| PMOS3 | X |   |   |   |   |   |
| Poly1 |   |   | X |   | X | X |
| Poly2 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 | O |   |
| PMOS1 | O |   |
| PMOS2 | O |   |
| PMOS3 |   |   |
