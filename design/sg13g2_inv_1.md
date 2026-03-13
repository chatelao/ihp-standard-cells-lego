# Design Documentation for sg13g2_inv_1

## Substrate
```
012345

NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
NNNNNN
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS
SSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345


 Xppp
 Xppp
 XppX
 X  X
 X  X


  X

 nnnn
 nnnn
 XnnX
 Xnnn
 Xnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


 XG
 XG
 XG X
 XG X
 XG X
  G
  G
  X
  G
  G
  G
 XG X
 XG
 XG


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++
 x
 x
 x  x
 x  x
 x  x
 +  O
    O
 Ix O
 II O
    O
 -  O
 x  x
 x
 x
------
------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345


















```
