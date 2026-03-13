# Design Documentation for sg13g2_buf_16

## Substrate
```
0123456789012345678901234567890123456789012345678

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123456789012345678


XpppXppppXpppXpppXpppXppppXpppXpppXpppXppppXpppX
XpppXppppXpppXpppXpppXppppXpppXpppXpppXppppXpppX
XpXpXpXXpXpXpXpXpXpXpXpXXpXpXpXpXpXpppXppppXpppX
X X X XX X X X X X X X XX X X X X X   X    X   X
X X   XX X X   X   X   XX   X   X              X


                                            X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
XnXnXnXXnXnXnXnXnXnXnXnXXnXnXnXnXnXnnnXnnnnXnnnX
XnnnXnnnnXnnnXnnnXnnnXnnnnXnnnXnnnXnnnXnnnnXnnnX
XnnnXnnnnXnnnXnnnXnnnXnnnnXnnnXnnnXnnnXnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123456789012345678


X   X    X   X   X   X    X   X   X   X    XG  X
X   X    X   X   X   X    X   X   X   X    XG  X
X X X XX X X X X X X X XX X X X X X   X    XG  X
X X X XX X X X X X X X XX X X X X X   X    XG  X
X X   XX X X   X   X   XX   X   X           G  X
                                            G
                                            G
                                            X
                                            G
                                            G
                                            G
X X X XX X X X X X X X XX X X X X X   X    XG  X
X   X    X   X   X   X    X   X   X   X    XG  X
X   X    X   X   X   X    X   X   X   X    XG  X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123456789012345678
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
x   x    x   x   x   x    x   x   x   x    x   x
x   x    x   x   x   x    x   x   x   x    x   x
x x x xx x x x x x x x xx x x x x x C x CC x C x
x x x xx x x x x x x x xx x x x x x C x CC x C x
x x   xx x x   x   x   xx   x   x   C   CC   C x
+ OOOOOO + OOOOOOOOOOOOOOOOOOOOOO CCCCCCCCCCCC +
  O   OO   O   O   O   OO         C
  O   OOOOOO   O   O   OO CCCCCCCCC       IIxII
  O   OOOOOO   O   O   OO CCCCCCCCC       IIIII
  O   OO   O   O   O   OO         C
- O - OO - O - O - O - OOOOOOOOOO CCCCCCCCCCCC -
x x x xx x x x x x x x xx x x x x x C x CC x C x
x   x    x   x   x   x    x   x   x   x    x   x
x   x    x   x   x   x    x   x   x   x    x   x
-------------------------------------------------
-------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123456789012345678


















```
