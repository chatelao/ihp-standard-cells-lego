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

 pppXpppXpp
 pppXpXpXpX
 pppXpXpXpX
    X X   X
    X XXXXX

   X X X
 nnnnnnnnnn
 nnnnnnnnnn
 nnnnnnnnnX
 nnnXnnnnnX
 nnnXnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901

   GXG GX
   GXGXGX X
   GXGXGX X
   GXGXG  X
   GXGXXXXX
   G G G
   X X X
   G G G
   G G G
   G G G  X
   GXG G  X
   GXG G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
    x   x
    x x x xO
  C x x x xO
  C x x   xO
  C x xxxxxO
  C        O
  Cx x x C O
  CI I I C O
  CCCCCCCCOO
          xO
    x     xO
    x
------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901














```
