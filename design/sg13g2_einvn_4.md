# Design Documentation for sg13g2_einvn_4

## Substrate
```
01234567890123456789012
NNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012

 XppppppXppXpppppppppp
 XppppppXppXpppppppppp
 XppppppXppXpppppppppp
 X      X  X   X   X
 X      X  X   XXXXX

  X               X
 nnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnn
 XnnnnnnXnnnXnnnnnnnXn
 XnnnnnnXnnnXnnnnnnnnn
 XnnnnnnXnnnXnnnnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012

 XG     X  X      G
 XG     X  X      G
 XG     X  X      G
 XG     X  X   X  GX
 XG     X  X   XXXXX
  G               G
  X               X
  G               G
  G               G
 XG     X   X     G X
 XG     X   X     G
 XG     X   X     G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012
+++++++++++++++++++++++
 x      x  x CCCCCCCCC
 x C  C xC x C   C   C
 x C  C xC x C   C   C
 x C  C xC x C x C x C
 x C  C xC x C xxxxx C
   C  CCCCCCCC OO
 IxC            OIxII
 IIC   CCCCCCCC O
   C   C  C   C OOOOO
 x CCC Cx C x C     x C
 x CCC Cx C x CCCCCCCCC
 x      x   x
-----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012














```
