# Design Documentation for sg13g2_nor2_2

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


ppXppppppp
ppXppppppp
ppXppppppp
  X
      XX


   X   X

nnnnnnnnnn
nnnnnnnnnn
XnXnnXnXnX
XnnnnXnXnX
XnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890


  X G G G
  X G G G
  X G G G
  X G G G
  G G XXG
  G G G G
  G G G G
  GXG GXG
  G G G G
  G G G G
  G G G G
X X GXGXGX
X G GXGXGX
X G GXG GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
+++++++++++
  x
  x
C x  CCCCC
C x  C   C
C    Cxx
CCCCCCOOOO
         O
  Ix  Ix O
  II  II O
         O
- OOOOOOOO
x x  x x x
x    x x x
x    x   x
-----------
-----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890


















```
