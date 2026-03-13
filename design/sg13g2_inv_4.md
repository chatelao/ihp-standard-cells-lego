# Design Documentation for sg13g2_inv_4

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


XpppXppppX
XpppXppppX
XpXpXppXpX
X X X  X X
X X    X


   X

nnnnnnnnnn
nnnnnnnnnn
XnXnXnnXnX
XnnnXnnnnX
XnnnXnnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890


X  GX    X
X  GX    X
X XGX  X X
X XGX  X X
X XG   X
   G
   G
   X
   G
   G
   G
X XGX  X X
X  GX    X
X  GX    X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
+++++++++++
x   x    x
x   x    x
x x x  x x
x x x  x x
x x    x
+ OOOOOOOO
        OO
 IIxIII OO
 IIIIII OO
        OO
- OOOOOOOO
x x x  x x
x   x    x
x   x    x
-----------
-----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890


















```
