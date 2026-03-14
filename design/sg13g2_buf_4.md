# Design Documentation for sg13g2_buf_4

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
2  XpppXppXpppX
1  XpXpXpXXpppX
0  XpXpXpXXpppX
9  X X X XX
8  X X   XX
7
6           X
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  XnXnnnXnnnnn
2  XnXnXnXnXXnn
1  XnnnXnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
3
2  X   X  X G X
1  X X X XX G X
0  X X X XX G X
9  X X X XX G
8  X X   XX G
7           G
6           X
5           G
4           G
3  X X   X  G
2  X X X X XX
1  X   X   XG
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123
3 ++++++++++++++
2  x   x  x   x
1  x x x xx   x
0  x x x xx   x
9  x x x xx C
8  x x   xx CCCC
7    OOOOO     C
6  OOO  CCC xI C
5    O    C II C
4    OOOOOCCCCCC
3  x x   x    CC
2  x x x x xx CC
1  x   x   x
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
