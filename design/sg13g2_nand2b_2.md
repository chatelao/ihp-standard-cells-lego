# Design Documentation for sg13g2_nand2b_2

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
2  pppXpppXpppX
1  pppXpXpXpXpX
0  pppXpXpXpXpX
9     X X   X X
8     X XXXXX X
7
6  X      X
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2  nnnnnXnnnnnn
1  nnnnnXnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
3
2 G G X  GXG  X
1 G G X XGXGX X
0 G G X XGXGX X
9 G G X XG GX X
8 G G X XXXXX X
7 G G    G G
6 GXG    GXG
5 G G    G G
4 G G    G G
3 G G    G G
2 G G   XG G
1 G G   XG G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123
3 ++++++++++++++
2 +   x   x   x
1 +   x x x x x
0 + C x x x x x
9 + C x x   x x
8 + CCx xxxxx x
7    C      O
6  x CC   xIO
5  I C      O
4 - CCCCCCC O
3 -   C   C   C
2 -   C x CCCCC
1 -     x
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
