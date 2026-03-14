# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
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
3
2  ppXppppppXppppppppXXpppXpppppXpp
1  ppXpppppppppppppppXXpppXpppppXpX
0  ppppppppppppppppppXXpppXpXpppXpX
9                         X X   X X
8                           X   X X
7    X X
6                        X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnXnnnnnnnnnnnnnnXnnnnXnXnnnXnX
2  nnnXnnnnnXnnnnnnnnXnnnnXnXnnnXnX
1  nnnXnnnnnXnnnnnnnnXnnnnXnnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
3
2    X G    X        XX  GX     X
1    X G             XX  GX     X X
0    G G             XX  GX X   X X
9    G G                 GX X   X X
8    G G                 G  X   X X
7    X X                 G
6    G G                 X
5    G G                 G
4    G G                 G
3    GXG             X   GX X   X X
2    GXG    X        X   GX X   X X
1    GXG    X        X   GX     X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123
3 ++++++++++++++++++++++++++++++++++
2    x      x  CCCC  xx   x     x
1  C x CCCC    C  C  xx   x     x x
0  C   C  CCCC CC C  xx C x x C x x
9  CCCCCCCCCCC CC C     C x x C x x
8  C     C  CC CC C CCCCC   x C x x
7  C x x CC CC CCCCCC  CCCCCOOC   O
6  C I I CCCCC C   CCC C x C OCCCCO
5  C     CCCCCCC CCCCC C I   OC   O
4  C  - CCCCCCCCCCCC  CC    OOC   O
3  C  x CCC        C xCC  x x C x x
2     x CCC x   CCCC xCC  x x   x x
1     x     x        x    x     x
0 ----------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123
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
