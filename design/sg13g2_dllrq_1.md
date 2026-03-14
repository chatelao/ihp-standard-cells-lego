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
1  pppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567
4
3    G G                 G
2    G G                 G
1    G G                 G
0    G G                 G
9    G G                 G
8    G G                 G
7    G G                 G
6    G G                 G
5    G G                 G
4    G G                 G
3    G G                 G
2    G G                 G
1    G G                 G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 ++++++++++++++++++++++++++++
3     x     x       xxx   x
2     x     x       xxx   x
1     x             xxx C x xO
0  CC + CCCCCCCCCCC +++ C + OO
9  CC + CC     CC C CCCCCCCCOO
8  CC + CCCCCCCCC C CCCC   COO
7  C x x C C  CCCCCCCC C I C O
6  C I I C CCCCC     CCC x C O
5  CC    C CCCCCCCC  C C I   O
4  CC   CCCCCC   CCCCC C  x xO
3  CCCCCCCCCCC   C     C  x xO
2                    x C  x xO
1     x     xxx      x    x
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
