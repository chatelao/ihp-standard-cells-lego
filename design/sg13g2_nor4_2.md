# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4 ppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppN
1 NpppppppppppppppppppN
0 NpppppppppppppppppppN
9 NpppppppppppppppppppN
8 NpppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890
4
3
2   G G  G G G G G G
1   G G  G G G G G G
0   G G  G G G G G G
9   G G  G G G G G G
8   G G  G G G G G G
7   G G  G G G G G G
6   GGG  GGG GGG GGG
5   G G  G G G G G G
4   G G  G G G G G G
3   G G    G G G   G
2   G G    G G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3  +   +
2  &   &    c       c
1  + C + CCCCCCCC CCCCC
0  & c & cc c c c c o c
9  + C    C C C   C O C
8    cCcCccC  cCcCc o c
7   II    II  II II O
6   Ii    iI  iI Ii oO
5    OOOOOOOOOOOOOOOO
4  _ o    o   o     o _
3  - O ---O - O --- O -
2  _   _-_  _   _-_   _
1  -   ---  -   ---   -
0 _-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | C | D | Y |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   |   |   | X |
| PMOS1 | X |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |
| Poly2 |   |   |   | X |   | X |   |
| Poly3 |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O | O | O |
| PMOS1 | O | O | O | O |
| PMOS2 |   |   |   |   |
