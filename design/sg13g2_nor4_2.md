# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
3
2  XpppXpppppppppppppp
1  XpppXpppppppppppppp
0  XpppXpppppppppppppp
9  X                X
8  X                X
7
6   X     X   X   X
5  nnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnn
3  XnXnXXXXnXnXnXXXnXn
2  XnnnXXXnnXnnnXXXnnn
1  XnnnXXXnnXnnnXXXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890
3
2  X G X G G G G G G
1  X G X G G G G G G
0  X G X G G G G G G
9  X G   G G G G G GX
8  X G   G G G G G GX
7  G G   G G G G G G
6  GXG   GXG GXG GXG
5  G G   G G G G G G
4  G G   G G G G G G
3  X X XXXXGXGXGXXXGX
2  X G XXX GXG GXXXG
1  X G XXX GXG GXXXG
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890
3 +++++++++++++++++++++
2  x   x
1  x C x CCCCCCCC CCCCC
0  x C x C  C   C C   C
9  x C    C C C   C x C
8  x CCCCCC C CCCCC x C
7                   O
6   xI    xI  xI Ix OO
5                   O
4  - OOOOOOOOOOOOOOOO -
3  x x xxxx x x xxx x -
2  x   xxx  x   xxx   -
1  x   xxx  x   xxx   -
0 ---------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890
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
