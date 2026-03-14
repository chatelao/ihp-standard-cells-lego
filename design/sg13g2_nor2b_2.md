# Design Documentation for sg13g2_nor2b_2

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

 ppXppppppp
 ppXppppppp
 ppXppppppp
   X   X
   X XXX

         X
 nnnnnnnnnn
 nnnnnnnnnn
 XnXnXnXnXn
 nnXnnnXnnn
 nnXnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901

G GX    G G
G GX    G G
G GX    G G
G GX   XG G
G GX XXXG G
G G     G G
G G     GXG
G G     G G
G G     G G
GXGX X XGXG
GGGX   XG G
G GX   XG G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
   x       +
   x CCCCC +
 C x C   C +
 C x   x C +
 C x xxx C +
 C   O
 CCC O  IxI
 C   O
 C - OOOOO -
 x x x x x -
 I x   x   -
   x   x   -
------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901














```
