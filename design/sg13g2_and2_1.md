# Design Documentation for sg13g2_and2_1

## Substrate
```
0123456789

NNNNNNNNNN
NNNNNNNNNN
NNNNNNNNNN
NNNNNNNNNN
NNNNNNNNNN
NNNNNNNNNN
NNNNNNNNNN
NNNNNNNNNN
SSSSSSSSSS
SSSSSSSSSS
SSSSSSSSSS
SSSSSSSSSS
SSSSSSSSSS
SSSSSSSSSS
SSSSSSSSSS
SSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789


 XpppXppp
 XpppXppp
 XpppXpXX
 X   X XX
       XX


    X

 nnnnnnnn
 nnnnnnnn
 XnnnXnXX
 nnnnXnnn
 nnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789


 X  GX
 X  GX
 X  GX XX
 X  GX XX
 G  G  XX
 G  G
 G  G
 G  X
 G  G
 G  G
 G  G
 X  GX XX
 G  GX
 G  GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789
++++++++++
++++++++++
 x   x
 x   x
 x C x xxO
 x C x xxO
   C   xxO
 CCCCC OOO
 C    C OO
 C Ix C OO
 C II   OO
 C     OOO
     - OOO
IxI  x xxO
III  x
     x
----------
----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789


















```
