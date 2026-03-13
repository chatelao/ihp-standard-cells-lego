# Design Documentation for sg13g2_decap_8

## Substrate
```
0123456789012

NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
NNNNNNNNNNNNN
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS
SSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012


XpppXXXXpppX
XpppXXXXpppX
XpppXXXXpppX
X   XXXX   X
X   XXXX   X




nnnnnnnnnnnn
nnnnnnnnnnnn
XXnnnXXnnnXX
XXnnnXXnnnXX
XXnnnXXnnnXX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012


X   XXXX   X
X   XXXX   X
X   XXXX   X
X   XXXX   X
X   XXXX   X






XX   XX   XX
XX   XX   XX
XX   XX   XX


```
Legend: X=Connection (lower side)

## Metal 1
```
0123456789012
+++++++++++++
+++++++++++++
x   xxxx   x
x   xxxx   x
x   xxxx   x
x   xxxx   x
x   xxxx   x
+   ++++   +
    ++++
 -  ++++  -
 -  ++++  -
 -        -
 -        -
xx   xx   xx
xx   xx   xx
xx   xx   xx
-------------
-------------
```
Legend: +=VDD, -=VSS, x=Connection (upper side)

## Metal 2
```
0123456789012


















```
