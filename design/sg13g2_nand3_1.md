# Design Documentation for sg13g2_nand3_1

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


XpppXppp
XpppXppp
XpXpXpXX
X X X XX
X XXXXXX


 X X   X

nnnnnnnn
nnnnnnnn
XnnnnnnX
Xnnnnnnn
Xnnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678


XG GX  G
XG GX  G
XGXGX XX
XGXGX XX
XGXXXXXX
 G G   G
 G G   G
 X X   X
 G G   G
 G G   G
 G G   G
XG G   X
XG G   G
XG G   G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
+++++++++
x   x
x   x
x x x xx
x x x xx
x xxxxxx
     O
     O
Ix x OIx
II I OII
     O
-    OOO
x      x
x
x
---------
---------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678


















```
