# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
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
4
3  pppppppppppppp
2  pppppppppppppp
1  pppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnn
4  nnnnnnnnnnnnnn
3  nnnnnnnnnnnnnn
2  nnnnnnnnnnnnnn
1  nnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3   G
2   G
1   G
0   G
9   G
8   G
7   G
6   G
5   G
4   G
3   G
2   G
1   G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 ++++++++++++++++
3
2
1       C       x
0  C    C C     O
9  CCCC C C     O
8     C C CCCC  O
7  II C C     C O
6  Ix C CCCCC C O
5  II C C     C x
4  CCCC C CCCCCxx
3  C    C      xx
2       C      xx
1
0 ----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345
4
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
