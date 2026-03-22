# Design Documentation for sg13g2_and2_2

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
2 pppppppNpNN
1 ppppppNNNNN
0 ppppppNppNN
9 ppppppNNNNN
8 ppppppNpNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 nnnnnnSnSSS
3 nnnnnnSSSSS
2 nnnnnnSSSnS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
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
  01234567890
4 &+&+&+&+&+&
3  +   +  +
2  +   +& &
1  + C + O+
0  + C + o&
9    C   O+
8  CCCCC o
7  C   C O
6  c I c O
5  C     O
4      _ o-
3 III  - O-
2 III  _  -_
1      -  -
0 -_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | X | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS3 |   |   | X |
| NMOS4 | X |   |   |
| PMOS1 |   | X |   |
| PMOS2 | X |   |   |
| PMOS3 | X | X |   |
| PMOS4 |   | X |   |
| PMOS5 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 |   |
| NMOS4 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
| PMOS5 |   |
