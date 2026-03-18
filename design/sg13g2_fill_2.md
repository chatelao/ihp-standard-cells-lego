# Design Documentation for sg13g2_fill_2

## Substrate
```
  0123
4 NNNN
3 SSSS
2 SSSS
1  NN
0  NN
9
8
7
6  SS
5  SS
4  SS
3  SS
2
1
0
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
7 S  S
6 SSSS
5 S  S
4 S  S
3 SnnS
2 S  S
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
0 -_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

