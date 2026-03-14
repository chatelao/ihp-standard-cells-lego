# Design Documentation for sg13g2_nor2b_2

## Substrate
```
  012345678901
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
3
2  ppXppppppp
1  ppXppppppp
0  ppXppppppp
9    X   X
8    X XXX
7
6          X
5  nnnnnnnnnn
4  nnnnnnnnnn
3  XnXnXnXnXn
2  nnXnnnXnnn
1  nnXnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
3
2 G GX    G G
1 G GX    G G
0 G GX    G G
9 G GX   XG G
8 G GX XXXG G
7 G G     G G
6 G G     GXG
5 G G     G G
4 G G     G G
3 GXGX X XGXG
2 GGGX   XG G
1 G GX   XG G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901
3 ++++++++++++
2    x       +
1    x CCCCC +
0  C x C   C +
9  C x   x C +
8  C x xxx C +
7  C   O
6  CCC O  IxI
5  C   O
4  C - OOOOO -
3  x x x x x -
2  I x   x   -
1    x   x   -
0 ------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901
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
