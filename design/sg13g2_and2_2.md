# Design Documentation for sg13g2_and2_2

## Substrate
```
  01234567890
4 NNNNNNNNNNN
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NpppppppppN
0 NpppppppppN
9 NpppppppppN
8 NpppppppppN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SnnnnnnnnnS
4 SnnnnnnnnnS
3 SnnnnnnnnnS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
4
3
2 G GGG
1 G GGG
0 G GGG
9 GGGGGG
8 GGGGGG
7 GGGGGG
6 GGGGGG
5 GGGGGG
4 GGGGG
3 GGGGG
2 GGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 +++++++++++
3  +   +  +
2 &+  &+  + &
1  + C +OO+
0  +cC +oO+
9    C  OO+
8  CcCcC O
7  C I CCO
6  c i iCo
5  C     O
4      -oO-
3 III  -OO-
2 iIi _-  - _
1      -  -
0 -----------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   | X |
| PMOS1 |   |   |   |   | X | X |
| Poly1 | X | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
