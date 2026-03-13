# Design Documentation for sg13g2_and2_2

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

 XpppXppXp
 XpppXpXXp
 XpppXpXXp
       XX
       XX

   X
 nnnnnnnnn
 nnnnnnnnn
 XnnnXnXXn
 nnnnXnnXn
 nnnnXnnXn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890

GXG GX  X
GXG GX XX
GXG GX XX
G G G  XX
G G G  XX
G G G
G GXG
G G G
G G G
GXG GX XX
GGG GX  X
G G GX  X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
 x   x  x
 x C x xx
 x C x xx
   C   xx
 CCCCC xx
 C   C O
 C x C O
 C I   O
 C     O-
IxI  x xx
III  x  x
     x  x
-----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890














```
