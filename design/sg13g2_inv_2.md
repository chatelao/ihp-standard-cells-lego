# Design Documentation for sg13g2_inv_2

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
2 pppppNN
1 ppppNNN
0 ppppNNN
9 ppppNNN
8 ppppNpN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 nnnnSnS
3 nnnnSSS
2 nnnnSnS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2 G G
1 G G
0 G G
9 G G
8 G G
7 G G
6 GGG
5 G G
4 G G
3 G G
2 G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3  +   +
2  +  &+
1  + O +
0  + o +
9  + O +
8    o o
7    O
6  I OOO
5    O
4  _ o _
3  - O -
2  _   _
1  -   -
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Output1 | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   | X |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| PMOS1 |   | X | X |   |
| PMOS2 | X |   |   |   |
| PMOS3 |   |   | X |   |

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
