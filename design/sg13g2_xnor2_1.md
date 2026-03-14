# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4
3  pppppppppppp
2  pppppppppppp
1  pppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2  nnnnnnnnnnnn
1  nnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
4
3      GG GG
2      GG GG
1      GG GG
0      GG GG
9      GG GG
8      GG GG
7      GG GG
6      GG GG
5      GG GG
4      GG GG
3      GG GG
2      GG GG
1      GG GG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 ++++++++++++++
3
2
1           x
0     C     O
9    CC     O
8    C IxII OOO
7    C x   x   O
6    C xxI x C O
5    C       C O
4    CCCCCCCCC O
3    CC CCCCC xO
2             xO
1
0 --------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123
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
