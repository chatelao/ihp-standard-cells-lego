# Design Documentation for sg13g2_nor2b_2

## Substrate
```
0123456789012

NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012


ppXppppppppX
ppXppppppppX
ppXppppppppX
  X        X
  X    X   X


         X

nnnnnnnnnnnn
nnnnnnnnnnnn
nXXnnXnXnXnX
nnXnnnnXnnnX
nnXnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012


G X     G GX
G X     G GX
G X     G GX
G X     G GX
G X    XG GX
G G     G G
G G     G G
G G     GXG
G G     G G
G G     G G
G G     G G
GXX  X XGXGX
GGX    XG GX
G X    XG GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012
+++++++++++++
+++++++++++++
  x        x
  x        x
C x  CCCCC x
C x  C   C x
C x    x C x
C +  OOO C +
C    O
CCCC O  IxI
C    O  III
C -  OOOOO -
  -  O   O -
Ixx  x x x x
IIx    x   x
  x    x   x
-------------
-------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012


















```
