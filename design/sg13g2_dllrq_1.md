# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
3
2  pppXpppppXpppppppXXXpppXpp
1  pppXpppppXpppppppXXXpppXpX
0  pppXpppppppppppppXXXpppXpX
9     X                     X
8     X                     X
7
6    X X                 X
5  nnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnXnX
2  nnnnnnnnnnnnnnnnnnXnnnnXnX
1  nnnXnnnnnXXXnnnnnnXnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567
3
2    GXG    X       XXX  GX
1    GXG    X       XXX  GX X
0    GXG            XXX  GX X
9    GXG                 G  X
8    GXG                 G  X
7    G G                 G
6    X X                 X
5    G G                 G
4    G G                 G
3    G G                 GX X
2    G G             X   GX X
1    GXG    XXX      X   GX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567
3 ++++++++++++++++++++++++++++
2     x     x       xxx   x
1     x     x       xxx   x xO
0  CC x CCCCCCCCCCC xxx C x xO
9  CC x CC        C     C   xO
8  CC x CCCC   CC C CCCCCCCCxO
7  C     C CCCCCCCCCCC C   C O
6  C x x C C  CC     C C x C O
5  C     C CCCCCCCC  CCC I C O
4  CC   CCCCCC       C C     O
3  CC       CC   CCCCC C  x xO
2  CCCCCCCCCCC   C   x C  x xO
1     x     xxx      x    x
0 ----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567
3
2
1
0
9
8
7
6
5
4
3
2
1
0
```
