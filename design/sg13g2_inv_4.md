# Design Documentation for sg13g2_inv_4

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
1 NpppppNNNNN
0 NpppppNpNNN
9 NpppppNNNNN
8 NpppppNNpNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SnnnnnSnnSS
3 SnnnnnSSSSS
2 SnnnnnSSSnS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
4
3
2   G G
1   G G
0   G G
9   G G
8   G G
7   G G
6   GGGG
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
  01234567890
4 &+&+&+&+&+&
3  +   +   +
2 &+   +& &+
1  + O + O +
0  + o + o +
9  + OOOOOO
8      o  o
7   IIIII O
6   IIIiI O
5         O
4  _ oOoOoo
3  - O - O -
2  _   _   _
1  -   -   -
0 -_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   | X |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   | X |   |   |
| PMOS1 |   | X | X |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   |   | X |   |
| PMOS5 |   |   | X |   |
| Poly1 | X |   |   |   |

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
