# Design Documentation for sg13g2_nor2_1

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

 pXppp
 pXppX
 pXppX
  X  X
  XXXX

 X   X
 nnnnn
 nnnnn
 nXXnX
 nXXnX
 nXnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456

 GX  G
 GX  X
 GX  X
 GX  X
 GXXXX
 G   G
 X   X
 G   G
 G   G
 GXX X
 GXX X
 GX  X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456
+++++++
  x
  x  x
  x  x
  x  x
  xxxx
   O
 x O x
   O
   O
  xx x
  xx x
  x  x
-------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456














```
