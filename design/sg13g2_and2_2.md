# Design Documentation for sg13g2_and2_2

## Substrate
```
012345678901

NNNNNNNNNNNN
NNNNNNNNNNNN
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


 XpppXppppX
 XpppXppppX
 XpppXpXXpX
 X   X XX X
       XX X


    X

 nnnnnnnnnn
 nnnnnnnnnn
 XnnnXnXXnX
 nnnnXnnnnX
 nnnnXnnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901


GXGG X    X
GXGG X    X
GXGG X XX X
GXGG X XX X
G GG G XX X
G GG G
G GG G
G GGXG
G GGGG
G GG G
G GG G
GXGG X XX X
GGGG X    X
G GG X    X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
++++++++++++
 x   x    x
 x   x    x
 x C x xx x
 x C x xx x
   C   xx x
 CCCCC OO +
 C    C O
 C Ix C O
 C II   O
 C     OO -
     - OO -
IxI  x xx x
III  x    x
     x    x
------------
------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901


















```
