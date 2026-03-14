# Design Documentation for sg13g2_nand3b_1

## Substrate
```
  012345678901
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
3
2  pppXpppXpp
1  pppXpXpXpX
0  pppXpXpXpX
9     X X   X
8     X XXXXX
7
6    X X X
5  nnnnnnnnnn
4  nnnnnnnnnn
3  nnnnnnnnnX
2  nnnXnnnnnX
1  nnnXnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
3
2    GXG GX
1    GXGXGX X
0    GXGXGX X
9    GXGXG  X
8    GXGXXXXX
7    G G G
6    X X X
5    G G G
4    G G G
3    G G G  X
2    GXG G  X
1    GXG G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901
3 ++++++++++++
2     x   x
1     x x x xO
0   C x x x xO
9   C x x   xO
8   C x xxxxxO
7   C        O
6   Cx x x C O
5   CI I I C O
4   CCCCCCCCOO
3           xO
2     x     xO
1     x
0 ------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901
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
