# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  0123456789012345
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
3
2  ppXppppppppXpp
1  ppXppppppppXpX
0  ppXppppppppXpX
9               X
8               X
7
6   X
5  nnnnnnnnnnnnnn
4  nnnnnnnnnnnnnn
3  nnnnnnnnnnnnXX
2  nnXnnnnnnnnXXX
1  nnXnnnnnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
3
2   GX        X
1   GX        X X
0   GX        X X
9   G           X
8   G           X
7   G
6   X
5   G
4   G
3   G          XX
2   GX        XXX
1   GX        X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345
3 ++++++++++++++++
2    x        x
1    x  C     x x
0  C x  C C   x x
9  CCCC C C     x
8     C C CCCC  x
7  II C C     C O
6  Ix C CCCCC C O
5  II C C     C O
4  CCCC C CCCCCOO
3  C    C      xx
2    x  C     xxx
1    x        x
0 ----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345
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
