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

 XpppXppXpppX
 XpXpXpXXpppX
 XpXpXpXXpppX
 X X X XX
 X X   XX

          X
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 XnXnnnXnnnnn
 XnXnXnXnXXnn
 XnnnXnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123

 X   X  X G X
 X X X XX G X
 X X X XX G X
 X X X XX G
 X X   XX G
          G
          X
          G
          G
 X X   X  G
 X X X X XX
 X   X   XG

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
 x   x  x   x
 x x x xx   x
 x x x xx   x
 x x x xx C
 x x   xx CCCC
   OOOOO     C
 OOO  CCC xI C
   O    C II C
   OOOOOCCCCCC
 x x   x    CC
 x x x x xx CC
 x   x   x
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123














```
