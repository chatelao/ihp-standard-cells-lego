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
4
3
2  pp
1  pp
0  pp
9  pp
8  pp
7
6
5
4  nn
3  nn
2  nn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

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
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
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
Legend: M=Metal 2
