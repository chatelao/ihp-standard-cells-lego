# Design Documentation for sg13g2_buf_8

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

 pXpppXpppXpppXpppXppX
 pXpppXpXpXpXpXpXpXpXX
 pXpppXpXpXpXpXpXpXpXX
        X   X   X   XX
        XXXXXXXXXXXXXX

    X
 nnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnn
 nnnnnnnXnnnXnnnXnnnXX
 nXnnnXnXnXnXnXnXnXnXX
 nXnnnXnnnXnnnXnnnXnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012

  X G X   X   X   X  X
  X G X X X X X X X XX
  X G X X X X X X X XX
    G   X   X   X   XX
    G   XXXXXXXXXXXXXX
    G
    X
    G
    G
    G   X   X   X   XX
  X G X X X X X X X XX
  X G X   X   X   X  X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012
+++++++++++++++++++++++
  x   x   x   x   x  x
 Cx C x x x x x x x xx
 Cx C x x x x x x x xx
 C  C   x   x   x   xx
 CCCCCCCxxxxxxxxxxxxxx
       C            O
  IIxI CCCCCCCCCCC  OO
       C            O
 CCCCCCCOOOOOOOOOOOOO
 C  C   x   x   x   xx
 Cx C x x x x x x x xx
  x   x   x   x   x  x
-----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012














```
