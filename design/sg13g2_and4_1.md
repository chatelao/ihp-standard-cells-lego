# Design Documentation for sg13g2_and4_1

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
2  pXppXpppXppp
1  pXppXpppXppX
0  pXppXpppXppX
9             X
8             X
7
6    X X X X
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnXnnX
2  nnnnnnnnXnnX
1  nnnnnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
3
2   XG X G X
1   XG X G X  X
0   XG X G X  X
9    G G G G  X
8    G G G G  X
7    G G G G
6    X X X X
5    G G G G
4    G G G G
3    G G G X  X
2    G G G X  X
1    G G G X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123
3 ++++++++++++++
2   x  x   x
1   xC x C x  xO
0   xC x C x  xO
9    C   C    xO
8  CCCCCCCCCCCxO
7  C         C O
6  C x x x x C O
5  C I I I I   O
4  C           O
3  CC      x  xO
2  CC      x  xO
1          x
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
