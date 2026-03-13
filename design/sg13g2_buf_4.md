# Design Documentation for sg13g2_buf_4

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


XpppXppppXpppX
XpppXppppXpppX
XpXpXpXppXpppX
X X X X  X   X
X X X X  X


           X

nnnnnnnnnnnnnn
nnnnnnnnnnnnnn
XnXnXnXnnXXnnn
XnXnXnnnnnXnnn
XnnnXnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123


X   X    X G X
X   X    X G X
X X X X  X G X
X X X X  X G X
X X X X  X G
           G
           G
           X
           G
           G
           G
X X X X  XXG
X X X     XG
X   X     XG


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
++++++++++++++
x   x    x   x
x   x    x   x
x x x x  x   x
x x x x  x C x
x x x x  x C
+ O   O  + CCC
  OOOOO      C
OOO   CCC Ix C
OOO   CCC II C
  O     C    C
- OOOOO CCCCCC
x x x x  xx  C
x x x     x
x   x     x
--------------
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123


















```
