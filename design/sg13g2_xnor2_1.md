# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
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
4
3  pppppppppppp
2  pppppppppppp
1  pppppppppXpp
0
9
8       X
7      X   X
6      XX  X
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnnnnX
2  nnnnnnnnnnnX
1  nnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
4
3       G  G
2       G  G
1       G  GX
0       G  G
9       G  G
8       X  G
7      XG  X
6      XX  X
5       G  G
4       G  G
3       G  G  X
2       G  G  X
1       G  G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123
4 ++++++++++++++
3
2
1           x
0     C     O
9    CC     O
8    C IxII OOO
7    C x   x   O
6    C xxI x C O
5    C       C O
4    CCCCCCCCC O
3    CC CCCCC xO
2             xO
1
0 --------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123
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
