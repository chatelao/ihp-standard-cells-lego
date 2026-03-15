# Design Documentation for sg13g2_fill_1

## Substrate
```
  01
4 NN
3 NN
2 NN
1 NN
0 NN
9 NN
8 NN
7 SS
6 SS
5 SS
4 SS
3 SS
2 SS
1 SS
0 SS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01
4 NN
3 NN
2 pN
1 pN
0 pN
9 pN
8 pN
7 SS
6 SS
5 SS
4 nS
3 nS
2 nS
1 SS
0 SS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01
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
  01
4 &+
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
0 -_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  01
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
