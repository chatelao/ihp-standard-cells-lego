# Design Documentation for sg13g2_nor3_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 SNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 NNNNNNNNN
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
7 NNNNNNNNN
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
2   G GGG
1   G GGG
0   G GGG
9   G GGG
8   G GGG
7  GG GGGG
6  GG GGGG
5   G GGG
4   G GGG
3   G GGG
2   G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3 +++++++++
2  &+
1  ++    OO
0  &+ OOOoO
9  ++OOOOOO
8  & OO  o
7    OO
6  i OOi i
5    OO
4  _-oOOOoO
3  --OO--OO
2  _-  _-o
1 ---------
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | B | A | C |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X |   |   |
| PMOS1 | X |   | X |   |   |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   |   | X |   |
| Poly2 |   | X | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |

