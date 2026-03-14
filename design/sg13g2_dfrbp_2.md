# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
3
2  XpppppppppXpppppppppppppppppppppppppppXppXpppXpppXp
1  XpppppppppXpppppppppppppppppppppppppppXppXpppXpXXXp
0  XpppppppppppppppppppppppppppppppppppppXpXXpppXpXXXp
9  X                                     X XX   X XXX
8  X                                       XX   X XXX
7
6  X      X               X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnXnXn
2  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnXnXnnnXnXn
1  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnXnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
3
2 GXG    G G X           G G             X  X   X   X
1 GXG    G G X           G G             X  X   X XXX
0 GXG    G G             G G             X XX   X XXX
9 GXG    G G             G G             X XX   X XXX
8 GXG    G G             G G               XX   X XXX
7 G G    G G             G G
6 GXG    GXG             GXG
5 GGG    G G             G G
4 G G    G G             G G
3 G G    G G             G G                X     X X
2 G G X  GXG             G G         X    X X X   X X
1 G G X  GXG             G G         X    X   X   X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
3 +++++++++++++++++++++++++++++++++++++++++++++++++++++
2  x         x                           x  x   x   x
1  x CCCCCCCCx CCCC CCCCCCCCCCCCCCCCCCCC x  x   x xxx
0  x CCCC C C  C  C   CCCCCCCCCCC        x xx CCx xxx
9  x CC   C CCCCC C   C         C        x xx CCx xxx
8  x CC CCCCCCCCC C  CC CCCCCC CCCC CCCCCC xx CCx xxx
7    CC C       C C  C  C      CC  CC    C O+ CC   O
6  x CC C xI C  C C  C CC xI CCCCC CC    C OO  CCC OO
5  I CC      C C  CC C  C II C     CCCCCCC  O   C   OOO
4    CCCCCCCCC CCCCC C  C    CC CCCC     C  O   C   OOO
3    C  C   C CCCCCC    CCCC CCCCCCCC    C  x   C x x
2  CCCx   x CCCCCCCCCCCCCCCCCCCCCCC Cx  CCx x x C x x -
1     x   x                          x    x   x   x   -
0 -----------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012
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
