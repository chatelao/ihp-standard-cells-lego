# Design Documentation for sg13g2_nor3_2

## Substrate
```
  0123456789012345
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
3
2  XpppXppppppppp
1  XpppXppppppppp
0  XpppXppppppppp
9  X          X
8  X        XXX
7
6   XX  XX    X
5  nnnnnnnnnnnnnn
4  nnnnnnnnnnnnnn
3  XnXnXXXXnXnXnX
2  XnnnXXXnnXnnnX
1  XnnnXXXnnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
3
2  X G X G   G G
1  X G X G   G G
0  X G X G   G G
9  X G G G   GXG
8  X G G G  XXXG
7  G G G G   G G
6  GXX GXX   GXG
5  G G G G   G G
4  G G G G   G G
3  X X XXXX XGXGX
2  X G XXX  XG GX
1  X G XXX  XG GX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345
3 ++++++++++++++++
2  x   x
1  x C x CCCCCCCC
0  x C x C  C   C
9  x C    C   x C
8  x CCCCCC xxx C
7           O
6   xx  xxOOO xI
5         O O
4  - OOOOOO OOO -
3  x x xxxx x x x
2  x   xxx  x   x
1  x   xxx  x   x
0 ----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345
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
