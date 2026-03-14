# Design Documentation for sg13g2_dlhrq_1

## Substrate
```
  01234567890123456789012345678
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678
5
4  ppppppppppppppppppppppppppp
3  ppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppXX
1
0
9
8
7  X   X                 X
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnX
4  nnnnnnnnnnnnnnnnnnnnnnnnnnX
3  nnnnnnnnnnnnnnnnnnnnnnnnXXX
2  nnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678
5
4  G   G                 G
3  G   G                 G
2  G   G                 G  XX
1  G   G                 G
0  G   G                 G
9  G   G                 G
8  G   G                 G
7  X   X                 X
6  G   G                 G
5  G   G                 G   X
4  G   G                 G   X
3  G   G                 G XXX
2  G   G                 G
1  G   G                 G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678
5 +++++++++++++++++++++++++++++
4
3             CCCCC
2             C   C     C   xx
1  C          C C C     C   OO
0  CCCCCCCCCCCC C C     C   OO
9  CCC  CCCC CC C C CCCCC   OO
8    C   C C C CCCCCCCCC    OO
7  x C x C C C C C    CC x   O
6  I C I C C   C CC    C I C O
5    C   CCCCCCC CC   CCCCCC x
4  CCC  CCCCCCC  CC   C      x
3       C     C CCC   C    xxx
2       C     CCCCC
1
0 -----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678
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
