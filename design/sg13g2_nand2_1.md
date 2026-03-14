# Design Documentation for sg13g2_nand2_1

## Substrate
```
0123456
NNNNNNN
NNNNNNN
NNNNNNN
NNNNNNN
NNNNNNN
NNNNNNN
SSSSSSS
SSSSSSS
SSSSSSS
SSSSSSS
SSSSSSS
SSSSSSS
SSSSSSS
SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
0123456

 XpppX
 XpXpX
 XpXpX
 X X X
 X X X

 X   X
 nnnnn
 nnnnn
 XnnnX
 XnnnX
 Xnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456

 X   X
 X X X
 X X X
 X X X
 X X X
 G   G
 X   X
 G   G
 G   G
 X   X
 X   X
 X   G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456
+++++++
 x   x
 x x x
 x x x
 x x x
 x x x
   O
 x O x
 I O I
 - OOO
 x   x
 x   x
 x
-------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456














```
