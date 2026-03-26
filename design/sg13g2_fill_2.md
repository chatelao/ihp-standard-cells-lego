# Design Documentation for sg13g2_fill_2

## Substrate
```
  0123
4 NNNN
3 NNNN
2 NNNN
1 NNNN
0 NNNN
9 NNNN
8 NNNN
7 SSSS
6 SSSS
5 SSSS
4 SSSS
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
3 NNNN
2 NppN
1 NppN
0 NppN
9 NppN
8 NppN
7 SSSS
6 SSSS
5 SSSS
4 SnnS
3 SnnS
2 SnnS
1 SSSS
0 nnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123
4
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
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123
4 &+&+
3 ++++
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
0 c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 |
| --- | --- | --- | --- |
| NMOS1 |   | X | X |
| PMOS2 | X |   |   |
