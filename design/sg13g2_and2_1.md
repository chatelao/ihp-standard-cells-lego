# Design Documentation for sg13g2_and2_1

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

 XpppXpp
 XpppXpX
 XpppXpX
       X
       X

   X
 nnnnnnn
 nnnnnnn
 XnnnXnX
 nnnnXnn
 nnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678

 X G X
 X G X X
 X G X X
 G G   X
 G G   X
 G G
 G X
 G G
 G G
 X G X X
 G G X
 G G X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
 x   x
 x C x xO
 x C x xO
   C   xO
 CCCCC xO
 C   C  O
 C x C  O
 C I    O
 C     OO
IxI  x xO
III  x
     x
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678














```
