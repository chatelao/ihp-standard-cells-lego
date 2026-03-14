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
1  pppppppppX
0
9
8
7
6     X  X
5  nnnnnnnnnn
4  nnnnnnnnXX
3  nnnnXnnnXn
2  nnXnnnnnnn
1  nnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3     GG G
2     GG G
1     GG G  X
0     GG G
9     GG G
8     GG G
7     GG G
6     XG X
5     GG G
4     GG G XX
3     GX G X
2    XGG G
1     GG G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

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
