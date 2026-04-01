# Design Documentation for sg13g2_nor4_1

## Substrate
```
  01234567890
4 SSSSSSSSSSS
3 NNNNNNNNNNN
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
0 NNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3
2
1  ppppppppp
0  ppppppppp
9  ppppppppp
8  ppppppppp
7
6
5
4  nnnnnnnnn
3  nnnnnnnnn
2
1
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
4
3
2   G G G
1   G G G
0   G G G
9   G G G
8   G G G
7   G G G
6  GG GGGGG
5   G G G
4   G G G
3   G G G
2   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  C
2  c      c
1  C      OO
0  c     IoO
9  C     IOO
8  c   I IcO
7  I I I IIO
6  i iIi IiO
5          O
4  c oOOOoOO
3  C O C O C
2  c c c ccC
1  C   C   C
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Internal1 | Internal4 | Output1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | X |   | X |
| PMOS1 |   |   |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |   |
| Poly2 |   |   |   | X | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
