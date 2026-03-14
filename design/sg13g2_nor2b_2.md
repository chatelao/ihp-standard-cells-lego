# Design Documentation for sg13g2_nor2b_2

## Substrate
```
  0123456789012
5 NNNNNNNNNNNNN
4 NNNNNNNNNNNNN
3 NNNNNNNNNNNNN
2 NNNNNNNNNNNNN
1 NNNNNNNNNNNNN
0 NNNNNNNNNNNNN
9 NNNNNNNNNNNNN
8 NNNNNNNNNNNNN
7 SSSSSSSSSSSSS
6 SSSSSSSSSSSSS
5 SSSSSSSSSSSSS
4 SSSSSSSSSSSSS
3 SSSSSSSSSSSSS
2 SSSSSSSSSSSSS
1 SSSSSSSSSSSSS
0 SSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012
5
4  ppppppppppp
3  ppppppppppp
2  ppppppppppp
1
0
9
8
7           X
6
5  nnnnXXXXXnn
4  nnnnXnnnXnn
3  XnnnXnnnXnn
2  nnnnnnnnnnn
1  nnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012
5
4 G G      G G
3 G G      G G
2 G G      G G
1 G G      G G
0 G G      G G
9 G G      G G
8 G G      G G
7 G G      GXG
6 G G      GGG
5 G G  XXXXX G
4 G G  X   X G
3 GXG  X   X G
2 GGG      G G
1 G G      G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012
5 +++++++++++++
4
3
2      CCCCC
1  C   C   C
0  C   C O C
9  C     O C
8  C   OOO
7  CCCCO   IxI
6  C   O   III
5  C   xxxxx
4      x   x
3  x   x   x
2  I
1
0 -------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012
5
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
