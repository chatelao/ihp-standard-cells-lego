# Design Documentation for sg13g2_nor4_2

## Substrate
```
  01234567890123456789012
5 NNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
5
4  ppppppppppppppppppppp
3  ppppppppppppppppppppp
2  ppppppppppppppppppppp
1
0
9
8
7
6    X     X   X  X
5  nnXXXXXXXXXXXXXXXXXnn
4  nnXnnnnnXnnnXnnnnnXnn
3  nnXnnnnnXnnnXnnnnnXnn
2  nnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
5
4   G G   G G G GG G
3   G G   G G G GG G
2   G G   G G G GG G
1   G G   G G G GG G
0   G G   G G G GG G
9   G G   G G G GG G
8   G G   G G G GG G
7   G G   G G G GG G
6   GXG   GXG GXGGXG
5   GXXXXXXXXXXXXXXXXX
4   GXG   GXG GXGG G X
3   GXG   GXG GXGG G X
2   G G   G G G GG G
1   G G   G G G GG G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012
5 +++++++++++++++++++++++
4
3
2    C   CCCCCCCCC CCCCC
1    C   C   C   C C   C
0    C   C C C C C C O C
9    CCCCCCC C CCCCC O C
8                    O C
7                    O
6   IxI   IxI IxI xI OOO
5    xxxxxxxxxxxxxxxxx
4    x     x   x     x
3    x     x   x     x
2
1
0 -----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012
5
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
