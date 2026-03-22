# Design Documentation for sg13g2_nor3_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
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
2 NpppppppN
1 NpppppppN
0 NpppppppN
9 NpppppppN
8 NpppppppN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SnnnnnnnS
3 SnnnnnnnS
2 SnnnnnnnS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2 G G G G G
1 G G G G G
0 G G G G G
9 G G G G G
8 G G G G G
7 G G G G G
6 GGGGGGGGG
5 G G G G G
4 G G G G G
3 G G G G G
2 G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +
2  +&
1  +     O
0  +   o o
9  +  OOOO
8    oO
7     O
6  I oOI I
5     O
4  _ oOoOo
3  -  O- O
2  _   _
1  -   -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Y | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 | X |   | X |
| PMOS1 | X | X |   |
| PMOS2 |   | X |   |
| Poly1 | X | X |   |

## Silicon Neighbourhood

| Silicon | NMOS1 | NMOS2 | PMOS1 | PMOS2 | Poly1 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 |   |   |   |   | O |
| PMOS1 |   |   |   |   | O |
| PMOS2 |   |   |   |   |   |
| Poly1 |   | O | O |   |   |
