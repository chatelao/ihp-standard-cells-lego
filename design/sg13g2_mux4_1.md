# Design Documentation for sg13g2_mux4_1

## Substrate
```
01234567890123456789012345678901234567890

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890


pppXppppppppppXpppppppppXppppppppppppXpp
pppXppppppppppXpppppppppXppppppppppppXpp
pppXppppppppppXpppppppppXppppppppppppXpX
   X                                 X X
   X                                   X


   X X       X X         X         X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnXnnnnnnnnnnXnnnnnnnXnnnnnnnnnnnnnnXnX
nnnXnnnnnnnnnnXnnnnnnnXnnnnnnnnnnnnnnXnn
nnnXnnnnnnnnnnXnnnnnnnXnnnnnnnnnnnnnnXnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890


   X G       GXG        XG         G X
   X G       GXG        XG         G X
   X G       GXG        XG         G X X
   X G       G G         G         G X X
   X G       G G         G         G   X
   G G       G G         G         G
   G G       G G         G         G
   X X       X X         X         X
   G G       G G         G         G
   G G       G G         G         G
   G G       G G         G         G
   X G       GXG      X  G         G X X
   X G       GXG      X  G         G X
   X G       GXG      X  G         G X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890
+++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++
   x          x         x            x
   x          x CCCCCCC x   CCCCCCCC x
   x          x C     C x C C      C x x
CC x    CCC     C CCC CCCCC C CC CCC x x
CC x    CCCCCCCCC CCC     C C CC CCC   x
CC +    CCC       CCCCCC  C C CC CCCCC O
C       CCC II I       C  C C C  C   C O
C IxIx  C   Ix x   CCC CIxC C C CC x C O
C IIIICCC CCII I C C   CIIC C C  C I   O
C     C C CC     C CCCCCCCC C CCCCC  - O
CCCCCCC C CCCCCCCCCCC    CC     CCC  - O
CC x  C   C   x   CCC x  CCCCCC CCC  x x
CC x  CCCCC   x   CCC x  CCCCCCCC    x
   x          x       x              x
-----------------------------------------
-----------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890


















```
