# Design Documentation for sg13g2_inv_8

## Substrate
```
0123456789012345678

NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678


XpppXpppXppppXpppX
XpppXpppXppppXpppX
XpXpXpXpXppXpXpXpX
X X X X X  X X X X
X X   X    X X X X


     X

nnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnn
XnXnXnXnXnnXnXnXnX
XnnnXnnnXnnnnXnnnX
XnnnXnnnXnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678


X   XG  X    X   X
X   XG  X    X   X
X X XGX X  X X X X
X X XGX X  X X X X
X X  GX    X X X X
     G
     G
     X
     G
     G
     G
X X XGX X  X X X X
X   XG  X    X   X
X   XG  X    X   X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678
+++++++++++++++++++
+++++++++++++++++++
x   x   x    x   x
x   x   x    x   x
x x x x x  x x x x
x x x x x  x x x x
x x   x    x x x x
+ OOOOOOOOOO + O +
          OO   O
  IIIxIII OOOOOO
  IIIIIII OOOOOO
          OO   O
- OOOOOOOOOO - O -
x x x x x  x x x x
x   x   x    x   x
x   x   x    x   x
-------------------
-------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678


















```
