# Design Documentation for sg13g2_inv_8

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3 NNNNNNNNNNNNNNNNNN
2 pppppppNpNNNpNNNpN
1 NpppppNNNNNNNNNNNN
0 NpppppNppNpNpNpNpN
9 NpppppNNNNNNNNNNNN
8 NpppppNpNNpNpNpNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnSnnSnSSSnSSS
3 SnnnnnSSSSSSSSSSSS
2 SnnnnnSSSnSSSnSnSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3
2   G G
1   G G
0   G G
9   G G
8   G G
7   G G
6   GGGG GG
5   G G
4   G G
3   G G
2   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3  +   +  +   +   +
2 &+   +& &   &   &
1  + O +O + O + O +
0  + o +Oo& o & o &
9  + OOOOOOOO + O +
8        o  o o o
7           O   O
6    IIiIii OOOOO
5           O   O
4  _ oOoOooOo - o -
3  - O -O - O - O -
2  _   _  -_  -_ _-
1  -   -  -   -   -
0 -_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Output1 | Y | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   |   | X |   | X |
| NMOS3 |   |   |   |   | X |
| NMOS4 |   |   |   |   | X |
| NMOS5 |   |   |   |   | X |
| NMOS6 |   |   | X |   |   |
| NMOS7 |   |   | X |   |   |
| NMOS8 |   |   | X |   |   |
| PMOS1 |   |   | X | X |   |
| PMOS10 |   |   |   | X |   |
| PMOS11 |   |   |   | X |   |
| PMOS12 |   |   |   | X |   |
| PMOS13 |   |   |   | X |   |
| PMOS14 |   |   |   | X |   |
| PMOS2 |   |   | X |   |   |
| PMOS3 |   |   | X |   |   |
| PMOS4 |   | X |   |   |   |
| PMOS5 |   |   | X |   |   |
| PMOS6 |   |   | X | X |   |
| PMOS7 |   |   | X |   |   |
| PMOS8 |   |   |   | X |   |
| PMOS9 |   |   | X |   |   |
| Poly1 | X |   |   |   |   |
| Poly2 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   |   |
| NMOS4 |   |   |
| NMOS5 |   |   |
| NMOS6 |   |   |
| NMOS7 |   |   |
| NMOS8 |   |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
| PMOS3 |   |   |
| PMOS4 |   |   |
| PMOS5 |   |   |
| PMOS6 |   |   |
| PMOS7 |   |   |
| PMOS8 |   |   |
| PMOS9 |   |   |
| PMOS10 |   |   |
| PMOS11 |   |   |
| PMOS12 |   |   |
| PMOS13 |   |   |
| PMOS14 |   |   |
