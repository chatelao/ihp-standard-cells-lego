# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNpppppNNNNpNNpppppNNpNNNN
1 NNNpppppNNNNNNNpppppNNNNNNN
0 NNNpppppNNNNNNNpppppNNpNpNN
9 NNNpppppNNNNNNNpppppNNNNNNN
8 NNNpppppNNNNNNNpppppNNNNpNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSnnnnnSSSnSSSnnnnnSSSnnSS
3 SSSnnnnnSSSSSSSnnnnnSSSSSSS
2 SSSnnnnnSSSSSnSnnnnnSSSnSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2     G G         G
1     G G         G
0     G G         G G
9     G G         G G
8     G G         G G
7     GGG         GGG
6     G G         G G
5     G G         G G
4     G G         G G
3     G G         G G
2     G G         G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +        +     +   +
2    +        &     +   &
1  C +  CCC       C +C  + O
0  c    C c c cCcCC  Cc & o
9  C CCCCCCCCCC C C  CC + O
8  c C I C    c c CI  cC  o
7  C C I C C  CCC CII  C  O
6  cCc c c CcCcCc C   cCc O
5  C CCCC       C C-  CC  O
4  cCCCCCCc  _- c  _  cC _o
3  C   C      -    -     -O
2    _ CCCcCcC-_   _     _
1    -        -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | GCLK | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS3 |   |   | X |
| NMOS4 |   |   | X |
| NMOS5 |   |   | X |
| NMOS6 |   |   | X |
| NMOS7 | X |   | X |
| PMOS3 | X |   |   |
| PMOS4 |   | X |   |
| PMOS5 | X |   |   |
| PMOS6 |   | X |   |
| PMOS7 |   | X |   |
| PMOS8 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   |   |
| NMOS4 |   | O |
| NMOS5 |   |   |
| NMOS6 |   |   |
| NMOS7 |   |   |
| PMOS1 | O |   |
| PMOS2 |   | O |
| PMOS3 |   |   |
| PMOS4 |   |   |
| PMOS5 |   |   |
| PMOS6 |   |   |
| PMOS7 |   |   |
| PMOS8 |   |   |
