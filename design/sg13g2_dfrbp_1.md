# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
3
2  XpppppppppXppppppppppppppppppppppppppppXppppppXppp
1  XpppppppppXppppppppppppppppppppppppppppXpXppppXpXp
0  XppppppppppppppppppppppppppppppppppppppXpXppppXpXp
9  X                                      X X    X X
8  X                                        X    X X
7
6         X               X
5  Xnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnXn
2  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnXnnnnXnXn
1  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
3
2  X      G  X            G               X      X
1  X      G  X            G               X X    X X
0  X      G               G               X X    X X
9  X      G               G               X X    X X
8  X      G               G                 X    X X
7  G      G               G
6  G      X               X
5  X      G               G
4  G      G               G
3  G      G               G                 X    X X
2  G  X   X               G          X    X X    X X
1  G  X   X               G          X    X      X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123456789012345678901
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++
2  x         x                            x      x
1  x CCCCCCCCxCCCCC CCCCCCCCCCCCCCCCCCCC  x x  C x x
0  x C    C C C   C    CCCCCCCCCC         x x  C x x
9  x CCCC C CCC C C    C        C         x x  C x x
8  x CC CCCCCCCCC C CCCCCCCCCC CCCCCCCCCCCC x  C x x
7    CC C       C C  C  C      CC  CC     C O  C   O
6  I CC C xI C  C C  C CC xI CCCCC CC     C O  CCCCO
5  x CC      C C  CCCC  C    C     CCCCCC C O  C  CO
4  I CCCCCCCCC CCCC CC  CCCC CC CCCC     CC O  C   O
3    C  C   C CCCCCCCCCC   C CCCCCCCC    C  x  C x x
2  CCCx   x CCCCCCCCCCCCCCCCCCCCCCC Cx  CCx x  C x x
1     x   x                          x    x      x
0 ----------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456789012345678901
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
