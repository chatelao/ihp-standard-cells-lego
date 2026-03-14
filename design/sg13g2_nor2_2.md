# Design Documentation for sg13g2_nor2_2

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
2  ppXpppppp
1  ppXpppppp
0  ppXpppppp
9        X
8        XXX
7
6    X   X
5  nnnnnnnnn
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
2   GXG G G
1   GXG G G
0   GXG G G
9   G G GXG
8   G G GXXX
7   G G G G
6   GXG GXG
5   G G G G
4   G G G G
3  XGXG GXG
2  XGXGXGXGX
1  XG GXG GX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
3 +++++++++++
2    x
1  C x CCCCC
0  C x C   C
9  C   C x
8  CCCCC xxx
7          O
6    x   x O
5          O
4    OOOOOOO
3  x x   x
2  x x x x x
1  x   x   x
0 -----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

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
