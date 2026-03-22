# Design Documentation for sg13g2_nor2b_2

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
2 pppppNNppppp
1 ppppNNNppppp
0 ppppNNNppppp
9 ppppNNNppppp
8 ppppNpNppppp
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 nnnnSnSnnnnn
3 nnnnSSSnnnnn
2 nnnnSSSnnnnn
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2 G G     G G
1 G G     G G
0 G G     G G
9 G G     G G
8 G G     G G
7 G G     G G
6 G G     GGG
5 G G     G G
4 G G     G G
3 GGG     G G
2 G G     G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +       +
2    +&c     +
1  C + CCCCC +
0  C + c   C +
9  C +   O C +
8  C   oOo
7  CCC O  III
6  c c O  iIi
5  C   OOOOO
4    _ o o O _
3  I - O - O -
2  I _   _   _
1    -   -   -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   | X |   | X |
| NMOS4 |   | X |   |   |
| PMOS1 |   |   | X |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   | O |
| NMOS4 |   |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
| PMOS3 |   | O |
| PMOS4 |   |   |
