# Design Documentation for sg13g2_einvn_4

## Substrate
```
0123456789012345678901234

NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234


pXpppppXXpppXppppppppppp
pXpppppXXpppXppppppppppp
pXpppppXXpppXppppppppppp
 X     XX   X   X   X
 X     XX   X   X   X


 X                 X

nnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnn
nXnnnnnnXnnnnXnnnnnnnnnn
nXnnnnnnXnnnnXnnnnnnnnnn
nXnnnnnnXnnnnXnnnnnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234


 X     XX   X      G
 X     XX   X      G
 X     XX   X      G
 X     XX   X   X  GX
 X     XX   X   X  GX
 G                 G
 G                 G
 X                 X
 G                 G
 G                 G
 G                 G
 X      X    X     G
 X      X    X     G
 X      X    X     G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234
+++++++++++++++++++++++++
+++++++++++++++++++++++++
 x     xx   x
 x     xx   x CCCCCCCCC
 x C C xx C x C   C   C
 x C C xx C x C x C x C
 x C C xx C x C x   x C
 + C C ++ C + C OOOOO C
   C CCCCCCCCCC OO
Ix C             OIxII
II C  CCCCCCCCCC OIIII
   C  C   CC   C OOOOO
 - CCCC - CC - C O   O C
 x CCCC x CC x CCCCC   C
 x      x    x CCCCCCCCC
 x      x    x
-------------------------
-------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234


















```
