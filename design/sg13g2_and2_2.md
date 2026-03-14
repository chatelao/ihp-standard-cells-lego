# Design Documentation for sg13g2_and2_2

## Substrate
```
  01234567890
4 NNNNNNNNNNN
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
4
3  ppppppppp
2  ppppppppp
1  ppppppXpp
0
9
8
7
6    X
5  nnnnnnXnn
4  nnnnnnXnn
3  XnnnnnXnn
2  nnnnnnnnn
1  nnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
4
3 G G G
2 G G G
1 G G G  X
0 G G G
9 G G G
8 G G G
7 G G G
6 G GXG
5 G G G  X
4 G G G  X
3 GXG G  X
2 GGG G
1 G G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
4 +++++++++++
3
2
1    C   x
0    C   O
9    C   O
8  CCCCC O
7  C   C O
6  C x C O
5  C I   x
4  C     x
3 IxI    x
2 III
1
0 -----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890
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
