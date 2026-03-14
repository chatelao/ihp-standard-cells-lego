# Design Documentation for sg13g2_nand2b_2

## Substrate
```
  012345678901234
5 NNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234
5
4  ppppppppppppp
3  ppppppppppppp
2  ppppppXpppXpp
1
0
9
8
7
6  X       X
5  nnnnnnnnnnXnn
4  nnnnnnnnnnXnn
3  nnnnnnnnnnnnn
2  nnnnnnnnnnnnn
1  nnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234
5
4 G G     G G
3 G G     G G
2 G G    XG GX
1 G G     G G
0 G G     G G
9 G G     G G
8 G G     G G
7 G G     G G
6 GXG     GXG
5 G G     G GX
4 G G     G GX
3 G G     G G
2 G G     G G
1 G G     G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234
5 +++++++++++++++
4
3
2        x   x
1        O   O
0    C   O   O
9    C   OOOOO
8    C       O
7    C       O
6  x CCC   x O
5    C       x
4    C CCCCC x C
3      C   C   C
2      C   CCCCC
1
0 ---------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234
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
