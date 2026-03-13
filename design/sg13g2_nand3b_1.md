# Design Documentation for sg13g2_nand3b_1

## Substrate
```
012345678901

NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901


pppXpppXppp
pppXpppXppp
pppXpXpXpXX
   X X X XX
   X X   XX


 X  X X

nnnnnnnnnnn
nnnnnnnnnnn
nnXXnnnnnnX
nnXXnnnnnnn
nnXXnnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901


 G XG GX
 G XG GX
 G XGXGX XX
 G XGXGX XX
 G XGXG  XX
 G  G G
 G  G G
 X  X X
 G  G G
 G  G G
 G  G G
 GXXG G   X
 GXXG G
 GXXG G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
++++++++++++
   x   x
   x   x
   x x x xx
CC x x x xx
CC x x   xx
C  + OOOOOO
C         O
Cx  x x CCO
CI  I I C O
C       C O
CCCCCCCCC O
  xx      x
  xx
  xx
------------
------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901


















```
