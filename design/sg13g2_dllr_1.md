# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4
3  pppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppp
1  pppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
4    G G                 G
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
0    G G                 G
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++
3    x      x        xx   x     x
2    x      x  CCCC  xx   x     x
1  C x CCCCCCC C  C  xx C x x   x x
0  C   CCCCC C CC C     C + O C + O
9  CCCCCCC  CC CC C CCCCC   O C + O
8  C     CC CC CC      CCCCCOOC + O
7  C x x CC CC CCCCCC  C   C OC   O
6  C I I CCCCCCC CCCCC C x C OCCCCO
5  C     CC      CCC   C     xC   x
4  C  x CCCCCCCCCCCC xCC  x x C x x
3     x CCC x   CCCC xCC  x x C x x
2     x     x        x    x x   x x
1     x     x        x    x     x
0 ----------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123
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
