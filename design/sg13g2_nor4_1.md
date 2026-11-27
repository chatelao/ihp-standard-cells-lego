# Design Documentation for sg13g2_nor4_1

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
5 SnnnnnnnnnS
4 SnnnnnnnnnS
3 SnnnnnnnnnS
2 SnnnnnnnnnS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
4
3
2   G G G G
1   G G G G
0   G G G G
9   G G G G
8   G G G G
7   G G G G
6  GGGGGGGG
5  GG GGGGG
4   G G G G
3   G G G G
2   G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  C
2  c      Oo
1  C      OO
0  c    IIOo
9  C   IIIOO
8     II IOo
7  I I I IIO
6  i IiiIIiO
5    III IIO
4  c oOOOoOO
3  C O COO C
2  c o c o c
1  C   C   C
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS2 | VSS3 | VSS4 | Y | A | B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |
| NMOS2 |   |   |   | X | X | X | X |   |   |
| PMOS1 | X |   |   |   |   |   | X |   |   |
| PMOS2 |   | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

