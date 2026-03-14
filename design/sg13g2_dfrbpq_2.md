# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
01234567890123456789012345678901234567890123456789
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123456789

 XpppppppppXpppppppppppppppppppppppppppXppppXpppX
 XpppppppppXpppppppppppppppppppppppppppXppppXpXpX
 XpppppppppppppppppppppppppppppppppppppXppppXpXpX
 X                                     X    X X X
 X                                          X X X

 X      X               X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnXnXnX
 nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnXnXnX
 nnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnXnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123456789

GXG    G G X           G G             X    X   X
GXG    G G X           G G             X    X X X
GXG    G G             G G             X    X X X
GXG    G G             G G             X    X X X
GXG    G G             G G                  X X X
G G    G G             G G
GXG    GXG             GXG
GGG    G G             G G
G G    G G             G G
G G    G G             G G              X   X X X
G G X  GXG             G G         X    X   X X X
G G X  GXG             G G         X    X   X   X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123456789
++++++++++++++++++++++++++++++++++++++++++++++++++
 x         x                           x    x   x
 x CCCCCCCCx CCCC CCCCCCCCCCCCCCCCCCCC x C  x x x
 x CCCC C C  C  C   CCCCCCCCCCC        x C  x x x
 x CC   C CCCCC C   C         C        x C  x x x
 x CC CCCCCCCCC C  CC CCCCCC CCCC CCCCCC C  x x x
   CC C       C C  C  C      CC  CC    C C    O
 x CC C xI C  C C  C CC xI CCCCC CC    C CCC  OOO
 I CC      C C  CC C  C II C     CCCCCCC  C   O
   CCCCCCCCC CCCCC C  C    CC CCCC     C  C   O
   C  C   C CCCCCC    CCCC CCCCCCCC    Cx C x x x
 CCCx   x CCCCCCCCCCCCCCCCCCCCCCC Cx  CCx C x x x
    x   x                          x    x   x   x
--------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123456789














```
