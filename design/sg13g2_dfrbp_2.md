# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
01234567890123456789012345678901234567890123456789012345678

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123456789012345678


XppppppppppXpppppppppppppppppppppppppppppppXpppXpppXppppXp
XppppppppppXpppppppppppppppppppppppppppppppXpppXpppXppppXp
XppppppppppXpppppppppppppppppppppppppppppppXpXpXpppXpXXpXp
X                                          X X X   X XX X
X                                          X X X   X XX X


 X       X                X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnXnXnnnXnXnX
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnXnXnnnXnXnX
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnnXnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123456789012345678


X G     G GX             G G               X   X   X    X
X G     G GX             G G               X   X   X    X
X G     G GX             G G               X X X   X XX X
X G     G G              G G               X X X   X XX X
X G     G G              G G               X X X   X XX X
G G     G G              G G
G G     G G              G G
GXG     GXG              GXG
GGG     G G              GGG
G G     G G              G G
G G     G G              G G
G G X   X G              G G           X    X  X X   X X X
G G X   X G              G G           X    X  X X   X X X
G G X   X G              G G           X    X    X   X   X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123456789012345678
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
x          x                               x   x   x    x
x CCCCCCCCCx       CCCCCCCCCCCCCCCCCCCCCC  x   x   x    x
x C       Cx CCCCC                         x x x   x xx x
x C CCC C C  C C C    CCCCCCCCCCCC         x x x CCx xx x
x C C   C CCCC C C    C          C         x x x CCx xx x
+ C C CCCCCCCCCC C  CCC CCCCCC C CCCCCCCCCCC O + CC+ OO +
  C C C        C C   C  C      C C  CC     C O + CC   O
IxC C C Ix C   C C   C CCIxI   C C  CC     C O    CCC O
IIC C   II C C C CCC C CCIII CCC CC C    C C OOO  CCC OO
  C CCCCCCCC CCCCC C C  C    C  CCCCCCCCCC C  OO   C   OOO
  C   C   C        C    CCCC CC            C  OO   C - OOO
CCC x C x C CCCCCCCC       C CCCCCCCCC x  CCx  x x C x x x
    x   x CCCCCCCCCCCCCCCCCCCCCCCCCC   x    x  x x C x x x
    x   x                              x    x    x   x   x
-----------------------------------------------------------
-----------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123456789012345678


















```
