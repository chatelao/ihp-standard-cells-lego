# Design Documentation for sg13g2_and2_1

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
2 pppppppNN
1 ppppppNNN
0 ppppppNpN
9 ppppppNNN
8 ppppppNpN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 nnnnnnSnS
3 nnnnnnSSS
2 nnnnnnSSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2 G G G
1 G G G
0 G G G
9 G G G
8 G G G
7 G G G
6 G GGG
5 G G G
4 G G G
3 GGG G
2 G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +   +
2  +   +&
1  + C + OO
0  + C + oO
9    C   OO
8  CCCCC oO
7  C   C  O
6  c I c  O
5  C      O
4      _ oO
3 III  - OO
2 III  _
1      -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | X | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS3 | X |   |   |
| PMOS1 |   | X |   |
| PMOS2 | X |   |   |
| PMOS3 | X |   |   |
| PMOS4 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
