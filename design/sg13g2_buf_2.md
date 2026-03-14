# Design Documentation for sg13g2_buf_2

## Substrate
```
  012345678
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
3
2  XppppXp
1  XppppXp
0  Xpppppp
9
8     X
7
6       X
5  nnnnnnn
4  nnnnnnn
3  nXnXnXn
2  nXnXnXn
1  nXnnnXn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
3
2  X   GXG
1  X   GXG
0  X   G G
9      G G
8     XG G
7      G G
6      GXG
5      G G
4      G G
3   X XGXG
2   X XGXG
1   X  GXG
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678
3 +++++++++
2  x    x
1  x    xC
0  x     C
9   CCCCCC
8  CC xC C
7  C  OC
6  COOOCxI
5     OC
4   - OCCC
3   x x xC
2   x x x
1   x   x
0 ---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678
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
