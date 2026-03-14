# Design Documentation for sg13g2_and3_1

## Substrate
```
  0123456789012
5 NNNNNNNNNNNNN
4 NNNNNNNNNNNNN
3 NNNNNNNNNNNNN
2 NNNNNNNNNNNNN
1 NNNNNNNNNNNNN
0 NNNNNNNNNNNNN
9 NNNNNNNNNNNNN
8 NNNNNNNNNNNNN
7 SSSSSSSSSSSSS
6 SSSSSSSSSSSSS
5 SSSSSSSSSSSSS
4 SSSSSSSSSSSSS
3 SSSSSSSSSSSSS
2 SSSSSSSSSSSSS
1 SSSSSSSSSSSSS
0 SSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012
5
4  ppppppppppp
3  ppppppppppp
2  ppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnn
4  nnnnnnnnnnn
3  nnnnnnnnnnn
2  nnnnnnnnnnn
1  nnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012
5
4     GG G
3     GG G
2     GG G
1     GG G
0     GG G
9     GG G
8     GG G
7     GG G
6     GG G
5     GG G
4     GG G
3     GG G
2     GG G
1     GG G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012
5 +++++++++++++
4
3
2   C   C    xO
1   C   C    OO
0   C   C    OO
9   CCCCCCCC OO
8   C      C  O
7   C xI x C  O
6   C II I C  O
5   C       xxO
4   C       xxO
3      x    x
2  IIxII
1
0 -------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012
5
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
