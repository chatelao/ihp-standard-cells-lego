# Design Documentation for sg13g2_xnor2_1

## Substrate
```
01234567890123
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123

 XppppXpppppX
 XppppXpppXpX
 XppppXpppXpX
 X        X
      X   XXX
     X   X
     XX  X
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 XnnnnnnnnnnX
 XnnnnnnnnnnX
 XnnnnnnXnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123

 X    X  G  X
 X    X  GX X
 X    X  GX X
 X    G  GX
      X  GXXX
     XG  X
     XX  X
      G  G
      G  G
 X    G  G  X
 X    G  G  X
 X    G XG

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
 x    x     x
 x    x   x x
 x  C x   x x
 x CC     x
   C IxII xxx
   C x   x   O
   C xxI x C O
   C       C O
 - CCCCCCCCC O
 x CC CCCCC xO
 x          xO
 x      x
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123














```
