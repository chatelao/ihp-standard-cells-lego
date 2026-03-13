# Design Documentation for sg13g2_buf_16

## Substrate
```
01234567890123456789012345678901234567890123
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123

 XpppXppXXppXpppXpppXpppXppXpppXpppXpppXppX
 XpXpXpXXXXpXpXpXpXpXpXpXpXXpXpXpppXpppXppX
 XpXpXpXXXXpXpXpXpXpXpXpXpXXpXpXpppXpppXppX
 X X X XXXX X X X X X X X XX X X   X   X  X
 X XXXXXXXXXXXXXXXXXXXXXXXXXXX            X

                                        X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 XnXnXnXXXXnXnXnXnXnXnXnnnXnnXnnnnnnnnnnnnX
 XnXnXnXXXXnXnXnXnXnXnXnXnXXnXnXnnnXnnnXnnX
 XnnnXnnXXnnXnnnXnnnXnnnXnnXnnnXnnnXnnnXnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123

 X   X  XX  X   X   X   X  X   X   X   XG X
 X X X XXXX X X X X X X X XX X X   X   XG X
 X X X XXXX X X X X X X X XX X X   X   XG X
 X X X XXXX X X X X X X X XX X X   X   XG X
 X XXXXXXXXXXXXXXXXXXXXXXXXXXX          G X
                                        G
                                        X
                                        G
                                        G
 X X X XXXX X X X X X X   X  X          G X
 X X X XXXX X X X X X X X XX X X   X   XG X
 X   X  XX  X   X   X   X  X   X   X   XG X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123
++++++++++++++++++++++++++++++++++++++++++++
 x   x  xx  x   x   x   x  x   x   x   x  x+
 x x x xxxx x x x x x x x xx x x C x C x Cx+
 x x x xxxx x x x x x x x xx x x C x C x Cx+
 x x x xxxx x x x x x x x xx x x C x C x Cx+
 x xxxxxxxxxxxxxxxxxxxxxxxxxxx CCCCCCCCCCCx+
   O   O  O   O   O   O        C
   O   OOOO   O   O   O CCCCCCCC      IIxI
   O   O  O   O   O   O        C
   O   O  O   O   O   OOOOOOOO CCCCCCCCCCC
 x x x xxxx x x x x x x   x  x   C   C   Cx-
 x x x xxxx x x x x x x x xx x x C x C x Cx-
 x   x  xx  x   x   x   x  x   x   x   x  x-
--------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123














```
