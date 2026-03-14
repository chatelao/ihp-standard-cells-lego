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
 XpXpXpX
 XpXpXpX
 X X   X
 X XXXXX

 X X  X
 nnnnnnn
 nnnnnnn
 XnnnnnX
 XnnnnnX
 Xnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678

 X G XG
 X X XGX
 X X XGX
 X X  GX
 X XXXXX
 G G  G
 X X  X
 G G  G
 G G  G
 X G  GX
 X G  GX
 X G  G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
 x   x
 x x x x
 x x x x
 x x   x
 x xxxxx
     O
 x x OxI
     O
 -   OOO
 x     x
 x     x
 x
---------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678














```
