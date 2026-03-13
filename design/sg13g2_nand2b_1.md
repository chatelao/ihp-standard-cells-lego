# Design Documentation for sg13g2_nand2b_1

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

 ppXppXp
 ppXXpXp
 ppXXppp
   XXXXX
       X

 X X
 nnnnnnn
 nnnnnnn
 nnXnnXX
 nnXnnXX
 nnXnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678

 G X  X
 G XX X
 G XX
 G XXXXX
 G G   X
 G G
 X X
 G G
 G G
 G X  XX
 G X  XX
 G X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
   x  x
   xx x
 C xx
 C xxxxx
 CCCCC x
     C O
 x x CCO
     C O
 CCCCCOO
 C x  xx
   x  xx
   x
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678














```
