# Design Documentation for sg13g2_and3_1

## Substrate
```
012345678901
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

 ppXpppXXpp
 ppXpppXXpX
 ppXpppXXpX
          X
          X

    X  X
 nnnnnnnnnn
 nnnnnnnnnn
 nnnnXnXnXn
 nnXnnnXnnn
 nnnnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901

   XGG XX
   XGG XX X
   XGG XX X
    GG G  X
    GG G  X
    GG G
    XG X
    GG G
    GG G
    GX X X
   XGG X
    GG X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
   x   xx
  Cx C xx xO
  Cx C xx xO
  C  C    xO
  CCCCCCC xO
  C     C  O
  C xI xCC O
  C II I   O
  C      OOO
     x x x
 IIxII x
       x
------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901














```
