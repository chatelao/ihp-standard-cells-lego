# Design Documentation for sg13g2_nand4_1

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
2 NpppppppppN
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
2       G
1       G
0       G
9       G
8       G
7       G
6  G G GGG
5       G
4       G
3       G
2       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 +++++++++++
3  +   +   +
2  +&O&+ O&+
1  + O + O +
0  +oO +oO +
9  + OOOOOOO
8       o  O
7  I I     O
6  i i i ioO
5      I I O
4  -    iIoO
3  -     I O
2  -_ _
1  -
0 -----------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | A | B | C | D | Y |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   | X |   |   |   | X |
| PMOS1 | X |   |   |   |   | X |
| Poly1 |   | X | X |   |   | X |
| Poly2 |   |   |   |   | X |   |
| Poly3 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | N | N |
| PMOS1 | O |   |   |
| PMOS2 |   |   |   |
