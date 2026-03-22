# Design Documentation for sg13g2_einvn_4

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
2 ppppNNNNpNNNpNNpppppNNN
1 ppppNNNNNNNNNNNpppppNNN
0 ppppNNNNpNNNNNNppppppNN
9 ppppNNNNNNNNNNNpppppNNN
8 ppppNNNNNNNNNNppppppNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 nnnnSSSSSSSSSSnnnnnnnSS
3 nnnnSSSSSSSSSSSnnnnnSSS
2 nnnnSSSSSnSSSnSnnnnnSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2 G G             G G
1 G G             G G
0 G G             G G
9 G G             G G
8 G G             G G
7 G G             G G
6 GGG             GGG G
5 G G             G G
4 G G             G G
3 G G             G G
2 G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3  +      +  +
2  +      &  +&CcCCCCCcC
1  + C  C +C + C   C   C
0  + C cC &Cc+ CcO C OoCc
9  + C  C +C + C O   O C
8    C  C  Cc  CoOOOOO
7  IIC  CCCCCCCC  OIIII
6  IIc   CCCcCCCC OIiIi
5    C   C  C   C OOOOO
4  _ CCc c- c _ o O   o c
3  - CCC C- C - CCCCC   C
2  _      -_  -_c   CCcCc
1  -      -   -
0 -_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Output1 | Z | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   |   |   |   | X |
| NMOS3 |   |   |   |   | X |
| NMOS4 |   |   |   |   | X |
| NMOS5 |   | X | X |   |   |
| PMOS2 |   |   | X |   |   |
| PMOS3 |   |   |   | X |   |
| PMOS4 |   |   |   | X |   |
| PMOS5 |   |   |   | X |   |
| PMOS6 |   |   |   | X |   |
| Poly2 | X |   |   |   |   |
| Poly3 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   |   |   |
| NMOS4 |   |   |   |
| NMOS5 |   | O |   |
| PMOS1 | O |   |   |
| PMOS2 |   | O |   |
| PMOS3 |   |   |   |
| PMOS4 |   |   |   |
| PMOS5 |   |   |   |
| PMOS6 |   |   |   |
