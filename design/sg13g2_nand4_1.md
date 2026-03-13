# Design Documentation for sg13g2_nand4_1

## Substrate
```
01234567890
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890

 XpppXpppX
 XpXpXpXpX
 XpXpXpXpX
 X X   X
 X XXXXXXX

 X X X X
 nnnnXnnnn
 nnnnXnXnn
 XnnnnnXnX
 XnnnnnnnX
 Xnnnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890

 X G X G X
 X X X X X
 X X X X X
 X X G X
 X XXXXXXX
 G G G G
 X X X X
 G G X G
 G G X X
 X G G X X
 X G G G X
 X G G G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
 x   x   x
 x x x x x
 x x x x x
 x x   x
 x xxxxxxx
         O
 x x x x O
     x I O
 -   x x O
 x     x x
 x       x
 x
-----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890














```
