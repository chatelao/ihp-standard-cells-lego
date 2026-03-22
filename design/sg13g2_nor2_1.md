# Design Documentation for sg13g2_nor2_1

## Substrate
```
  0123456
4 NNNNNNN
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 SSSSSSS
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
2 ppppNpp
1 NpppNpp
0 NpppNpp
9 NpppNpp
8 NpppNpp
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SnnnSnn
3 SnnnSnn
2 SnnnSnn
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2       G
1       G
0       G
9       G
8   G   G
7   G   G
6  GG  GG
5   G   G
4       G
3       G
2       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3   +
2 & +
1   +  O
0   +  o
9   +OOO
8    o
7    O
6  I O I
5    O
4  _-o _
3   -O -
2  _-  _
1   -  -
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Y | VDD | VDD2 | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 | X |   |   | X |
| NMOS3 |   |   |   | X |
| PMOS1 | X |   | X |   |
| PMOS2 | X |   |   |   |
| PMOS3 |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 |   | N |
| NMOS3 | O |   |
| PMOS1 |   | O |
| PMOS2 | O |   |
| PMOS3 |   |   |
