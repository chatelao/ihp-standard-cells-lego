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

 pppXpppXpppX
 pppXpXpXpXpX
 pppXpXpXpXpX
    X X   X X
    X XXXXX X

 X      X
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 nnnnnXnnnnnn
 nnnnnXnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123

G G X  GXG  X
G G X XGXGX X
G G X XGXGX X
G G X XG GX X
G G X XXXXX X
G G    G G
GXG    GXG
G G    G G
G G    G G
G G    G G
G G   XG G
G G   XG G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
+   x   x   x
+   x x x x x
+ C x x x x x
+ C x x   x x
+ CCx xxxxx x
   C      O
 x CC   xIO
 I C      O
- CCCCCCC O
-   C   C   C
-   C x CCCCC
-     x
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123














```
