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
2 NNNNNNN
1 NpppppN
0 NpppppN
9 NpppppN
8 NpppppN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SnnnnnS
3 SnnnnnS
2 SSSSSSS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2
1
0
9
8
7
6  G   G
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 +++++++
3  +
2  + &
1  +   O
0  +   o
9  + OOO
8    o
7    O
6  iIo i
5    O
4  - Oo-
3  - O -
2  -_ _-_
1  -   -
0 -------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B | Y |
| --- | --- | --- | --- |
| NMOS2 |   |   | X |
| PMOS1 |   |   | X |
| Poly1 | X |   |   |
| Poly2 |   | X |   |

