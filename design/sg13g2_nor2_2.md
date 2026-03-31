# Design Documentation for sg13g2_nor2_2

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
2   GGG GG
1   GGG GG
0   GGG GG
9   GGG GG
8   GGG GG
7   GGG GG
6   GGG GG
5   GGG GG
4   GGG GG
3   GGG GG
2   GGG GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3    +
2  & +   c
1  C + CCCCC
0  c + c ocC
9  CCCCC OOO
8    c    oO
7          O
6    i  IioO
5          O
4  - oOoOooO
3  - O - O -
2  -   -   -
1  -   -   -
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   |   |   |   | X |
| PMOS1 |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X |   | X | X |
| Poly2 |   |   |   | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
