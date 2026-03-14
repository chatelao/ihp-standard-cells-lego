# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
3
2  XpppppppppXpppppppppppppppppppppppppppXppppXpppX
1  XpppppppppXpppppppppppppppppppppppppppXppppXpXpX
0  XpppppppppppppppppppppppppppppppppppppXppppXpXpX
9  X                                     X    X X X
8  X                                          X X X
7
6  X      X               X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnXnXnX
2  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnXnXnX
1  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
3
2 GXG    G G X           G G             X    X   X
1 GXG    G G X           G G             X    X X X
0 GXG    G G             G G             X    X X X
9 GXG    G G             G G             X    X X X
8 GXG    G G             G G                  X X X
7 G G    G G             G G
6 GXG    GXG             GXG
5 GGG    G G             G G
4 G G    G G             G G
3 G G    G G             G G              X   X X X
2 G G X  GXG             G G         X    X   X X X
1 G G X  GXG             G G         X    X   X   X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123456789
3 ++++++++++++++++++++++++++++++++++++++++++++++++++
2  x         x                           x    x   x
1  x CCCCCCCCx CCCC CCCCCCCCCCCCCCCCCCCC x C  x x x
0  x CCCC C C  C  C   CCCCCCCCCCC        x C  x x x
9  x CC   C CCCCC C   C         C        x C  x x x
8  x CC CCCCCCCCC C  CC CCCCCC CCCC CCCCCC C  x x x
7    CC C       C C  C  C      CC  CC    C C    O
6  x CC C xI C  C C  C CC xI CCCCC CC    C CCC  OOO
5  I CC      C C  CC C  C II C     CCCCCCC  C   O
4    CCCCCCCCC CCCCC C  C    CC CCCC     C  C   O
3    C  C   C CCCCCC    CCCC CCCCCCCC    Cx C x x x
2  CCCx   x CCCCCCCCCCCCCCCCCCCCCCC Cx  CCx C x x x
1     x   x                          x    x   x   x
0 --------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789
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
