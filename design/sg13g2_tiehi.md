# Design Documentation for sg13g2_tiehi

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

 ppppp
 ppppp
 ppppX
     X
     X


 nnnnn
 nnnnn
 nnnnn
 nnXnn
 nnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456



     X
     X
     X





   X
   X

```
Legend: X=Connection (lower side)

## Metal 1
```
0123456
+++++++
+
+
     x
     x
CC   x
 CCC
   C C
C  C C
C    C

   x
   x
-------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, x=Connection (upper side)

## Metal 2
```
0123456














```
