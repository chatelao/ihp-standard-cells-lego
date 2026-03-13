# Design Documentation for sg13g2_inv_2

## Substrate
```
012345

NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345


XpppXX
XpppXX
XpXXXX
X XXXX
X XXXX


 X

nnnnnn
nnnnnn
XnXXXn
XnnnXn
XnnnXn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


X G XX
X G XX
X XXXX
X XXXX
X XXXX
G G
G G
GXG
G G
G G
G G
X XXX
X G X
X G X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++
x   xx
x   xx
x xxxx
x xxxx
x xxxx
+ OO++
   O
Ix OOO
II OOO
   O
- OO-
x xxx
x   x
x   x
------
------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345


















```
