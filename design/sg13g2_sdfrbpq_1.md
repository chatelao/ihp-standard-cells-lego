# Design Documentation for sg13g2_sdfrbpq_1

## Substrate
```
01234567890123456789012345678901234567890123456789012345678901
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123456789012345678901

 pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpXpp
 pppXppppppppXpppppXpppppppppXppppppppppppppppppppppppppXpXpp
 pppXppppppppXpppppXppppppppppppppppppppppppppppppppppppXpXpX
             X     X                                    X X X
             X     X                                      X X

  X     X                 X               X
 nnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnX
 nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnX
 nnXnnnnnnnnnXnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123456789012345678901

  G X   G G  X     X      G  X            G             X X
  G X   G G  X     X      G  X            G             X X
  G X   G G  X     X      G               G             X X X
  G     G G  X     X      G               G             X X X
  G     G G  X     X      G               G               X X
  G     G G               G               G
  X     X G               X               X
  G   X G X               G               G
  G     X G               G               G
  GX    G G               G               G                 X
  GX    G G  X        X   X               G          X    X X
  GX    G G  X        X   X               G          X    X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123456789012345678901
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    x CCCCCCCx     x         x                          x x
    x C     Cx CC  x CCCCCCC x CCCC CCCCCCCCCCCCCCCCCCCCx x
 C  x C CC  Cx CC  x CCCC CC   C  C   CCCCCCCCCC        x x x
 CCCCCCCCC  Cx CC  x CC   CCCCCCC C   C         C       x x x
 C   CCC    Cx CC  xCCC CCCCCCCCC C CCC CCCCCCC CCC CCCCCCx x
 C   C      C   C    CC C       C C  C  C     C C C C    C  O
 CxI C  x I CC CC    CC C xI C  C C  C CCIxICCC CCC C    CC O
 C   Cx I x    CCCCC CC      CC   CC C  CIIIC     CCCCCC C  O
 C   CIIxII CCCCC    CCCCCCCCC CCCCC C  C   C CCCCC      C OO
 C x C      C   C    C  C   C CCCCCC    CCCCC CCCCCC     C  x
   x CCCCCCCCx  C  CCCx   x CCCCCCCCCCCCCCCCCCCCCC C x  CCx x
   x         x        x   x                          x    x
--------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123456789012345678901














```
