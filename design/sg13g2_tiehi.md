# Design Documentation for sg13g2_tiehi

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


Xppppp
Xppppp
pppppp
    XX
    XX




nnnnnn
nnnnnn
nnnnnn
nnXnnn
nnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


X
X

    XX
    XX







  X
  X


```
Legend: X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++
x
x

    xx
    xx
C   OO
CCCC
   CCC
C  CCC
C   CC
C   CC

  x
  x
------
------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345


















```
