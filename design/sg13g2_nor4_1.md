# Design Documentation for sg13g2_nor4_1

## Substrate
```
01234567890

NNNNNNNNNNN
NNNNNNNNNNN
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


Xppppppppp
Xppppppppp
XppppppppX
X        X
X      X X
     X
     X X
 X X   X
   X X
nnnnnnnnnn
nnnnnnnnnn
XnXnnXnXnX
XnnnnXnnnX
XnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890


XG G G G
XG G G G
XG G G G X
XG G G G X
XG G G X X
 G G X G
 G G X X
 X X G X
 G X X G
 G G G G
 G G G G
XGXG X X X
XG G X G X
XG G X G X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
+++++++++++
x
x
x        x
x        x
x      x x
+   Ix I O
    Ix x O
Ix x I xIO
II x x IIO
         O
- OOOOOOOO
x x  x x x
x    x   x
x    x   x
-----------
-----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890


















```
