# Design Documentation for sg13g2_inv_16

## Substrate
```
0123456789012345678901234567890123456

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123456


XppppXpppXpppXpppXppppXpppXpppXppppX
XppppXpppXpppXpppXppppXpppXpppXppppX
XppXpXpXpXpXpXpXpXpXXpXpXpXpXpXpXppX
X  X X X X X X X X XX X X X X X X  X
X  X   X   X   X   XX   X   X   X  X


                                 X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
XnnXnXnXnXnXnXnXnXnXXnXnXnXnXnXnXnXn
XnnnnXnnnXnnnXnnnXnnnnXnnnXnnnXnnnXn
XnnnnXnnnXnnnXnnnXnnnnXnnnXnnnXnnnXn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123456


X    X   X   X   X    X   X   X  G X
X    X   X   X   X    X   X   X  G X
X  X X X X X X X X XX X X X X X XG X
X  X X X X X X X X XX X X X X X XG X
X  X   X   X   X   XX   X   X   XG X
                                 G
                                 G
                                 X
                                 G
                                 G
                                 G
X  X X X X X X X X XX X X X X X XGX
X    X   X   X   X    X   X   X  GX
X    X   X   X   X    X   X   X  GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123456
+++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++
x    x   x   x   x    x   x   x    x
x    x   x   x   x    x   x   x    x
x  x x x x x x x x xx x x x x x x  x
x  x x x x x x x x xx x x x x x x  x
x  x   x   x   x   xx   x   x   x  x
+  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  +
   OOOOOOOOOOOOOOOOOOOOOOOOOO
   O   O   O   O   OO   O   O   IxII
   O   O   O   O   OO   O   O   IIII
   O   O   O   O   OO   O   O
-  O - O - O - O - OO - O - OOOOO -
x  x x x x x x x x xx x x x x x x x
x    x   x   x   x    x   x   x   x
x    x   x   x   x    x   x   x   x
-------------------------------------
-------------------------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123456


















```
