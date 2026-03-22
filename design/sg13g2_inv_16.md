# Design Documentation for sg13g2_inv_16

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNpNpNNNpNNNpNNNpNNNpNNNpNNNpppppp
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNppppp
0 NNNpNNNpNNNNNNpNpNpNpNpNpNpNpppppp
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNppppp
8 NNNpNpNppNpNpNpNpNpNpNpNpNpNpppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnSnSnSnSnSSSnnSSSnSSSnSSSnSnnnnnn
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnn
2 SnSSSnSSSnSSSnSSSnSSSnSnSSSnSnnnnn
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2                               G
1                               G
0                               G
9                               G
8                               G G
7                               G G
6                               GGG
5                               G G
4                               G G
3                               G G
2                               G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +   +   +   +  +   +   +   +   +
2  +& &+  &+  &+  &   &   &   &   +
1  + O + O + O +O + O + O + O + O +
0  + o + o + O +o & o & o & o & O +
9  + O   O   O  O   O   O   O   O +
8    oOoOooOoOoOoOoOoOoOoOoOoOoOO
7    O   O   O  O   O   O   O
6    O   O   O  O   O   O   O   iIi
5    O   O   O  O   O   O   O
4  _ o _ o _ O _o - o - o - oOoOO_
3  - O - O - O -O - O - O - O - O-
2  _   _   _   _  -_  -_ _-  _-  _
1  -   -   -   -  -   -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS10 |   | X |   | X |
| NMOS11 |   |   |   | X |
| NMOS12 |   | X |   |   |
| NMOS13 |   |   |   | X |
| NMOS14 |   | X |   |   |
| NMOS15 |   |   |   | X |
| NMOS16 |   | X |   | X |
| NMOS17 |   | X |   |   |
| NMOS18 |   | X |   |   |
| NMOS19 |   | X |   |   |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   |   |   | X |
| NMOS8 |   |   |   | X |
| NMOS9 |   |   |   | X |
| PMOS1 |   | X |   |   |
| PMOS10 |   | X |   |   |
| PMOS11 |   | X |   |   |
| PMOS12 |   | X |   |   |
| PMOS13 |   | X | X |   |
| PMOS14 |   | X |   |   |
| PMOS15 |   | X |   |   |
| PMOS16 |   | X |   |   |
| PMOS17 |   |   | X |   |
| PMOS18 |   | X |   |   |
| PMOS19 |   |   | X |   |
| PMOS2 |   | X |   |   |
| PMOS20 |   | X |   |   |
| PMOS21 |   |   | X |   |
| PMOS22 |   | X |   |   |
| PMOS23 |   |   | X |   |
| PMOS24 |   |   | X |   |
| PMOS25 |   |   | X |   |
| PMOS26 |   |   | X |   |
| PMOS27 |   |   | X |   |
| PMOS28 |   |   | X |   |
| PMOS29 |   |   | X |   |
| PMOS3 |   | X |   |   |
| PMOS30 |   |   | X |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   | X |   |   |
| PMOS7 |   | X |   |   |
| PMOS8 |   | X |   |   |
| PMOS9 |   | X |   |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 |   |
| NMOS3 |   |
| NMOS4 |   |
| NMOS5 |   |
| NMOS6 |   |
| NMOS7 |   |
| NMOS8 |   |
| NMOS9 |   |
| NMOS10 | O |
| NMOS11 |   |
| NMOS12 |   |
| NMOS13 |   |
| NMOS14 |   |
| NMOS15 |   |
| NMOS16 |   |
| NMOS17 |   |
| NMOS18 |   |
| NMOS19 |   |
| PMOS1 |   |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
| PMOS5 |   |
| PMOS6 |   |
| PMOS7 |   |
| PMOS8 |   |
| PMOS9 |   |
| PMOS10 |   |
| PMOS11 |   |
| PMOS12 |   |
| PMOS13 | O |
| PMOS14 |   |
| PMOS15 |   |
| PMOS16 |   |
| PMOS17 |   |
| PMOS18 |   |
| PMOS19 |   |
| PMOS20 |   |
| PMOS21 |   |
| PMOS22 |   |
| PMOS23 |   |
| PMOS24 |   |
| PMOS25 |   |
| PMOS26 |   |
| PMOS27 |   |
| PMOS28 |   |
| PMOS29 |   |
| PMOS30 |   |
