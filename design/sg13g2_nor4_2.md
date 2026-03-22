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
2 pppppppppppppppppppNN
1 NpppppNppppppppppppNN
0 NpppppNppppppppppppNN
9 NpppppNppppppppppppNN
8 NpppppNppppppppppppNN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SnnnnnSnnnnnnnnnnnnSS
3 SnnnnnSnnnnnnnnnnnnSS
2 SnnnnnSnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890
4
3
2   G G   G GG G G G
1   G G   G GG G G G
0   G G   G GG G G G
9   G G   G GG G G G
8   G G   G GG G G G
7   G G   G GG G G G
6   GGG   GGGGGG GGG
5   G G   G GG G G G
4   G G   G GG G G G
3   G G   G  G G   G
2   G G   G  G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3  +   +
2 &+   +&CCCCCCCC CCCCc
1  + C + C  C   C C   C
0  + C + CC C C C C o c
9  + CCCCCC C CCCCC O C
8                   o c
7                   O
6  cII c ciI  IIcII OO
5    OOOOOOOOOOOOOOOO
4  _ o   oO   o     o -
3  - O ---O - O --- O -
2  _   _-_ _-   ---  _-
1  -   ---  -   ---   -
0 -_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | B | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   | X |   | X |
| NMOS3 |   | X |   | X |
| PMOS1 |   | X | X |   |
| PMOS2 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   | O | O |
| PMOS1 | O | O | O |
| PMOS2 |   |   |   |
