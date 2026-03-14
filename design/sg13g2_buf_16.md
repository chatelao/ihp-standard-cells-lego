# Design Documentation for sg13g2_buf_16

## Substrate
```
  01234567890123456789012345678901234567890123
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
3
2  XpppXppXXppXpppXpppXpppXppXpppXpppXpppXppX
1  XpXpXpXXXXpXpXpXpXpXpXpXpXXpXpXpppXpppXppX
0  XpXpXpXXXXpXpXpXpXpXpXpXpXXpXpXpppXpppXppX
9  X X X XXXX X X X X X X X XX X X   X   X  X
8  X XXXXXXXXXXXXXXXXXXXXXXXXXXX            X
7
6                                         X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  XnXnXnXXXXnXnXnXnXnXnXnnnXnnXnnnnnnnnnnnnX
2  XnXnXnXXXXnXnXnXnXnXnXnXnXXnXnXnnnXnnnXnnX
1  XnnnXnnXXnnXnnnXnnnXnnnXnnXnnnXnnnXnnnXnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123
3
2  X   X  XX  X   X   X   X  X   X   X   XG X
1  X X X XXXX X X X X X X X XX X X   X   XG X
0  X X X XXXX X X X X X X X XX X X   X   XG X
9  X X X XXXX X X X X X X X XX X X   X   XG X
8  X XXXXXXXXXXXXXXXXXXXXXXXXXXX          G X
7                                         G
6                                         X
5                                         G
4                                         G
3  X X X XXXX X X X X X X   X  X          G X
2  X X X XXXX X X X X X X X XX X X   X   XG X
1  X   X  XX  X   X   X   X  X   X   X   XG X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123
3 ++++++++++++++++++++++++++++++++++++++++++++
2  x   x  xx  x   x   x   x  x   x   x   x  x+
1  x x x xxxx x x x x x x x xx x x C x C x Cx+
0  x x x xxxx x x x x x x x xx x x C x C x Cx+
9  x x x xxxx x x x x x x x xx x x C x C x Cx+
8  x xxxxxxxxxxxxxxxxxxxxxxxxxxx CCCCCCCCCCCx+
7    O   O  O   O   O   O        C
6    O   OOOO   O   O   O CCCCCCCC      IIxI
5    O   O  O   O   O   O        C
4    O   O  O   O   O   OOOOOOOO CCCCCCCCCCC
3  x x x xxxx x x x x x x   x  x   C   C   Cx-
2  x x x xxxx x x x x x x x xx x x C x C x Cx-
1  x   x  xx  x   x   x   x  x   x   x   x  x-
0 --------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123
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
