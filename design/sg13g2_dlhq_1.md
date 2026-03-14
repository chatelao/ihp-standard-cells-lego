# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  01234567890123456789012345678901
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
5
4  pppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppp
1
0
9
8
7   X                       X
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnX
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnX
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnX
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnX
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901
5
4   G                       G
3   G                       G
2   G                       G
1   G                       G
0   G                       G
9   G                       G
8   G                       G
7   X                       X
6   G                       G
5   G                       G   X
4   G                       G   X
3   G                       G   X
2   G                       G   X
1   G                       G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901
5 ++++++++++++++++++++++++++++++++
4
3
2      C   CCC CCCC
1    CCCCCCC   C CCCCCCCCCCCC   O
0    CCC   CCCCC C        CCC   O
9     CC   C CCC CCCCCCCC CCC   O
8     C      C CCCC CC  C CC    O
7  Ix C      CCC  C  C  C CCx   O
6  II C CCCC C   CC  C  C CCI CCO
5     C C  C CCCCCCC C  C  C  C x
4     C C  CCC     C C  CC C  C x
3    CC C    CCCCC   C     CCCC x
2           CCCCCCCCCCCCCCCC    x
1
0 --------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901
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
