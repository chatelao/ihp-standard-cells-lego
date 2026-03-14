# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
3
2  XppppXpppppX
1  XppppXpppXpX
0  XppppXpppXpX
9  X        X
8       X   XXX
7      X   X
6      XX  X
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  XnnnnnnnnnnX
2  XnnnnnnnnnnX
1  XnnnnnnXnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
3
2  X    X  G  X
1  X    X  GX X
0  X    X  GX X
9  X    G  GX
8       X  GXXX
7      XG  X
6      XX  X
5       G  G
4       G  G
3  X    G  G  X
2  X    G  G  X
1  X    G XG
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123
3 ++++++++++++++
2  x    x     x
1  x    x   x x
0  x  C x   x x
9  x CC     x
8    C IxII xxx
7    C x   x   O
6    C xxI x C O
5    C       C O
4  - CCCCCCCCC O
3  x CC CCCCC xO
2  x          xO
1  x      x
0 --------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123
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
