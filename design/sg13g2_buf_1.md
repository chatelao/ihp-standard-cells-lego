# Design Documentation for sg13g2_buf_1

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


ppXppp
ppXppp
ppXpXX
    XX
    XX

 X


nnnnnn
nnnnnn
nnXnXX
nnXnXX
nnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


 GX
 GX
 GX XX
 G  XX
 G  XX
 G
 X
 G
 G
 G
 G
 GX XX
 GX XX
 GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++
  x
  x
C x xx
C   xx
CCCCxx
   COO
Ix COO
   C O
   C O
CCCC O
C   OO
  x xx
  x xx
  x
------
------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345


















```
