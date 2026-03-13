# Design Documentation for sg13g2_sighold

## Substrate
```
012345678

NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678


pXXXXXXp
pXXXXXXp
pppppppp






nnnnnnnn
nnnnnnnn
nnnnnnnn
nnnnnnnn
nXXXXXXn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678


 XXXXXX
 XXXXXX











 XXXXXX


```
Legend: X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
+++++++++
 xxxxxx
 xxxxxx



C      C
C      C
CCCCCCCC
CCCC   C
C      C
C      C


 xxxxxx
---------
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, x=Connection (upper side)

## Metal 2
```
012345678


















```
