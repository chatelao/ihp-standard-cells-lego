# Design Documentation for sg13g2_nor3_1

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
2  Xpppppp
1  XpppppX
0  XpppppX
9  X  XXXX
8  X  X  X
7
6  X   X X
5  nnnnnnn
4  nnnnnnn
3  XnnXnnX
2  XnnXXnX
1  XnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
3
2  X   G G
1  X   G X
0  X   G X
9  X  XXXX
8  X  XG X
7  G   G G
6  X   X X
5  G   G G
4  G   G G
3  X  XG X
2  X  XX X
1  X   X G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678
3 +++++++++
2  x
1  x     x
0  x     x
9  x  xxxx
8  x  x  x
7     O
6  x  Ox x
5     O
4     OOOO
3  x  x  x
2  x  xx x
1  x   x
0 ---------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

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
