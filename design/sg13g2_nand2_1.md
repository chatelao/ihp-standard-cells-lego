# Design Documentation for sg13g2_nand2_1

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


XppppX
XppppX
XpXXpX
X XX X
X XX X


 X   X

nnnnnn
nnnnnn
XnnnnX
Xnnnnn
Xnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


XG   X
XG   X
XGXX X
XGXX X
XGXX X
 G   G
 G   G
 X   X
 G   G
 G   G
 G   G
XG   X
XG   G
XG   G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++
x    x
x    x
x xx x
x xx x
x xx x
+ OO +
  OO
IxOOIx
IIOOII
  OO
- OOOO
x    x
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
