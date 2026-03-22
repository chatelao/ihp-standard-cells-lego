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
2 NNppppppppNN
1 NNNpppppppNN
0 NNNppppppppN
9 NNNpppppppNN
8 NNNppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSnnnnnnnnS
3 SSSnnnnnnnSS
2 SSSnnnnnnnSS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2     G G
1     G G
0     G G
9     G G G
8     G G G
7     G G G
6    GGGGGG
5     G G G
4     GGG G
3     G G G
2     G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +   ++
2   &+   ++
1   C+ C ++ OO
0  cC+ C ++ oO
9   C  C    OO
8  cCCCCCCC oO
7   C II ICC O
6  cCiII ICCcO
5   C      OOO
4      I _ Oo
3      I - O
2  IIIII _
1        -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | B | X | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   | X |   | X |
| PMOS1 |   | X | X |   |
| PMOS2 |   |   | X |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
