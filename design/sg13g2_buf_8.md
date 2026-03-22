# Design Documentation for sg13g2_buf_8

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NppppppNNNpNNNpNNNpNNNp
1 NpppppNNNNNNNNNNNNNNNNN
0 NppppppNpNpNpNpNpNpNNNN
9 NpppppNNNNNNNNNNNNNNNNN
8 NpppppNNNNNNNNpNNNNNpNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnSSnSnSnSnSnSnSSnS
3 SnnnnnSSSSSSSSSSSSSSSSS
2 SnnnnnSnSSSnSnSSSnSSSnS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2     G
1     G
0     G
9   G G
8   G G
7   G G
6   GGGG
5   G G
4   G G
3     G
2     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3   +   +   +   +   +  +
2   +   &   &   &   &  +&
1  C+ C + O + O + O + O+
0  C+ C &co & o & o & O+
9  CCCCCC OOOOOOOOOOOOO+
8        c      o     o
7        C            O
6  cIIIi ccCcCcCcCcC  OO
5        C            O
4  CCCCCCcoOoOoOoOoOoOO_
3  C- C - O - O - O - O-
2   -_  -_  -_ _-  _-  _
1   -   -   -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | X | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS10 |   | X |   |   |
| NMOS11 |   | X |   |   |
| NMOS12 |   | X |   |   |
| NMOS13 |   | X |   |   |
| NMOS14 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   |   |   | X |
| NMOS8 |   | X |   |   |
| NMOS9 |   | X |   |   |
| PMOS1 |   |   | X |   |
| PMOS10 |   |   | X |   |
| PMOS11 |   |   | X |   |
| PMOS12 |   |   | X |   |
| PMOS13 |   |   | X |   |
| PMOS14 |   |   | X |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   |   | X |   |
| PMOS6 |   | X |   |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   | X |   |   |
| PMOS9 |   |   | X |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 |   |
| NMOS4 |   |
| NMOS5 |   |
| NMOS6 |   |
| NMOS7 |   |
| NMOS8 |   |
| NMOS9 |   |
| NMOS10 |   |
| NMOS11 |   |
| NMOS12 |   |
| NMOS13 |   |
| NMOS14 |   |
| PMOS1 | O |
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
| PMOS13 |   |
| PMOS14 |   |
