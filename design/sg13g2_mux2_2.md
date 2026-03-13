# Design Documentation for sg13g2_mux2_2

## Substrate
```
01234567890123456789
NNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789

 pppXppppppppXppppX
 pppXppppppppXpXXXX
 pppXppppppppXpXXXX
             X XXXX
             X XXXX

  X     X
 nnnnnXnnnXnnnnnnnn
 nnnnnnnXnnnnnnnnnn
 nnXnnnnnnnnnnnnXXX
 nnXnnnnnnnnnXnnXXX
 nnXnnnnnnnnnXnnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789

 G GX  G G G X    X
 G GX  G G G X XXXX
 G GX  G G G X XXXX
 G G   G G G X XXXX
 G G   G G G X XXXX
 G G   G G G
 GXG   GXG G
 G G  XG GXG
 G G   GXG G
 G X   G G G    XXX
 G X   G G G X  XXX
 G X   G G G X    X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789
++++++++++++++++++++
    x CCCCCCCx    x
    x C     Cx xxxx
 C  x C CC  Cx xxxx
 CCCCCCCCC  Cx xxxx
 C   CCC    Cx xxxx
 C   C      C    O
 CxI C  x I CC C O
 C   Cx I x    C O
 C   CIIxII CCCC O
 C x C      C   xxx
   x CCCCCCCCx  xxx
   x         x    x
--------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789














```
