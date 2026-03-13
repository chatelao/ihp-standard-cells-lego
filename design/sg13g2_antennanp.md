# Design Documentation for sg13g2_antennanp

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


 pppp
 pppp
 pppp

  X

  X


 nnnn
 nnnn
 nXnn
 nnnn
 nnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


  G
  G
  G
  G
  X
  G
  X
  G
  G
  G
  G
  X
  G
  G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++




  xI
  II
  x
  I
  I
  I
  II
  xI
  II

------
------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, x=Connection (upper side)

## Metal 2
```
012345


















```
