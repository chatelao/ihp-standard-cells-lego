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
1  pppppppppppppppppppppppppppppppX
0
9
8
7    X X
6                        X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnX
4  nnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnX
3  nnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnX
2  nnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnX
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
4
3    G G                 G
2    G G                 G
1    G G                 G        X
0    G G                 G
9    G G                 G
8    G G                 G
7    X X                 G
6    G G                 X
5    G G                 G   X    X
4    G G                 G  XX    X
3    G G                 G  X     X
2    G G                 G  X     X
1    G G                 G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++
3
2              CCCC
1  C   CCCC    C  C               x
0  C   C  CCCC CC C     C   O C   O
9  CCCCCCCCCCC CC C     C   O C   O
8  C     C  CC CC C CCCCC   O C   O
7  C x x CC CC CCCCCC  CCCCCOOC   O
6  C I I CCCCC C   CCC C x C OCCCCO
5  C     CCCCCCC CCCCC C I   xC   x
4  C    CCCCCCCCCCCC  CC    xxC   x
3  C    CCC        C  CC    x C   x
2       CCC     CCCC  CC    x     x
1
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
