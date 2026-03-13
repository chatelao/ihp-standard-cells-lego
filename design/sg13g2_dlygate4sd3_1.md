# Design Documentation for sg13g2_dlygate4sd3_1

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

 ppXppppppppXpp
 ppXppppppppXpX
 ppXppppppppXpX
              X
              X

  X
 nnnnnnnnnnnnnn
 nnnnnnnnnnnnnn
 nnnnnnnnnnnnXX
 nnXnnnnnnnnXXX
 nnXnnnnnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345

  GX        X
  GX        X X
  GX        X X
  G           X
  G           X
  G
  X
  G
  G
  G          XX
  GX        XXX
  GX        X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345
++++++++++++++++
   x        x
   x  C     x x
 C x  C C   x x
 CCCC C C     x
    C C CCCC  x
 II C C     C O
 Ix C CCCCC C O
 II C C     C O
 CCCC C CCCCCOO
 C    C      xx
   x  C     xxx
   x        x
----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345














```
