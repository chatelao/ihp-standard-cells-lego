# Design Documentation for sg13g2_nor4_1

## Substrate
```
  01234567890
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
3
2  Xpppppppp
1  XppppppXX
0  XppppppXX
9  X     XXX
8  X   X  XX
7      X X
6  X X    X
5  nnnXXnnnn
4  nnnnnnnnn
3  XnXnnnXnn
2  XnXnXnXnX
1  XnnnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
3
2  X  GG  G
1  X  GG  XX
0  X  GG  XX
9  X  GG XXX
8  X  GX  XX
7  G  GX XG
6  X XGG  X
5  G  XX  G
4  G  GG  G
3  X XGG XG
2  X XGX XGX
1  X  GX  GX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
3 +++++++++++
2  x
1  x      xx
0  x      xx
9  x     xxx
8  x   x Ixx
7      x x O
6  x x I IxO
5  I Ixx IIO
4    OOOOOOO
3  x x   x
2  x x x x x
1  x   x   x
0 -----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890
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
