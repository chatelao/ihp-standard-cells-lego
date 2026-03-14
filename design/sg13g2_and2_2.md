# Design Documentation for sg13g2_and2_2

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
2  XpppXppXp
1  XpppXpXXp
0  XpppXpXXp
9        XX
8        XX
7
6    X
5  nnnnnnnnn
4  nnnnnnnnn
3  XnnnXnXXn
2  nnnnXnnXn
1  nnnnXnnXn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
3
2 GXG GX  X
1 GXG GX XX
0 GXG GX XX
9 G G G  XX
8 G G G  XX
7 G G G
6 G GXG
5 G G G
4 G G G
3 GXG GX XX
2 GGG GX  X
1 G G GX  X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
3 +++++++++++
2  x   x  x
1  x C x xx
0  x C x xx
9    C   xx
8  CCCCC xx
7  C   C O
6  C x C O
5  C I   O
4  C     O-
3 IxI  x xx
2 III  x  x
1      x  x
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
