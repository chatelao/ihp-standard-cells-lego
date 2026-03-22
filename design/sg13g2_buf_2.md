# Design Documentation for sg13g2_buf_2

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 pNNNNpppp
1 NNNNNpppp
0 NNNNNpppp
9 NNNNNpppp
8 NNNpNpppp
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSnSnnnn
3 SSSSSnnnn
2 SnSSSnnnn
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2         G
1         G
0       G G
9       G G
8       G G
7       G G
6       GGG
5       G G
4       G G
3         G
2         G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +    +
2 &+    +
1  +    +C
0  +CcCCCC
9  CC  C C
8  c oOC
7  C  OC
6  cOOOcII
5     OCCC
4   -oO  C
3   - O -C
2  _-  _-
1   -   -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | X | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS3 |   |   | X |
| NMOS4 | X |   |   |
| PMOS1 | X |   |   |
| PMOS3 |   | X |   |
| PMOS4 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 |   |
| NMOS3 | O |
| NMOS4 |   |
| PMOS1 |   |
| PMOS2 | O |
| PMOS3 |   |
| PMOS4 |   |
