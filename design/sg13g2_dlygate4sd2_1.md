# Design Documentation for sg13g2_dlygate4sd2_1

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
2    G G  G
1   GG G  G
0   GG G  G
9   GG G  G
8   GG G  G
7   GGGG  G
6   GGGG  GG G
5    G G  G
4    G G  G
3    G G  G
2    G G  G
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
1    +    C  + O
0  c + cC c  +oO
9  CCCC C C    O
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

| Silicon | VDD | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   |   |   |   |   |
| NMOS3 |   |   |   |   | X |
| PMOS1 |   |   |   |   | X |
| PMOS2 |   |   |   |   | X |
| PMOS3 | X |   |   |   |   |
| Poly1 |   |   | X | X | X |
| Poly2 |   |   |   |   | X |
| Poly3 |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   | O |   |
| PMOS1 |   | O |   |
| PMOS2 | O |   |   |
| PMOS3 |   |   |   |
