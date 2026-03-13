# Design Documentation for sg13g2_dllr_1

## Substrate
```
012345678901234567890123456789012345

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567890123456789012345


ppXpppppppXppppppppXXXpppXppppppXpp
ppXpppppppXppppppppXXXpppXppppppXpp
ppXppppppppppppppppXXXpppXpXppppXpX
                         X X    X X
                         X X    X X


  X X                   X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnXnnnnnnnnnnnnnnnnXnnnnnXnXXnnnXnX
nnXnnnnnnnXnnnnnnnnXnnnnnXnXXnnnXnX
nnXnnnnnnnXnnnnnnnnXnnnnnXnnnnnnXnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456789012345


  X G     X        XXX  GX      X
  X G     X        XXX  GX      X
  X G              XXX  GX X    X X
  G G                   GX X    X X
  G G                   GX X    X X
  G G                   G
  G G                   G
  X X                   X
  G G                   G
  G G                   G
  G G                   G
  X G              X    GX XX   X X
  X G     X        X    GX XX   X X
  X G     X        X    GX      X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456789012345
++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++
  x       x        xxx   x      x
  x       x CCCCC  xxx   x      x
C x CCCCCCC C   C  xxx C x x    x x
C   C      CC C C      C x x CC x x
CCCCCCCCCC CC C C      C x x CC x x
C    C   C CCCC C CCCCCC   O  C + O
CIIIIC C C C CCCCCC  CCCCCCOO C   O
CIxIxC C C C C   CC  C Ix C O CCCCO
CIIIIC CCCCCCC CCCCC C II C O CCCCO
C    C C       CCC   C      O C   O
C - CC CCCCCCCCCCC - C   - OO C - O
  x CC C         C x C   x xxCC x x
  x CC C  x   CCCC x C   x xx   x x
  x       x        x     x      x
------------------------------------
------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456789012345


















```
