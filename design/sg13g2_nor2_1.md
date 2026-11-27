# Design Documentation for sg13g2_nor2_1

## Substrate
```
  0123456
4 NNNNNNN
3 SNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 NNNNNNN
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
4 ppppppp
3 NNNNNNN
2 NNNNNNN
1 NpppppN
0 NpppppN
9 NpppppN
8 NpppppN
7 NNNNNNN
6 SSSSSSS
5 SSSSSSS
4 SnnnnnS
3 SnnnnnS
2 SSSSSSS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2   GGG
1   GGG
0   GGG
9   GGG
8   GGG
7  GGGGG
6  GGGGG
5   GGG
4   GGG
3   GGG
2   GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3 +++++++
2  &+  o
1  ++ OO
0  &+ Oo
9  ++OOO
8  & OOo
7    O
6  iIO i
5    O
4  _-oO_-
3  --OO--
2  _-o _-
1 -------
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Y | A | B |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X |   |   |
| PMOS1 | X |   | X |   |   |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

