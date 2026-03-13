# Design Documentation for sg13g2_nand2b_2

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


XpppXpppXpppXp
XpppXpppXpppXp
XpppXpXpXpXXXp
X   X X X XXX
X   X X   XXX


 X       X

nnnnnnnnnnnnnn
nnnnnnnnnnnnnn
XnnnnnXnnnnnnn
XnnnnnXnnnnnnn
XnnnnnXnnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123


X G X   X G X
X G X   X G X
X G X X X XXX
X G X X X XXX
X G X X G XXX
G G     G G
G G     G G
GXG     GXG
GGG     G G
G G     G G
G G     G G
X G   X G G
X G   X G G
X G   X G G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
++++++++++++++
x   x   x   x
x   x   x   x
x   x x x xxx
x C x x x xxx
x C x x   xxx
  C + OOOOOO+
  C        O
IxCCC   Ix O
IIC     II O
  C       OO
- C CCCCC OOC
x   C x C   C
x   C x CCCCC
x     x
--------------
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123


















```
