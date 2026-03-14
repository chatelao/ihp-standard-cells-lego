# Design Documentation for sg13g2_sdfrbpq_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
3
2  pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpXpp
1  pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpXpp
0  pppXppppppppXpppppXppppppppppppppppppppppppppppppppppppXpXpX
9              X     X                                    X X X
8              X     X                                      X X
7
6   X     X                 X               X
5  nnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnX
2  nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnX
1  nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
3
2   G X   G G  X     X      G  X            G             X X
1   G X   G G  X     X      G  X            G             X X
0   G X   G G  X     X      G               G             X X X
9   G     G G  X     X      G               G             X X X
8   G     G G  X     X      G               G               X X
7   G     G G               G               G
6   X     X G               X               X
5   G   X G X               G               G
4   G     X G               G               G
3   GX    G G               G               G                 X
2   GX    G G  X        X   X               G          X    X X
1   GX    G G  X        X   X               G          X    X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2     x CCCCCCCx     x         x                          x x
1     x C     Cx CC  x CCCCCCC x CCCC CCCCCCCCCCCCCCCCCCCCx x
0  C  x C CC  Cx CC  x CCCC CC   C  C   CCCCCCCCCC        x x x
9  CCCCCCCCC  Cx CC  x CC   CCCCCCC C   C         C       x x x
8  C   CCC    Cx CC  xCCC CCCCCCCCC C CCC CCCCCCC CCC CCCCCCx x
7  C   C      C   C    CC C       C C  C  C     C C C C    C  O
6  CxI C  x I CC CC    CC C xI C  C C  C CCIxICCC CCC C    CC O
5  C   Cx I x    CCCCC CC      CC   CC C  CIIIC     CCCCCC C  O
4  C   CIIxII CCCCC    CCCCCCCCC CCCCC C  C   C CCCCC      C OO
3  C x C      C   C    C  C   C CCCCCC    CCCCC CCCCCC     C  x
2    x CCCCCCCCx  C  CCCx   x CCCCCCCCCCCCCCCCCCCCCC C x  CCx x
1    x         x        x   x                          x    x
0 --------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012345678901
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
