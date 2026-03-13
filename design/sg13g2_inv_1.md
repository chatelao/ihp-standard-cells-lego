# Design Documentation for sg13g2_inv_1

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

 Xpp
 XpX
 XpX
 X X
 X X

 X
 nnn
 nnn
 XnX
 XnX
 Xnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234

 X
 X X
 X X
 X X
 X X
 G
 X
 G
 G
 X X
 X X
 X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234
+++++
 x
 x x
 x x
 x x
 x x
   O
 x O
   O
   O
 x x
 x x
 x
-----
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234














```
