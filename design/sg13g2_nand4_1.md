# Design Documentation for sg13g2_nand4_1

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
2  XpppXpppX
1  XpXpXpXpX
0  XpXpXpXpX
9  X X   X
8  X XXXXXXX
7
6  X X X X
5  nnnnXnnnn
4  nnnnXnXnn
3  XnnnnnXnX
2  XnnnnnnnX
1  Xnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
3
2  X G X G X
1  X X X X X
0  X X X X X
9  X X G X
8  X XXXXXXX
7  G G G G
6  X X X X
5  G G X G
4  G G X X
3  X G G X X
2  X G G G X
1  X G G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
3 +++++++++++
2  x   x   x
1  x x x x x
0  x x x x x
9  x x   x
8  x xxxxxxx
7          O
6  x x x x O
5      x I O
4  -   x x O
3  x     x x
2  x       x
1  x
0 -----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
