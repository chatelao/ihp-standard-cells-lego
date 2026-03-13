# Design Documentation for sg13g2_decap_4

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

 XppXX
 XppXX
 XppXX
 X  XX
 X  XX


 nnnnn
 nnnnn
 nXnnn
 XXnnn
 XXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456

 X  XX
 X  XX
 X  XX
 X  XX
 X  XX




  X
 XX
 XX

```
Legend: X=Connection (lower side)

## Metal 1
```
0123456
+++++++
+x  xx+
+x  xx+
+x  xx+
+x  xx+
+x  xx+
    +
  - +
  - +
  -
  x
-xx   -
-xx   -
-------
```
Legend: +=VDD, -=VSS, x=Connection (upper side)

## Metal 2
```
0123456














```
