# Design Documentation for sg13g2_buf_1

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

 ppXpp
 ppXpX
 ppppX
     X
     X
 X

 nnnnn
 nnnnn
 nnXnX
 nnXnX
 nnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456

 G X
 G X X
 G   X
 G   X
 G   X
 X
 G
 G
 G
 G X X
 G X X
 G X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456
+++++++
   x
 C x x
 C   x
 CCC x
   C x
 x C O
   CCO
 CCC O
 C   O
   x x
   x x
   x
-------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456














```
