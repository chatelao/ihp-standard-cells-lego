# Design Documentation for sg13g2_ebufn_2

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
3 NNNNNNNpNNNNNNNNNN
2 NNNNNNNpNNNNNNNNNN
1 NpppppppppNpppppNN
0 NpppppppppNpppppNN
9 NpppppppppNpppppNN
8 NpppppppppNpppppNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnSnnnnnSS
3 SnnnnnnnnnSnnnnnSS
2 SnnnnnnnnnSnnnnnSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3
2   G GGGGG G G G
1   G GGGGG G G G
0   G GGGGG G G G
9   G GGGGG G G G
8   G GGGGG G G G
7   G GGGGGGGGG G
6   G GG GG G G G
5   G  G GG G G G
4   G  G GG G G G
3   G  G GG G G G
2   G  G GG G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3        +     +
2  cCcCc +c    +&
1  C   CCCCC   + CC
0  c o c c CcCcCcCc
9    O C   C     CC
8    o c  cCcC   Cc
7    O     CC     C
6    oCiCccCc i i c
5    O      C I I C
4  c o cCcc cCc- Cc
3  C   C -C  C - CC
2  cCcCc -c  C -
1        -     -
0 _-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Input1 | TE_B | Internal1 | Internal2 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | X |   | X |
| NMOS3 |   |   |   |   |   |   | X |   |
| PMOS1 | X |   |   |   |   |   | X | X |
| PMOS2 |   |   |   |   |   |   | X |   |
| Poly1 |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   | X | X | X | X |   |
| Poly3 | X |   | X |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| NMOS3 |   | O | O |
| PMOS1 | O | O |   |
| PMOS2 |   | O | O |
