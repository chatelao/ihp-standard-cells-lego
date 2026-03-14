# Design Documentation for sg13g2_mux4_1

## Substrate
```
0123456789012345678901234567890123456
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123456

 pppXppppppppXppppppppXpppppppppppXp
 pppXppppppppXppppppppXpppppppppppXp
 pppXpppppppppppppppppppppppppppppXp
    X
    X

   X X      X X       X         X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnXnnnnnnnnnnnXnX
 nnnXnnnnnnnnXnnnnnnnXnnnnnnnnnnnXnX
 nnnXnnnnnnnnXnnnnnnnXnnnnnnnnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123456

   GXG      GXG       X         G X
   GXG      GXG       X         G X
   GXG      G G       G         G X
   GXG      G G       G         G
   GXG      G G       G         G
   G G      G G       G         G
   X X      X X       X         X
   G G      G G       G         G
   G G      G G       G         G
   G G      G G      XG         GX X
   GXG      GXG      XG         GX X
   GXG      GXG      XG         GX

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123456
+++++++++++++++++++++++++++++++++++++
    x        x CCCCCC x   CCCCCCC x
    x        x C     Cx C C     C x
 CC x   CC     C CCC C  C C     C x O
 CC x   CCCCCCCC CCC CCCC C C CCC   O
 CC x   CC       CCCCC  C C C CCCCC O
 C      CC  I I      C  C C C C   C O
 C x x  C   x x   CC CxIC C CCC x C O
 C I ICCC C I I C C  C  C C CCC     O
 CCCCCC C CCCCCCCCCCCCCCC C  CCC - OO
 C    C C C        C x CCCCCCCCC x xO
 C  x CCCCC  x   CCC x CCCCCCC   x xO
    x        x       x           x
-------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123456














```
