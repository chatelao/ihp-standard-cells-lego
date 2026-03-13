# Design Documentation for sg13g2_nor3_2

## Substrate
```
01234567890123456

NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456


XpppXppppppppppp
XpppXppppppppppp
XpppXppppppppppp
X   X        X
X            X


  X    X     X

nnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnn
XnXnXXXnnXnXnXnX
XnnnXXXnnnnXnnnX
XnnnXXXnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456


XG GX G G   G G
XG GX G G   G G
XG GX G G   G G
XG GX G G   GXG
XG G  G G   GXG
 G G  G G   G G
 G G  G G   G G
 GXG  GXG   GXG
 G G  G G   G G
 G G  G G   G G
 G G  G G   G G
XGXGXXX GX XGXGX
XG GXXX G  XG GX
XG GXXX G  XG GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456
+++++++++++++++++
+++++++++++++++++
x   x
x   x
x C x CCCCCCCCCC
x C x C  C C x C
x C      C   x C
+ CCCCCCCC OOO C
           O
 IxI  Ix OOOIxI
 III  II OOOIII
- OOOOOOOO OOO -
- O      O   O -
x x xxx  x x x x
x   xxx    x   x
x   xxx    x   x
-----------------
-----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456


















```
