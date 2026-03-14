# Design Documentation for sg13g2_nor4_1

## Substrate
```
  01234567890
4 NNNNNNNNNNN
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
4
3  ppppppppp
2  ppppppppp
1  pppppppXX
0
9        X
8      X
7      X X
6  X X    X
5  nnnXXnnnX
4  nnXXXXXXX
3  nnXnnnXnn
2  nnXnnnXnn
1  nnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
4
3  G  GG  G
2  G  GG  G
1  G  GG  XX
0  G  GG  G
9  G  GG XG
8  G  GX  G
7  G  GX XG
6  X XGG  X
5  G  XX  GX
4  G XXXXXXX
3  G XGG XG
2  G XGG XG
1  G  GG  G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
4 +++++++++++
3
2
1         xx
0         OO
9        xOO
8      x IOO
7      x x O
6  x x I IxO
5  I Ixx IIx
4    xxxxxxx
3    x   x
2    x   x
1
0 -----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890
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
