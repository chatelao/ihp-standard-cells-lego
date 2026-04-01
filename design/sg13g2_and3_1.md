# Design Documentation for sg13g2_and3_1

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NNNNNNNppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SnnnnnnnnnSS
4 SnnnnnnnnnSS
3 SnnnnnnnnnSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2  G G GGGG
1  G G GGGG
0  G G GGGG
9  G G GGGG
8  G G GGGG
7  G GGGGGGG
6  G G GGGGG
5  G G GGGG
4  G G GGGG
3  G G GGGG
2  GGG G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +   ++
2    +   ++
1  C + C ++ OO
0  c + c ++ oO
9  C   C    OO
8  cCcCcCcc  O
7  C  IIIICC O
6  c  IiIicC O
5  C       OOO
4  c  Ii - Oo
3  IIIII - O
2  iIiIi -
1        -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   | X |   | X |   |
| PMOS1 |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
