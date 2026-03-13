# Design Documentation for sg13g2_nor2_1

## Substrate
```
012345

NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345


pXpppp
pXpppp
pXppXX
 X  XX
 X  XX


 X   X

nnnnnn
nnnnnn
nXnXnX
nXnXnX
nXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


 X   G
 X   G
 X  XX
 X  XX
 X  XX
 G   G
 G   G
 X   X
 G   G
 G   G
 G   G
 X X X
 X X X
 X   X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++
 x
 x
 x  xx
 x  xx
 x  xx
 + OOO
   O
Ix OIx
II OII
   O
 - O -
 x x x
 x x x
 x   x
------
------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345


















```
