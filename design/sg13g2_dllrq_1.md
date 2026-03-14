# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4
3  pppppppppppppppppppppppppp
2  pppppppppppppppppppppppppp
1  pppppppppppppppppppppppppX
0
9
8
7
6    X X                 X
5  nnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnX
2  nnnnnnnnnnnnnnnnnnnnnnnnnX
1  nnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567
4
3    G G                 G
2    G G                 G
1    G G                 G  X
0    G G                 G
9    G G                 G
8    G G                 G
7    G G                 G
6    X X                 X
5    G G                 G
4    G G                 G
3    G G                 G  X
2    G G                 G  X
1    G G                 G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567
4 ++++++++++++++++++++++++++++
3
2
1                           xO
0  CC   CCCCCCCCCCC     C   OO
9  CC   CC        C     C   OO
8  CC   CCCC   CC C CCCCCCCCOO
7  C     C CCCCCCCCCCC C   C O
6  C x x C C  CC     C C x C O
5  C     C CCCCCCCC  CCC I C O
4  CC   CCCCCC       C C     O
3  CC       CC   CCCCC C    xO
2  CCCCCCCCCCC   C     C    xO
1
0 ----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567
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
