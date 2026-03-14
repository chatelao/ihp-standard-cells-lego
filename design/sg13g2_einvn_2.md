# Design Documentation for sg13g2_einvn_2

## Substrate
```
0123456789012345
NNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345

 pXpppppXpppppp
 pXpppppXpppppp
 pXpppppXpppppp
            X
            X
  X

 nnnnnnnnnnnnnX
 nnnnnnnnnnnnnn
 nnnnnnnnnnnnnn
 nXnnnnnXnnnnnn
 nXnnnnnXnnnnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345

 GXG    X    G G
 GXG    X    G G
 GXG    X    G G
 G G        XG G
 G G        XG G
 GXG         G G
 GGG         G G
 G G         GXG
 G G         G G
 G G         G G
 GXG    X    G G
 GXG    X    G G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345
++++++++++++++++
  x     x CCCCC
  x C C x C   C
  x C C x C   C
    C C   C x C
 IIIC CCCCC x C
 IxIC       O
 IIICC      O
 IIIC       O x
    C CCCCC O I
    C C   C
  x C C x CCCCC
  x     x
----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345














```
