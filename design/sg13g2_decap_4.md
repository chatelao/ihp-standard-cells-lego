# Design Documentation for sg13g2_decap_4

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


XppXXX
XppXXX
XppXXX
X  XXX
X  XXX




nnnnnn
nnnnnn
XXXnnX
XXXnnX
XXXnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345


X  XXX
X  XXX
X  XXX
X  XXX
X  XXX






XXX  X
XXX  X
XXX  X


```
Legend: X=Connection (lower side)

## Metal 1
```
012345
++++++
++++++
x  xxx
x  xxx
x  xxx
x  xxx
x  xxx
+  +++
   ++
 --++
 --++
 --
 --
xxx  x
xxx  x
xxx  x
------
------
```
Legend: +=VDD, -=VSS, x=Connection (upper side)

## Metal 2
```
012345


















```
