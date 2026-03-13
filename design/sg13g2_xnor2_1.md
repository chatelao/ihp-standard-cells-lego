# Design Documentation for sg13g2_xnor2_1

## Substrate
```
01234567890123

NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123


XpppppXpppppXp
XpppppXpppppXp
XpppppXpppXpXp
X     X   X X
X         X
       X
         X
     X X X

nnnnnnnnnnnnnn
nnnnnnnnnnnnnn
XnnnnnnnnnnnnX
XnnnnnnnXnnnnn
XnnnnnnnXnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123


X     XG G  X
X     XG G  X
X     XG GX X
X     XG GX X
X      G GX
       X G
       G X
     X X X
       G G
       G G
       G G
X      G G   X
X      GXG
X      GXG


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
++++++++++++++
x     x     x
x     x     x
x     x   x x
x  C  x   x x
x CC      x
  C  IIxI OOOO
  C  I   x   O
  C IxIx x C O
  C IIII   C O
- C CCCCCCCC O
- CCC        O
x     CCCCCC x
x       x
x       x
--------------
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123


















```
