# Design Documentation for sg13g2_and3_1

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4
3  pppppppppp
2  pppppppppp
1  pppppppppp
0
9
8
7
6
5  nnnnnnnnnn
4  nnnnnnnnnn
3  nnnnnnnnnn
2  nnnnnnnnnn
1  nnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3    GGG G
2    GGG G
1    GGG G
0    GGG G
9    GGG G
8    GGG G
7    GGG G
6    GGG G
5    GGG G
4    GGG G
3    GGG G
2    GGG G
1    GGG G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 ++++++++++++
3
2
1   C  C    xO
0   C  C    OO
9   C  C    OO
8   CCCCCCC OO
7   C     C  O
6   C xI xCC O
5   C II I   O
4   C      xxO
3      x   x
2  IIxII
1
0 ------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901
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
