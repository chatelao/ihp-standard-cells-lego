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


pXpppppp
pXpppppp
pXpppppX
 X     X
 X XXXXX


 X   X X

nnnnnnnn
nnnnnnnn
nXnXnXnX
nXnnnXnn
nXnnnXnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678


 X   G G
 X   G G
 X   G X
 X   G X
 X XXXXX
 G   G G
 G   G G
 X   X X
 G   G G
 G   G G
 G   G G
 X X X X
 X   X G
 X   X G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
+++++++++
 x
 x
 x     x
 x     x
 x xxxxx
 + O   O
   O
Ix OIxIx
II OIIII
   O
 - OOOOO
 x x x x
 x   x
 x   x
---------
---------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678


















```
