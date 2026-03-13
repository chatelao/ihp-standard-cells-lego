# Design Documentation for sg13g2_decap_8

## Substrate
```
012345678901
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901

 XppXXXXppp
 XppXXXXppp
 XppXXXXppp
 X  XXXX
 X  XXXX


 nnnnnnnnnn
 nnnnnnnnnn
 XXnnnXnnnX
 XXnnnXnnnX
 XXnnnXnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901

 X  XXXX
 X  XXXX
 X  XXXX
 X  XXXX
 X  XXXX




 XX   X   X
 XX   X   X
 XX   X   X

```
Legend: X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
 x  xxxx   +
 x  xxxx   +
 x  xxxx   +
 x  xxxx   +
 x  xxxx   +
    ++++
  - ++++  -
  - ++++  -
  -       -
 xx   x   x-
 xx   x   x-
 xx   x   x-
------------
```
Legend: +=VDD, -=VSS, x=Connection (upper side)

## Metal 2
```
012345678901














```
