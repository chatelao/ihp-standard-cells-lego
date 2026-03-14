# Design Documentation for sg13g2_and4_1

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

 pXppXpppXppp
 pXppXpppXppX
 pXppXpppXppX
            X
            X

   X X X X
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 nnnnnnnnXnnX
 nnnnnnnnXnnX
 nnnnnnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123

  XG X G X
  XG X G X  X
  XG X G X  X
   G G G G  X
   G G G G  X
   G G G G
   X X X X
   G G G G
   G G G G
   G G G X  X
   G G G X  X
   G G G X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
  x  x   x
  xC x C x  xO
  xC x C x  xO
   C   C    xO
 CCCCCCCCCCCxO
 C         C O
 C x x x x C O
 C I I I I   O
 C           O
 CC      x  xO
 CC      x  xO
         x
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123














```
