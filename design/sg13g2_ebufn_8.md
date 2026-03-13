# Design Documentation for sg13g2_ebufn_8

## Substrate
```
01234567890123456789012345678901234567890123
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123

 pppppppppppppppppXppXpppXpppXpppppppppXppp
 pppppppppppppppppXppXpppXpppppppppppppXppp
 pXpppXpppXpppXpppppppppppppppppppppppppppp
  X   X   X   X
  XXXXXXXXXXXXX

                                     X  X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nXnnnXnnnXnnnXnnnXnnnXnnXnnnXnnnnnnnnnXnnn
 nnnnnnnnnnnnnnnnnXnnnXnnXnnnXnnnnnnnnnXnnn
 nnnnnnnnnnnnnnnnnXnnnXnnXnnnXnnnnnnnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123

                  X  X   X   X       G XG
                  X  X   X           G XG
  X   X   X   X                      G  G
  X   X   X   X                      G  G
  XXXXXXXXXXXXX                      G  G
                                     G  G
                                     X  X
                                     G  G
                                     G  G
  X   X   X   X   X   X  X   X       G XG
                  X   X  X   X       G XG
                  X   X  X   X       G XG

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123
++++++++++++++++++++++++++++++++++++++++++++
 CCCCCCCCCCCCCCCC x  x   x   x         x   +
 C  C   C   C   C x Cx C x C   C       x C +
 Cx C x C x C x CCCCCCCCCCCCCCCC CCCCCCCCC +
 Cx   x   x   x                  C       C
 Cxxxxxxxxxxxxx CCCCCCCCCCCCCCCCCCCCCC   CCC
   O            C                 C        C
   O  CCCCCCCCCCC CCCCCCCCCCCCCC  C IxI xI C
   O            CCCCC   C  C   C  C        C
 COOOOOOOOOOOOO C   C - C- C - C  C  C - CCC
 Cx C x C x C x C x C x Cx C x C  C  C x C
 CCCCCCCCCCCCCCCC x   x  x   x   CCCCC x C -
                  x   x  x   x         x   -
--------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123














```
