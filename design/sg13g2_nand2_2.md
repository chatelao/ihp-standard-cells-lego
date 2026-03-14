# Design Documentation for sg13g2_nand2_2

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
2  XpppXpppX
1  XpXpXpXpX
0  XpXpppXpX
9  X XXXXX X
8  X   X   X
7        X
6    X   X
5  nnnnnnnnn
4  nnnnnnnnn
3  nnnnnnnnn
2  nnXnnnnnn
1  nnXnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
3
2  XG GXG GX
1  XGXGXGXGX
0  XGXG GXGX
9  XGXXXXXGX
8  XG GXG GX
7   G G GXG
6   GXG GXG
5   G G G G
4   G G G G
3   G G G G
2   GXG G G
1   GXG G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
3 +++++++++++
2  x   x   x
1  x x x x x
0  x x   x x
9  x xxxxx x
8  x   x I x
7      O x
6    x O x
5    I OOO
4  CCCCC O
3  C   C   C
2  C x CCCCC
1    x
0 -----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
