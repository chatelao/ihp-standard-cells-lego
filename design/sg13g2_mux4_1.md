# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
3
2  pppXppppppppXppppppppXpppppppppppXp
1  pppXppppppppXppppppppXpppppppppppXp
0  pppXpppppppppppppppppppppppppppppXp
9     X
8     X
7
6    X X      X X       X         X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnXnnnnnnnnnnnXnX
2  nnnXnnnnnnnnXnnnnnnnXnnnnnnnnnnnXnX
1  nnnXnnnnnnnnXnnnnnnnXnnnnnnnnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456
3
2    GXG      GXG       X         G X
1    GXG      GXG       X         G X
0    GXG      G G       G         G X
9    GXG      G G       G         G
8    GXG      G G       G         G
7    G G      G G       G         G
6    X X      X X       X         X
5    G G      G G       G         G
4    G G      G G       G         G
3    G G      G G      XG         GX X
2    GXG      GXG      XG         GX X
1    GXG      GXG      XG         GX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123456
3 +++++++++++++++++++++++++++++++++++++
2     x        x CCCCCC x   CCCCCCC x
1     x        x C     Cx C C     C x
0  CC x   CC     C CCC C  C C     C x O
9  CC x   CCCCCCCC CCC CCCC C C CCC   O
8  CC x   CC       CCCCC  C C C CCCCC O
7  C      CC  I I      C  C C C C   C O
6  C x x  C   x x   CC CxIC C CCC x C O
5  C I ICCC C I I C C  C  C C CCC     O
4  CCCCCC C CCCCCCCCCCCCCCC C  CCC - OO
3  C    C C C        C x CCCCCCCCC x xO
2  C  x CCCCC  x   CCC x CCCCCCC   x xO
1     x        x       x           x
0 -------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456
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
