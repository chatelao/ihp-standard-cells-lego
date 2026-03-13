# Design Documentation for sg13g2_buf_2

## Substrate
```
012345678

NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678


XppppXpp
XppppXpp
XppppXpp
X



       X

nnnnnnnn
nnnnnnnn
nXnXnXnn
nXnnnXnn
nXnnnXnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678


X    XG G
X    XG G
X    XG G
X     G G
      G G
      G G
      G G
      GXG
      G G
      G G
      G G
 X X XG G
 X   XG G
 X   XG G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
+++++++++
x    x
x    x
x    x C
xCCCCCCC
 C   C C
CC O C C
C  O C
C OO CIx
C OO CII
   O CCC
 - O   C
 x x x C
 x   x
 x   x
---------
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678


















```
