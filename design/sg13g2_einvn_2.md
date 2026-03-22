# Design Documentation for sg13g2_einvn_2

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
2 ppppNNNNpNNNpppp
1 ppppNNNNNNNNpppp
0 ppppNNNNpNNNpppp
9 ppppNNNNNNNNpppp
8 ppppNNNNNNNNpppp
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 nnnnSSSSSSSSnnnn
3 nnnnSSSSSSSSnnnn
2 nnnnSSSnSSSSnnnn
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2 G            G G
1 G            G G
0 G            G G
9 G G          G G
8 G G          G G
7 G G          G G
6 GGGG         GGG
5 G G          G G
4 G G          G G
3 G            G G
2 G            G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3   +     +
2   +     & cCCCC
1   + C C + C   C
0   + CcCc& c o C
9     C CCCCC O C
8  IIICc  c   o
7  IIIC       O
6  IIiCc      O I
5  IIIC       O I
4     C CccCc o I
3   - C C - CCCCC
2   -_ c _- c
1   -     -
0 -_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | TE_B | Z | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   | X |   |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   |   | X |   |
| PMOS4 |   |   | X |   |
| PMOS5 |   |   | X |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   |   |
| NMOS4 |   | O |
| PMOS1 | O |   |
| PMOS2 |   | O |
| PMOS3 |   |   |
| PMOS4 |   |   |
| PMOS5 |   |   |
