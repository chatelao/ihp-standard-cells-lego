# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
3
2  pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpppXpppXpppXp
1  pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpppXpppXpXXXp
0  pppXppppppppXpppppXppppppppppppppppppppppppppppppppppppXpXpXpppXpXXXp
9              X     X                                    X X X   X XXX
8              X     X                                      X X   X XXX
7
6   X     X                 X               X
5  nnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnXnXn
2  nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnXnXnnnXnXX
1  nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnXnnnXnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
3
2  G GX  G G G X     X     G G X           G G            X   X   X   X
1  G GX  G G G X     X     G G X           G G            X   X   X XXX
0  G GX  G G G X     X     G G             G G            X X X   X XXX
9  G G   G G G X     X     G G             G G            X X X   X XXX
8  G G   G G G X     X     G G             G G              X X   X XXX
7  G G   G G G             G G             G G
6  GXG   GXG G             GXG             GXG
5  G G  XG GXG             G G             G G
4  G G   GXG G             G G             G G
3  G X   G G G             G G             G G                X     X X
2  G X   G G G X        X  GXG             G G         X    X X X   X XX
1  G X   G G G X        X  GXG             G G         X    X   X   X  X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
3 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2     x CCCCCCCx     x         x                          x   x   x   x
1     x C     Cx CC  x CCCCCCC x CCCC CCCCCCCCCCCCCCCCCCCCx   x   x xxx
0  C  x C CC  Cx CC  x CCCC CC   C  C   CCCCCCCCCC        x x x CCx xxx
9  CCCCCCCCC  Cx CC  x CC   CCCCCCC C   C         C       x x x CCx xxx
8  C   CCC    Cx CC  xCCC CCCCCCCCC C CCC CCCCCCC CCC CCCCCCx x CCx xxx
7  C   C      C   C    CC C       C C  C  C     C C C C    CO + CC   O
6  CxI C  x I CC CCCCC CC C xI C  C C  C CCIxICCC CCC C    COOO  CCC OO
5  C   Cx I x    CC    CC      CC   CC C  CIIIC     CCCCCC C  O   C   OO
4  C   CIIxII CCCCC    CCCCCCCCC CCCCC C  C   C CCCCC      C  O   C   OO
3  C x C      C   C    C  C   C CCCCCC    CCCCC CCCCCC     C  x   C x x
2    x CCCCCCCCx  C  CCCx   x CCCCCCCCCCCCCCCCCCCCCC C x  CCx x x C x xx
1    x         x        x   x                          x    x   x   x  x
0 -----------------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012345678901234567890
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
