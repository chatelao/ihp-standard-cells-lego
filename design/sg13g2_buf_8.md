# Design Documentation for sg13g2_buf_8

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4
3  ppppppppppppppppppppp
2  ppppppppppppppppppppp
1  ppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
4
3     G
2     G
1     G
0     G
9     G
8     G
7     G
6     G
5     G
4     G
3     G
2     G
1     G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 +++++++++++++++++++++++
3
2
1  C  C   o   o   o   o
0  C  C   O   O   O   O
9  C  C   O   O   O   O
8  CCCCCCCOOOOOOOOOOOOO
7        C            O
6   IIiI CCCCCCCCCCC  OO
5        C            o
4  CCCCCCCooooooooooooo
3  C  C   o   o   o   o
2  C  C   o   o   o   o
1
0 -----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, i=Metal 1 Input Connection, o=Metal 1 Output Connection

## Metal 2
```
  01234567890123456789012
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
