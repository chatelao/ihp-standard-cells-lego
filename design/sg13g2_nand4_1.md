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
2   G GG G
1   G GG G
0   G GG G
9   G GG G
8   G GG G
7   G GG G
6  GGGGG G
5   G GG G
4   G GG G
3   G GG G
2   G GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  +   +   +
2  + & + o +
1  + O + O +
0  + o + o +
9  + OOOOOOO
8      o   O
7  I I     O
6  i i i ioO
5      I I O
4  -   i ioO
3  -     I O
2  - _
1  -
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | A | B | C | D | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |
| NMOS2 |   |   |   | X | X |   |   | X |
| PMOS1 |   | X |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X | X | X | X |
| Poly2 |   |   |   | X |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
