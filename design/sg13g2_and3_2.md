# Design Documentation for sg13g2_and3_2

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


ppXpppXpppX
ppXpppXpppX
ppXpppXpXpX
  X   X X
        XXX


   X  X

nnnnnnnnnnn
nnnnnnnnnnn
nnnnXnXnXnX
nnXnnnXnnnX
nnnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901


  XGGGXG  X
  XGGGXG  X
  XGGGXGX X
  XGGGXGX
  GGGG GXXX
  GGGG G
  GGGG G
  GXGGXG
  GGGG G
  GGGG G
  GGGG G
  GGXGXGX X
  XGGGXG  X
  GGGGXG  X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
++++++++++++
  x   x   x
  x   x   x
C x C x x x
C x C x x
C   C   xxx
CCCCCCCC OO
C      C OO
C  x IxCCOO
C  I II  OO
C       OOO
   II - O -
   Ix x x x
IIxII x   x
      x   x
------------
------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901


















```
