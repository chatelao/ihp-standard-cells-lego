# Design Documentation for sg13g2_dlygate4sd1_1

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
2 pppppNNNNNpNNN
1 ppppNNNNNNNNNN
0 ppppNNNNNNNNpN
9 ppppNNNNNNNNNN
8 ppppNNNNNNNNpN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 nnnnSSSSSSSSnS
3 nnnnSSSSSSSSSS
2 nnnnSSSSSSSnSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
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
  01234567890123
4 &+&+&+&+&+&+&+
3    +       +
2    +&     &+
1    +       + O
0  C + cC    +oO
9  CCCC C      O
8     CcC cCcCoO
7  II C C    C O
6  IIcCcCcc cCcO
5     C C CCCOOO
4  CCCC C c   oO
3  C -  C    - O
2    _ c     _
1    -       -
0 -_-_-_-_-_-_-_
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
| PMOS3 | X |   |   |
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
