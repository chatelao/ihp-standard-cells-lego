# Design Documentation for sg13g2_and2_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 NNNNNNNNN
1 NpppppppN
0 NpppppppN
9 NpppppppN
8 NpppppppN
7 SSSSSSSSS
6 SSSSSSSSS
5 SnnnnnnnS
4 SnnnnnnnS
3 SnnnnnnnS
2 SSSSSSSSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
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
  012345678
4 +++++++++
3  +   +
2 &+  &+
1  + C +OOO
0  +cC +oOo
9    C  OOO
8  CcCcCoOo
7  C I C  O
6  c i iC o
5  C      O
4      -oOo
3 III  -OOO
2 iIi _-
1      -
0 ---------
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
