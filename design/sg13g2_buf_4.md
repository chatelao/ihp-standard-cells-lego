# Design Documentation for sg13g2_buf_4

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 NNNNNNNNNNNNNN
2 pNNNpNNNpppppp
1 NNNNNNNNNppppp
0 NNNpNNNppppppp
9 NNNNNNNNNppppp
8 NpNpNpNppppppp
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnSnSnSnSnnnnn
3 SSSSSSSSSnnnnn
2 SnSSSnSSSnnnnn
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2           G
1           G
0           G
9           G G
8           G G
7           G G
6           GGG
5           G G
4           G G
3             G
2           G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +   +  +   +
2 &+  &+  &   +
1  + O + O+   +
0  + o + o& C +
9  + O   O+ C
8  & oOoOo& CCCC
7    O      II C
6  OOO  Ccc iI C
5    O    C    C
4  _ oOoOocCCCCC
3  - O - O -- CC
2  _   _   _
1  -   -   -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | X | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   | X |   |   |
| NMOS7 |   | X |   |   |
| NMOS8 |   | X |   |   |
| PMOS1 |   |   | X |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   | X | X |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 |   |   |
| NMOS3 |   |   |
| NMOS4 | O | O |
| NMOS5 |   |   |
| NMOS6 |   |   |
| NMOS7 |   |   |
| NMOS8 |   |   |
| PMOS1 |   |   |
| PMOS2 |   |   |
| PMOS3 |   |   |
| PMOS4 |   | O |
| PMOS5 |   |   |
| PMOS6 |   |   |
| PMOS7 |   |   |
| PMOS8 |   |   |
