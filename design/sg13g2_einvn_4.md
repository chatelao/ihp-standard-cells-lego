# Design Documentation for sg13g2_einvn_4

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
6   X               X
5  nnnnnnnnnnnnnnnXnnnnn
4  nnnnnnnnnnnnnnnXXXXXn
3  nnnnnnnnnnnnnnnnnnnXn
2  nnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
4
3   G               G
2   G               G
1   G               G
0   G               G
9   G               G
8   G               G
7   G               G
6   X               X
5   G             X G
4   G             XXXXX
3   G               G X
2   G               G
1   G               G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012
4 +++++++++++++++++++++++
3
2              CCCCCCCCC
1    C  C  C   C   C   C
0    C  C  C   C   C   C
9    C  C  C   C O C O C
8    C  C  C   C OOOOO C
7    C  CCCCCCCC OO
6  IxC            OIxII
5  IIC   CCCCCCCC x
4    C   C  C   C xxxxx
3    CCC C  C   C     x C
2    CCC C  C   CCCCCCCCC
1
0 -----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
