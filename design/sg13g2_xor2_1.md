# Design Documentation for sg13g2_xor2_1

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

 pXppppppXppp
 pXppppppXppp
 pXpppppppppp
  X
  X

  X     X
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 XXnnnnXnnXXn
 XXnnnnXnnXXX
 XXnnnnXnnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123

  X     GX
  X     GX
  X     G
  X     G
  X     G
  G     G
  X     X
  G     G
  G     G
 XX    XG XX
 XX    XG XXX
 XX    XG   X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
  x      x
  x  C C x C O
  x  C C   C O
  x  C CCCCC O
  x CCCCCCCCCO
    C       CO
 Ix C IIxII CO
    C        O
    C  -  OOOO
 xx C  x  xx
 xx    x  xxx
 xx    x    x
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123














```
