# Design Documentation for sg13g2_nand2_2

## Substrate
```
01234567890
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890

 XpppXpppX
 XpXpXpXpX
 XpXpppXpX
 X XXXXX X
 X   X   X
       X
   X   X
 nnnnnnnnn
 nnnnnnnnn
 nnnnnnnnn
 nnXnnnnnn
 nnXnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890

 XG GXG GX
 XGXGXGXGX
 XGXG GXGX
 XGXXXXXGX
 XG GXG GX
  G G GXG
  GXG GXG
  G G G G
  G G G G
  G G G G
  GXG G G
  GXG G G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
 x   x   x
 x x x x x
 x x   x x
 x xxxxx x
 x   x I x
     O x
   x O x
   I OOO
 CCCCC O
 C   C   C
 C x CCCCC
   x
-----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890














```
