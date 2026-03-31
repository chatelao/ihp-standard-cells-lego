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
2 NNNNNNNNNNNNNNNNNNNNN
1 NppppppppppppppNppppp
0 NppppppppppppppNppppp
9 NppppppppppppppNppppp
8 NppppppppppppppNppppp
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 Snnnnnnnnnnnnnnnnnnnn
4 Snnnnnnnnnnnnnnnnnnnn
3 Snnnnnnnnnnnnnnnnnnnn
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890
4
3
2   GG    G   GG  GGGG
1   GG    G   GG  GGGG
0   GG    G   GG  GGGG
9   GG    G   GG  GGGG
8   GG    G   GG  GGGG
7   GG    GG  GG  GGGG
6   GG    GG  GG  GGGG
5   GG    G   GG  GGGG
4   GG    G   GG  GGGG
3   GG    G   GG  GGGG
2   GG    G   GG  GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3  +   +
2  +   +    c       c
1  + C + CCCCCCCC CCCCC
0  + c + cc c c c c o c
9  + C    C C C   C O C
8    cCcCccC  cCcCc o c
7   II    II  II II O
6   Ii    iI  iI Ii oO
5    OOOOOOOOOOOOOOOO
4  - o    o   o     o -
3  - O ---O - O --- O -
2  -   ---  -   ---   -
1  -   ---  -   ---   -
0 _-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | C | D | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   | X |
| PMOS1 |   |   |   |   |   |   | X |   |
| PMOS2 |   |   |   |   |   |   | X | X |
| PMOS3 | X |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   | X | X |
| Poly2 |   |   |   | X |   |   | X | X |
| Poly3 |   |   |   |   | X |   | X | X |
| Poly4 |   |   |   |   |   | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O | O | O |
| PMOS1 | O | O | O |   |
| PMOS2 |   |   |   | O |
| PMOS3 |   |   |   |   |
