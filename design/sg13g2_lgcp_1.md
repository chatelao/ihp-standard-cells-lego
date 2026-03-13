# Design Documentation for sg13g2_lgcp_1

## Substrate
```
01234567890123456789012345678

NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678


pppXppppppppXppppppXppppXppp
pppXppppppppXppppppXppppXppp
pppXpppppppppppppppXppppXpXp
                   X    X X
                        X X

     X             X
                   X

nnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnXnnnnnXnnnnXnXn
nnnXnnnnnnnnnXnnnnnXnnnnXnXn
nnnXnnnnnnnnnXnnnnnXnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678


   X G      X      X    X
   X G      X      X    X
   X G             X    X X
     G             X    X X
     G             G    X X
     G             G
     X             X
     G             X
     G             G
     G             G
     G             G
     G       X     X    X X
   X G       X     X    X X
   X G       X     X    X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678
+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++
   x        x      x    x
   x        x      x    x
CC x  CCC          x    x x
CC    C     CCCCCC x C  x x
CC CCCCCCCCCC    C   C  x x
CC C   C    C CC C I CC + O
C  CIx C CC C  C C x  C   O
C CCII C CC CC C C x  CCC O
C CCCCCC CCCCCCC C    CCC O
C     C       CC C -  C   O
CCCCC CCC  ---CC   -  C - O
C   C        x     x  C x x
C  xCCCCCCCC x     x    x x
   x         x     x    x
-----------------------------
-----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678


















```
