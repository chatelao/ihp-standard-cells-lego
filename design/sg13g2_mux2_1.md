# Design Documentation for sg13g2_mux2_1

## Substrate
```
012345678901234567
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567

 pppXppppppppXppp
 pppXppppppppXpXX
 pppXppppppppXpXX
             X XX
             X XX

  X     X
 nnnnnXnnnXnnnnnn
 nnnnnnnXnnnnnnnn
 nnXnnnnnnnnnnnnX
 nnXnnnnnnnnnXnnX
 nnXnnnnnnnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567

  G X   G G  X
  G X   G G  X XX
  G X   G G  X XX
  G     G G  X XX
  G     G G  X XX
  G     G G
  X     X G
  G   X G X
  G     X G
  GX    G G     X
  GX    G G  X  X
  GX    G G  X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567
++++++++++++++++++
    x CCCCCCCx
    x C     Cx xx
 C  x C CC  Cx xx
 CCCCCCCCC  Cx xx
 C   CCC    Cx xx
 C   C      C   O
 CxI C  x I CC CO
 C   Cx I x    CO
 C   CIIxII CCCCO
 C x C      C   x
   x CCCCCCCCx  x
   x         x
------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567














```
