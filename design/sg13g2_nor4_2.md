# Design Documentation for sg13g2_nor4_2

## Substrate
```
0123456789012345678901

NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901


XpppXppppppppppppppppp
XpppXppppppppppppppppp
XpppXppppppppppppppppp
X   X              X
X                  X


  X      X   X   X

nnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnn
XnXnXXXnnXnXnXnXXXnXnX
XnnnXXXnnnnXnnnXXXnnnX
XnnnXXXnnnnXnnnXXXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901


XG GX   G G G G G G
XG GX   G G G G G G
XG GX   G G G G G G
XG GX   G G G G G GX
XG G    G G G G G GX
 G G    G G G G G G
 G G    G G G G G G
 GXG    GXG GXG GXG
 G G    G G G G G G
 G G    G G G G G G
 G G    G G G G G G
XGXGXXX GXGXGXGXXXGX X
XG GXXX G GXG GXXXG  X
XG GXXX G GXG GXXXG  X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901
++++++++++++++++++++++
++++++++++++++++++++++
x   x
x   x
x C x CCCCCCCCCC CCCCC
x C x C  C C C C C x C
x C      C C C   C x C
+ CCCCCCCC C CCCCC O C
                   O
 IxI    Ix  IxI Ix OOO
 III    II  III II OOO
- OOOOOOOOOOOOOOOOOO -
- O      O   O     O -
x x xxx  x x x xxx x x
x   xxx    x   xxx   x
x   xxx    x   xxx   x
----------------------
----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901


















```
