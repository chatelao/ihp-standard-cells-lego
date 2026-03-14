# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
3
2  XpppppppppXpppppppppppppppppppppppppppXppppXpp
1  XpppppppppXpppppppppppppppppppppppppppXppppXpX
0  XpppppppppppppppppppppppppppppppppppppXppppXpX
9  X                                     X    X X
8  X                                     X    X X
7
6         X               X
5  Xnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXX
2  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnnnXXX
1  nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678901234567
3
2  X      G  X            G              X    X
1  X      G  X            G              X    X X
0  X      G               G              X    X X
9  X      G               G              X    X X
8  X      G               G              X    X X
7  G      G               G
6  G      X               X
5  X      G               G
4  G      G               G
3  G      G               G                   XXX
2  G  X   X               G          X        XXX
1  G  X   X               G          X        X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789012345678901234567
3 ++++++++++++++++++++++++++++++++++++++++++++++++
2  x         x                           x    x
1  x CCCCCCCCxCCCCC CCCCCCCCCCCCCCCCCCCC x  C x x
0  x C    C C C   C    CCCCCCCCCC        x  C x x
9  x CCCC C CCC C C    C        C        x  C x x
8  x CC CCCCCCCCC C CCCCCCCCCC CCCCC   C x  C x x
7    CC C       C C  C  C      CC  CCCCCCCC C   O
6  I CC C xI C  C C  C CC xI CCCCC CC     C CCCCO
5  x CC      C C  CCCC  C    C     CCCCCC C C CCO
4  I CCCCCCCCC CCCC CC  CCCC CC CCCC      C C   O
3    C  C   C CCCCCCCCCC   C CCCCCCCC    C  C xxx
2  CCCx   x CCCCCCCCCCCCCCCCCCCCCCC Cx  CC  C xxx
1     x   x                          x        x
0 ------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678901234567
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
