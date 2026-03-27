# Design Documentation for sg13g2_buf_1

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
2 NpppppN
1 NpppppN
0 NpppppN
9 NpppppN
8 NpppppN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SnnnnnS
3 SnnnnnS
2 SnnnnnS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2   G
1   G
0   G
9   G
8  GG
7   G
6   G  G
5   G
4   G
3   G
2   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3    +
2    &
1  C + O
0  c   o
9  CCC O
8  iIc o
7  IIC O
6  c cCo
5  CCC O
4  c _ o
3    - O
2    _ o
1    -
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | A | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X |   | X |
| PMOS1 | X |   | X | X | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   |   | X |   |
| Poly2 |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
