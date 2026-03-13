# Design Documentation for sg13g2_einvn_8

## Substrate
```
0123456789012345678901234567890123456789012

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123456789012


XXpppppXpppXpppXXpppXppppppppppppppppppppp
XXpppppXpppXpppXXpppXppppppppppppppppppppp
XXpppppXpppXpppXXpppXppppppppppppppppppppp
XX     X   X   XX   X    X   X    X   X
XX     X   X   XX        X   X    X   X


 X                                 X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nXnnnnnnXnnnXnnnnXnnnXnnnnnnnnnnnnnnnnnnnn
nXnnnnnnXnnnXnnnnXnnnXnnnnnnnnnnnnnnnnnnnn
nXnnnnnnXnnnXnnnnXnnnXnnnnnnnnnnnnnnnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123456789012


XX     X   X   XX   X              G
XX     X   X   XX   X              G
XX     X   X   XX   X              G
XX     X   X   XX   X    X   X    XG  X
XX     X   X   XX        X   X    XG  X
 G                                 G
 G                                 G
 X                                 X
 G                                 G
 G                                 G
 G                                 G
 X      X   X    X   X             G
 X      X   X    X   X             G
 X      X   X    X   X             G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123456789012
+++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++
xx     x   x   xx   x
xx     x   x   xx   x  CCCCCCCCCCCCCCCCCC
xx C C x C x CCxx C x  C   C   CC   C   C
xx C C x C x CCxx C x  C x C x CC x C x C
xx C C x C x CCxx C    C x   x    x   x C
++ C C + C + CC++ CCCCCC OOOOOOOOOOOOOO C
   C CCCCCCCCCCCCCC      OOO
Ix C                     OOO  IIIIIxIIII
II C  CCCCCCCCCCCCCCCCCC OOO  IIIIIIIIII
   CC C   C    C   C   C OOOOOOOOOOOOOO
 - CC C - C -  C - C - C O   O    O   O C
 x CC C x C x  C x C x C   C   CC   C   C
 x CC   x   x    x   x CCCCCCCCCCCCCCCCCC
 x      x   x    x   x
-------------------------------------------
-------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123456789012


















```
