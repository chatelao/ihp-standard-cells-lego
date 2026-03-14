# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  01234567890123456789012345678
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678
5
4  ppppppppppppppppppppppppppp
3  ppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678
5
4      G             G
3      G             G
2      G             G
1      G             G
0      G             G
9      G             G
8      G             G
7      G             G
6      G             G
5      G             G
4      G             G
3      G             G
2      G             G
1      G             G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678
5 +++++++++++++++++++++++++++++
4
3
2                           x
1  C    CCC   CCCCCC   C    O
0  C CCCC     C    C   C    O
9  C C    CCCCC CC C I CC   O
8  C C x  C   C  C C x  C   O
7  C C I  C C CC C C x  C   O
6  C C    C C    C C    CCC O
5  C CCCC C CCCCCC C    C   x
4  CCCCCCCCC     C      C   x
3  C   C         C      C   x
2  C   CCCCCCCC             x
1
0 -----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678
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
