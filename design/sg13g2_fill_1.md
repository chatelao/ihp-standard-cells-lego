# Design Documentation for sg13g2_fill_1

## Substrate
```
  01
4 SS
3 NN
2 NN
1 NN
0 NN
9 NN
8 NN
7 NN
6 NN
5 NN
4 NN
3 NN
2 NN
1 SS
0 SS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01
4 pp
3 pp
2 pp
1 pp
0 pp
9 pp
8 pp
7 pp
6 pp
5 pp
4 pp
3 pp
2 pp
1 nS
0 nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01
4
3
2
1
0  G
9  G
8  G
7  G
6  G
5  G
4  G
3  G
2  G
1  G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01
4 &&
3 ++
2 ++
1 ++
0 ++
9 ++
8 ++
7 ++
6 ++
5 ++
4 ++
3 ++
2 ++
1
0 _c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| PMOS1 | X |   |
| Poly1 |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | NE |
| PMOS1 | O |
