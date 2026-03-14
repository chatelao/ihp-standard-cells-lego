# Design Documentation for sg13g2_buf_2

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

 XppppXp
 XppppXp
 Xpppppp

    X

      X
 nnnnnnn
 nnnnnnn
 nXnXnXn
 nXnXnXn
 nXnnnXn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678

 X   GXG
 X   GXG
 X   G G
     G G
    XG G
     G G
     GXG
     G G
     G G
  X XGXG
  X XGXG
  X  GXG

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
 x    x
 x    xC
 x     C
  CCCCCC
 CC xC C
 C  OC
 COOOCxI
    OC
  - OCCC
  x x xC
  x x x
  x   x
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678














```
