# Design Documentation for sg13g2_and3_2

## Substrate
```
  012345678901
4 SSSSSSSSSSSS
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 NNNNNNNNNNNN
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 NNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3
2        ppppp
1  ppppppppppp
0  ppppppppppp
9  ppppppppppp
8
7
6
5  nnnnnnnnnnn
4  nnnnnnnnnnn
3  nnnnnnnnnnn
2
1
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3
2       G G G
1       G G G
0       G G G
9       G G G
8       G G G
7     G GGGGG
6       G G G
5       G G G
4       G G G
3       G G G
2  GGG    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +   +   +
2  c & c &  c+
1  C + C + O +
0  c & c & Oc
9  C   C    O
8  C      c O
7  C  IIIIC O
6  C  IiIi  O
5  C       OO
4  c   I _ Oc-
3      I - O -
2  iIiII -   -
1        -   -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Internal1 | Internal2 | Internal3 | Output1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   | X |   |   |   |
| PMOS1 | X |   |   | X |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |
| Poly2 | X | X |   |   | X |   | X |
| Poly3 |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | S | O |   |
| PMOS1 |   | O |   |
| PMOS2 |   |   |   |
