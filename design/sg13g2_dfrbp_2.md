# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
01234567890123456789012345678901234567890123456789012
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123456789012

 XpppppppppXpppppppppppppppppppppppppppXppXpppXpppXp
 XpppppppppXpppppppppppppppppppppppppppXppXpppXpXXXp
 XpppppppppppppppppppppppppppppppppppppXpXXpppXpXXXp
 X                                     X XX   X XXX
 X                                       XX   X XXX

 X      X               X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnXnXn
 nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnXnXnnnXnXn
 nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnXnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123456789012

GXG    G G X           G G             X  X   X   X
GXG    G G X           G G             X  X   X XXX
GXG    G G             G G             X XX   X XXX
GXG    G G             G G             X XX   X XXX
GXG    G G             G G               XX   X XXX
G G    G G             G G
GXG    GXG             GXG
GGG    G G             G G
G G    G G             G G
G G    G G             G G                X     X X
G G X  GXG             G G         X    X X X   X X
G G X  GXG             G G         X    X   X   X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123456789012
+++++++++++++++++++++++++++++++++++++++++++++++++++++
 x         x                           x  x   x   x
 x CCCCCCCCx CCCC CCCCCCCCCCCCCCCCCCCC x  x   x xxx
 x CCCC C C  C  C   CCCCCCCCCCC        x xx CCx xxx
 x CC   C CCCCC C   C         C        x xx CCx xxx
 x CC CCCCCCCCC C  CC CCCCCC CCCC CCCCCC xx CCx xxx
   CC C       C C  C  C      CC  CC    C O+ CC   O
 x CC C xI C  C C  C CC xI CCCCC CC    C OO  CCC OO
 I CC      C C  CC C  C II C     CCCCCCC  O   C   OOO
   CCCCCCCCC CCCCC C  C    CC CCCC     C  O   C   OOO
   C  C   C CCCCCC    CCCC CCCCCCCC    C  x   C x x
 CCCx   x CCCCCCCCCCCCCCCCCCCCCCC Cx  CCx x x C x x -
    x   x                          x    x   x   x   -
-----------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123456789012














```
