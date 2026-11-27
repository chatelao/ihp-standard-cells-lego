# Design Documentation for sg13g2_inv_4

## Substrate
```
  01234567890
4 NNNNNNNNNNN
3 SNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 NNNNNNNNNNN
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
7 NNNNNNNNNNN
6 SSSSSSSSSSS
5 SSSSSSSSSSS
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
2   G G GGG
1   G G GGG
0   G G GGG
9   G G GGG
8   G G GGG
7   GGGGGGG
6   GGGGGGG
5   G G GGG
4   G G GGG
3   G G GGG
2   G G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3 +++++++++++
2  & o+& o+&
1  +OO++OO++
0  &Oo+&Oo+&
9  +OOOOOOO
8  & oOOOoOO
7   IIIII OO
6   Iiiii OO
5         OO
4  _OoOOOoOO
3  -OO--OO--
2  _ o-_ o-_
1 -----------
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Y | A |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X |   |
| PMOS1 | X |   | X |   |
| PMOS2 | X |   |   |   |
| Poly1 |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

