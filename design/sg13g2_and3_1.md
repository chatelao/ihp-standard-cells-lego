# Design Documentation for sg13g2_and3_1

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
2  ppXpppXXpp
1  ppXpppXXpX
0  ppXpppXXpX
9           X
8           X
7
6     X  X
5  nnnnnnnnnn
4  nnnnnnnnnn
3  nnnnXnXnXn
2  nnXnnnXnnn
1  nnnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
3
2    XGG XX
1    XGG XX X
0    XGG XX X
9     GG G  X
8     GG G  X
7     GG G
6     XG X
5     GG G
4     GG G
3     GX X X
2    XGG X
1     GG X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901
3 ++++++++++++
2    x   xx
1   Cx C xx xO
0   Cx C xx xO
9   C  C    xO
8   CCCCCCC xO
7   C     C  O
6   C xI xCC O
5   C II I   O
4   C      OOO
3      x x x
2  IIxII x
1        x
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
