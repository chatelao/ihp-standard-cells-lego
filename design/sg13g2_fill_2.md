# Design Documentation for sg13g2_fill_2

## Substrate
```
  0123
4 SSSS
3 NNNN
2 NNNN
1 NNNN
0 NNNN
9 NNNN
8 NNNN
7 NNNN
6 NNNN
5 NNNN
4 NNNN
3 SSSS
2 SSSS
1 SSSS
0 SSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123
4 pppp
3 pppp
2 pppp
1 pppp
0 pppp
9 pppp
8 pppp
7 pppp
6 pppp
5 pppp
4 pppp
3 nSSS
2 SSSS
1 SSSS
0 nnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123
4
3
2
1
0  GGG
9  GGG
8  GGG
7  GGG
6  GGG
5  GGG
4  GGG
3  GGG
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123
4 &&&&
3 ++++
2 ++++
1 ++++
0 ++++
9 ++++
8 ++++
7 ++++
6 ++++
5 ++++
4 ++++
3
2
1
0 _c_c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| NMOS2 |   |   |
| PMOS1 | X |   |
| Poly1 |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | E |
| PMOS1 | O |
