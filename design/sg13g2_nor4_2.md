# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNN
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
4
3  ppppppppppppppppppp
2  ppppppppppppppppppp
1  ppppppppppppppppppp
0
9
8
7
6   X     X   X   X
5  nnnnnnnnnnnnnnnnnXn
4  nnXXXXXXXXXXXXXXXXn
3  nnXnnnnXnnnXnnnnnXn
2  nnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890
4
3  G G   G G G G G G
2  G G   G G G G G G
1  G G   G G G G G G
0  G G   G G G G G G
9  G G   G G G G G G
8  G G   G G G G G G
7  G G   G G G G G G
6  GXG   GXG GXG GXG
5  G G   G G G G G GX
4  G XXXXXXXXXXXXXXXX
3  G X   GXG GXG G GX
2  G G   G G G G G G
1  G G   G G G G G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890
4 +++++++++++++++++++++
3
2
1    C   CCCCCCCC CCCCC
0    C   C  C   C C   C
9    C    C C C   C O C
8    CCCCCC C CCCCC O C
7                   O
6   xI    xI  xI Ix OO
5                   x
4    xxxxxxxxxxxxxxxx
3    x    x   x     x
2
1
0 ---------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890
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
