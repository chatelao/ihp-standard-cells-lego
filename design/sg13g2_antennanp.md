# Design Documentation for sg13g2_antennanp

## Substrate
```
01234
NNNNN
NNNNN
NNNNN
NNNNN
NNNNN
NNNNN
SSSSS
SSSSS
SSSSS
SSSSS
SSSSS
SSSSS
SSSSS
SSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234

 ppp
 ppp
 ppp
  X

 X

 nnn
 nnn
 nXn
 nnn
 nnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234

  G
  G
  G
  X
  G
 XG
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
01234
+++++



 IxI
 III
 x
 I
 I
 I
  xI
  II

-----
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, x=Connection (upper side)

## Metal 2
```
01234














```
