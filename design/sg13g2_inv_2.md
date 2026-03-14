# Design Documentation for sg13g2_inv_2

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

 X
 nnnnn
 nnnnn
 XnXnX
 XnXnX
 XnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456

GXG  X
GXGX X
GXGX X
GXGX X
GXGX X
G G
GXG
G G
G G
GXGX X
GXGX X
GXG  X

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
 x OOO
   O
   O
 x x x
 x x x
 x   x
-------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456














```
