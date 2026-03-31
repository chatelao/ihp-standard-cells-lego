# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NppppppNpppppppN
0 NppppppNpppppppN
9 NNNppppNpppppppN
8 NNNNNNNNpppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSnnnnnnnS
3 SnnnnnnSSSSSnnnS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2    GGG   GG G
1   GGGG   GG G
0   GGGG   GG G
9   GGGG   GG G
8   GGGG   GG G
7   GGGG   GG G
6   GGGG   GG G
5   GGGG   GG G
4   GGGG   GG G
3   GGGG   GG G
2   GGGG    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3    +        +
2  & +        +
1    +  C C   +OO
0  c +  Ccc   +Oo
9  CCCC C C    OO
8    cC C cCcCcOo
7  II C C     C O
6  iIiCcCccCc c o
5     C C     COO
4  cCcC C cCcCcOo
3  C -  C     -OO
2    -        -
1    -        -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS3 |   |   |   | X | X |
| PMOS1 |   |   |   | X | X |
| PMOS2 |   |   |   | X |   |
| PMOS3 | X |   |   |   |   |
| Poly1 |   |   | X | X |   |
| Poly2 |   |   |   | X |   |
| Poly3 |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   | O | O |
| PMOS1 |   | O | O |
| PMOS2 | O |   |   |
| PMOS3 |   |   |   |
