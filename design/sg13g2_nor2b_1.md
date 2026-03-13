# Design Documentation for sg13g2_nor2b_1

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

 ppXpppp
 ppXppXX
 ppXppXX
   X  XX
     XXX

 X    X
 nnnnnnn
 nnnnnnn
 nnnnXnX
 nnXnXnX
 nnXnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678

 G X  G
 G X  XX
 G X  XX
 G X  XX
 G   XXX
 G    G
 X    X
 G    G
 G    G
 G   XGX
 G X XGX
 G X  GX

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
   x
   x  xx
 C x  xx
 C x  xx
 CCC xxx
   C O
 x C OxI
   C O
 CCC O -
     x x
   x x x
   x   x
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678














```
