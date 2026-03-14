# Design Documentation for sg13g2_tielo

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
 ppppp
 ppppp




 nnnnn
 nnnnn
 nnnnX
 nnnXX
 nXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456

  X








     X
    XX
  X

```
Legend: X=Connection (lower side)

## Metal 1
```
0123456
+++++++
  x

     C
 C   C
 C   C
   C C
   C C
   C C
 CCC O
     x
    xx
  x
-------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456














```
