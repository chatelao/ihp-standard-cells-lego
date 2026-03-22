# Design Documentation for sg13g2_dlhrq_1

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
2 ppppppppNNpNNNNNNNppppppNNN
1 ppppppppNNNNNNNNNNNpppppNNN
0 ppppppppNNNNNNNNNNNppppppNN
9 ppppppppNNNNNNNNNNNpppppNNN
8 ppppppppNNNNNNNNNNNppppppNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnnnnnSSSSSSSSSSSnnnnnnSS
3 nnnnnnnnSSSSSSSSSSSnnnnnSSS
2 nnnnnnnnSSSSSSSSSnSnnnnnSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2 G G G G             G
1 G G G G             G
0 G G G G             G
9 G G G G             G
8 G G G G             G G
7 G G G G             G G
6 GGG GGG             GGG
5 G G G G             G G
4 G G G G             G G
3 G G   G             G
2 G G   G             G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +      +       +   +
2    +      & cCcC  &   +
1  C +      + C  C  + C + OO
0  CCCCCCCcCc cCcC  c C + oO
9  CCC CC C C CC C CCCC + OO
8    C  C c c cCcCcCc C   oO
7  I CIICCC CCC C   C CI   O
6  I cIICcc c c cCc c CI CcO
5  CCC  C CCCCC CC   CCCCC O
4  C    CCcCcC CcC  cC    oO
3     - C     C  C - C  - OO
2    _-     - cCcC _   _-
1     -     -      -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Q | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS3 |   |   | X |
| NMOS4 | X |   | X |
| PMOS2 | X | X |   |
| PMOS3 |   | X |   |
| PMOS4 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| NMOS3 |   |   |   |
| NMOS4 |   |   | O |
| PMOS1 | O | O |   |
| PMOS2 |   |   | O |
| PMOS3 |   |   |   |
| PMOS4 |   |   |   |
