# Design Documentation for sg13g2_sdfrbpq_2

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123
3
2  pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpppXpp
1  pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpppXpp
0  pppXppppppppXpppppXppppppppppppppppppppppppppppppppppppXpXXXpp
9              X     X                                    X XXX
8              X     X                                      XXX
7
6   X     X                 X               X
5  nnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnXnX
2  nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnXnX
1  nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
3
2  G GX  G G G X     X     G G X           G G            X   X
1  G GX  G G G X     X     G G X           G G            X   X
0  G GX  G G G X     X     G G             G G            X XXX
9  G G   G G G X     X     G G             G G            X XXX
8  G G   G G G X     X     G G             G G              XXX
7  G G   G G G             G G             G G
6  GXG   GXG G             GXG             GXG
5  G G  XG GXG             G G             G G
4  G G   GXG G             G G             G G
3  G X   G G G             G G             G G              X X X
2  G X   G G G X        X  GXG             G G         X    X X X
1  G X   G G G X        X  GXG             G G         X    X   X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2     x CCCCCCCx     x         x                          x   x
1     x C     Cx CC  x CCCCCCC x CCCC CCCCCCCCCCCCCCCCCCCCx   x
0  C  x C CC  Cx CC  x CCCC CC   C  C   CCCCCCCCCC        x xxx
9  CCCCCCCCC  Cx CC  x CC   CCCCCCC C   C         C       x xxx
8  C   CCC    Cx CC  xCCC CCCCCCCCC C CCC CCCCCCC CCC CCCCCCxxx
7  C   C      C   C    CC C       C C  C  C     C C C C    C O
6  CxI C  x I CC CCCCC CC C xI C  C C  C CCIxICCC CCC C    C OO
5  C   Cx I x    CC    CC      CC   CC C  CIIIC     CCCCCC C  O
4  C   CIIxII CCCCC    CCCCCCCCC CCCCC C  C   C CCCCC      C  O
3  C x C      C   C    C  C   C CCCCCC    CCCCC CCCCCC     Cx x x
2    x CCCCCCCCx  C  CCCx   x CCCCCCCCCCCCCCCCCCCCCC C x  CCx x x
1    x         x        x   x                          x    x   x
0 ----------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456789012345678901234567890123
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
