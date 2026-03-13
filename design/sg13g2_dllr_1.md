# Design Documentation for sg13g2_dllr_1

## Substrate
```
0123456789012345678901234567890123
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123

 ppXppppppXppppppppXXpppXpppppXpp
 ppXpppppppppppppppXXpppXpppppXpX
 ppppppppppppppppppXXpppXpXpppXpX
                        X X   X X
                          X   X X
   X X
                       X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnXnnnnnnnnnnnnnnXnnnnXnXnnnXnX
 nnnXnnnnnXnnnnnnnnXnnnnXnXnnnXnX
 nnnXnnnnnXnnnnnnnnXnnnnXnnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123

   X G    X        XX  GX     X
   X G             XX  GX     X X
   G G             XX  GX X   X X
   G G                 GX X   X X
   G G                 G  X   X X
   X X                 G
   G G                 X
   G G                 G
   G G                 G
   GXG             X   GX X   X X
   GXG    X        X   GX X   X X
   GXG    X        X   GX     X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123
++++++++++++++++++++++++++++++++++
   x      x  CCCC  xx   x     x
 C x CCCC    C  C  xx   x     x x
 C   C  CCCC CC C  xx C x x C x x
 CCCCCCCCCCC CC C     C x x C x x
 C     C  CC CC C CCCCC   x C x x
 C x x CC CC CCCCCC  CCCCCOOC   O
 C I I CCCCC C   CCC C x C OCCCCO
 C     CCCCCCC CCCCC C I   OC   O
 C  - CCCCCCCCCCCC  CC    OOC   O
 C  x CCC        C xCC  x x C x x
    x CCC x   CCCC xCC  x x   x x
    x     x        x    x     x
----------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123














```
