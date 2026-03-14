# Design Documentation for sg13g2_xor2_1

## Substrate
```
  01234567890123
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
3
2  pXppppppXppp
1  pXppppppXppp
0  pXpppppppppp
9   X
8   X
7
6   X     X
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  XXnnnnXnnXXn
2  XXnnnnXnnXXX
1  XXnnnnXnnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
3
2   X     GX
1   X     GX
0   X     G
9   X     G
8   X     G
7   G     G
6   X     X
5   G     G
4   G     G
3  XX    XG XX
2  XX    XG XXX
1  XX    XG   X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123
3 ++++++++++++++
2   x      x
1   x  C C x C O
0   x  C C   C O
9   x  C CCCCC O
8   x CCCCCCCCCO
7     C       CO
6  Ix C IIxII CO
5     C        O
4     C  -  OOOO
3  xx C  x  xx
2  xx    x  xxx
1  xx    x    x
0 --------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123
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
