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
6 SSSS
5 SSSS
4 SSSS
3 SSSS
2 SSSS
1 SSSS
0 NNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123
4 pppp
3
2
1
0
9
8
7
6
5
4
3  nn
2  nn
1  nn
0 nnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123
4
3
2
1
0  GG
9  GG
8  GG
7  GG
6  GG
5  GG
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123
4 &+&+
3
2
1
0
9
8
7
6
5
4
3
2
1
0 _-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| PMOS1 | X |   |
| Poly1 |   |   |
