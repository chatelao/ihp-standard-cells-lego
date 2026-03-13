# Design Documentation for sg13g2_nor3_1

## Substrate
```
012345678
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

 Xpppppp
 XpppppX
 XpppppX
 X  XXXX
 X  X  X

 X   X X
 nnnnnnn
 nnnnnnn
 XnnXnnX
 XnnXXnX
 XnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678

 X   G G
 X   G X
 X   G X
 X  XXXX
 X  XG X
 G   G G
 X   X X
 G   G G
 G   G G
 X  XG X
 X  XX X
 X   X G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
 x
 x     x
 x     x
 x  xxxx
 x  x  x
    O
 x  Ox x
    O
    OOOO
 x  x  x
 x  xx x
 x   x
---------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678














```
