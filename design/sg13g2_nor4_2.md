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
2 ppppppppppppppppppppp
1 NpppppppppppppppppppN
0 ppppppppppppppppppppp
9 NpppppppppppppppppppN
8 ppppppppppppppppppppp
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
2   G        G G G G
1   G     G GG G G G
0   G        G G G G
9   G G   G GG G G G
8   G G      G G G G
7   G G   G GG G G G
6   GGG  GGGGGGGGGGG
5   G G   G GG G G G
4   G          G   G
3   G     G    G   G
2   G     G    G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3  +   +
2 &+Cc&+CccCcCcCcCcCcCc
1  +CC +CCCCCCCCCCCCCCC
0 &+Cc&+CccCcCcCcCc oCc
9  +CCCCCCCCCCCCCCC OCC
8 & CcCcCccCcCcCcCc oCc
7                   O
6   Ii   iiii iIiIi OO
5    OOOOOOOOOOOOOOOO
4  _ o _ _o o_o o_o o_-
3  - O ---O - O --- O -
2  _   _-_  -_  -_-  _-
1  -   ---  -   ---   -
0 -_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B | D | Y | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | X |
| NMOS2 |   |   |   | X |   | X |
| PMOS1 |   |   | X | X | X |   |
| PMOS2 |   |   |   |   | X |   |
| Poly1 | X |   |   |   |   |   |
| Poly2 |   | X | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O |   |   |
| PMOS1 | O | O |   | O | O |
| PMOS2 |   |   |   |   |   |
