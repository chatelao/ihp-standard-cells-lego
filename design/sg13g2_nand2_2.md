# Design Documentation for sg13g2_nand2_2

## Substrate
```
01234567890

NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890


XppppXpppX
XppppXpppX
XppXpXpXpX
X  X   X X
X  XXXXX X

       X
   X   X

nnnnnnnnnn
nnnnnnnnnn
nnnXnnnnnn
nnnXnnnnnn
nnnXnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890


X G GXG GX
X G GXG GX
X GXGXGXGX
X GXG GXGX
X GXXXXXGX
  G G G G
  G G GXG
  GXG GXG
  GGG G G
  G G G G
  G G G G
  GXG G G
  GXG G G
  GXG G G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
+++++++++++
x    x   x
x    x   x
x  x x x x
x  x   x x
x  xxxxx x
+    OII +
     OIx
  Ix OIx
  II OOO
       O
CCCCCC O C
C  x C   C
C  x CCCCC
   x
-----------
-----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890


















```
