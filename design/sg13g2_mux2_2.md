# Design Documentation for sg13g2_mux2_2

## Substrate
```
  012345678901234567890
5 NNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
5
4  ppppppppppppppppppp
3  ppppppppppppppppppp
2  pppppppppppppppXXXp
1
0
9
8
7    X
6       X  X
5  nnnnnnXnnnXnnnnnnXn
4  nnnnnnnnXnnnnnnnXXn
3  nnnnnnnnnnnnnnnnXXn
2  nnnnnnnnnnnnnnnnXXn
1  nnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890
5
4   G G   G G G
3   G G   G G G
2   G G   G G G   XXX
1   G G   G G G
0   G G   G G G
9   G G   G G G
8   G G   G G G
7   GXG   G G G
6   G G X GXG G
5   G G  XG GXG     X
4   G G   GXG G    XX
3   G G   G G G    XX
2   G G   G G G    XX
1   G G   G G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890
5 +++++++++++++++++++++
4
3
2       CCCCCCCC  xxx
1       C  C   C  OOO
0  CCCCCC  C   C  OOO
9  C     CCC   C  OOO
8  C   CCC     C  OOO
7  C x C       C    O
6  C I CxI x I CC C O
5  C   C x   x    C x
4  C   C IIxII CCCCxx
3      C       C   xx
2      CCCCCCCCC   xx
1
0 ---------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890
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
