# Design Documentation for sg13g2_einvn_8

## Substrate
```
012345678901234567890123456789012345678
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567890123456789012345678

 XpppppXpppXpppXppXppppppppppppppppppp
 XpppppXpppXpppXppXppppppppppppppppppp
 XpppppXpppXpppXppXppppppppppppppppppp
 X     X   X   X       X   X   X   X
 X     X   X   X       XXXXXXXXXXXXX

 X                              X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 XnnnnnnXnnnXnnnXnnXnnnnnnnnnnnXnnnXnn
 XnnnnnnXnnnXnnnXnnXnnnnnnnnnnnnnnnnnn
 XnnnnnnXnnnXnnnXnnXnnnnnnnnnnnnnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456789012345678

 X     X   X   X  X             G
 X     X   X   X  X             G
 X     X   X   X  X             G
 X     X   X   X       X   X   XG  X
 X     X   X   X       XXXXXXXXXXXXX
 G                              G
 X                              X
 G                              G
 G                              G
 X      X   X   X  X           XG  X
 X      X   X   X  X            G
 X      X   X   X  X            G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456789012345678
+++++++++++++++++++++++++++++++++++++++
 x     x   x   x  x
 x C C x C x C x Cx  CCCCCCCCCCCCCCCC
 x C C x C x C x Cx  C   C   C   C  C
 x C C x C x C x C   C x   x C x   xC
 x C C x C x C x CCCCC xxxxxxxxxxxxxC
   C CCCCCCCCCCCCC     OOO
 x C  CCCCCCCCCCCCCCCC OOO  IIIIxIII
 I CCCC   C   C   C  C OOO
   CCCC - C - C - C  C OOOOOOOOOOOOOC
 x CCCC x C x C x Cx C         x   xC
 x CCCC x C x C x Cx CCCCCCCCCCCCCCCC
 x      x   x   x  x
---------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456789012345678














```
