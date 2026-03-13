# Design Documentation for sg13g2_dllrq_1

## Substrate
```
0123456789012345678901234567
NNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567

 pppXpppppXpppppppXXXpppXpp
 pppXpppppXpppppppXXXpppXpX
 pppXpppppppppppppXXXpppXpX
    X                     X
    X                     X

   X X                 X
 nnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnXnX
 nnnnnnnnnnnnnnnnnnXnnnnXnX
 nnnXnnnnnXXXnnnnnnXnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567

   GXG    X       XXX  GX
   GXG    X       XXX  GX X
   GXG            XXX  GX X
   GXG                 G  X
   GXG                 G  X
   G G                 G
   X X                 X
   G G                 G
   G G                 G
   G G                 GX X
   G G             X   GX X
   GXG    XXX      X   GX

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567
++++++++++++++++++++++++++++
    x     x       xxx   x
    x     x       xxx   x xO
 CC x CCCCCCCCCCC xxx C x xO
 CC x CC        C     C   xO
 CC x CCCC   CC C CCCCCCCCxO
 C     C CCCCCCCCCCC C   C O
 C x x C C  CC     C C x C O
 C     C CCCCCCCC  CCC I C O
 CC   CCCCCC       C C     O
 CC       CC   CCCCC C  x xO
 CCCCCCCCCCC   C   x C  x xO
    x     xxx      x    x
----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567














```
