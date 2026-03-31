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
2 NNNNNNNNNNNNNN
1 NppppppNpppppp
0 NppppppNpppppp
9 NNNppppNpppppp
8 NNNNNNNNpppppp
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSnnnnnn
3 SnnnnnnSSSSnnn
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2    G    G
1   GG    G
0   GG    G
9   GG    G
8   GG    G
7   GGG   G
6   GGG   GG G
5    G    G
4    G    G
3    G    G
2    G    G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3    +       +
2    +       +
1    +       + O
0  c + cC    +oO
9  CCCC C      O
8    cC C cCcC O
7  II C C    C O
6  iIiCcCccCcCcO
5     C C CC OOO
4  cCcC C c   oO
3  C -  C    - O
2    - c     -
1    -       -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Internal2 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS3 |   |   |   | X | X |
| PMOS1 |   |   |   | X | X |
| PMOS2 |   |   |   | X |   |
| PMOS3 | X |   |   |   |   |
| Poly1 |   |   | X | X |   |
| Poly2 |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   | O |   |
| PMOS1 |   | O |   |
| PMOS2 | O |   |   |
| PMOS3 |   |   |   |
