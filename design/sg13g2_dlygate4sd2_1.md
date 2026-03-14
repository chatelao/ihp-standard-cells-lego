# Design Documentation for sg13g2_dlygate4sd2_1

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
  01234567890123
4 ++++++++++++++
3
2
1              O
0  C    C C    O
9  C    C C    O
8  CCCC C CCCC O
7     C C    C O
6  Ix C CCC CC O
5  II C C   C  O
4  CCCC C CCCxxO
3  C    C      O
2  C    C      O
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
