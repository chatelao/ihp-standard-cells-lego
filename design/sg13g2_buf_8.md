# Design Documentation for sg13g2_buf_8

## Substrate
```
0123456789012345678901234

NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234


ppXpppXpppXppppXpppXpppX
ppXpppXpppXppppXpppXpppX
ppXpppXpXpXpXppXpXpXpXpX
  X   X X X X  X X X X X
        X   X    X   X X


   X

nnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnn
nnXnnnXnXnXnXnnXnXnXnXnX
nnXnnnXnnnXnnnnXnnnXnnnX
nnXnnnXnnnXnnnnXnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234


  XG  X   X    X   X   X
  XG  X   X    X   X   X
  XG  X X X X  X X X X X
  XG  X X X X  X X X X X
   G    X   X    X   X X
   G
   G
   X
   G
   G
   G
  XG  X X X X  X X X X X
  XG  X   X    X   X   X
  XG  X   X    X   X   X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234
+++++++++++++++++++++++++
+++++++++++++++++++++++++
  x   x   x    x   x   x
  x   x   x    x   x   x
C x C x x x x  x x x x x
C x C x x x x  x x x x x
C   C   x   x    x   x x
CCCCCCC OOOOOOOOOOOOOO +
      C              O
 IIxI CCCCCCCCCCCCCC OOO
 IIII CCCCCCCCCCCCCC OOO
      C              O
CCCCCCC OOOOOOOOOOOOOO -
C x C x x x x  x x x x x
  x   x   x    x   x   x
  x   x   x    x   x   x
-------------------------
-------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234


















```
