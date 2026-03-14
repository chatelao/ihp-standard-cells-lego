# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4
3  ppppppppppppppppppppppppp
2  ppppppppppppppppppppppppp
1  ppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
4
3      G           GG
2      G           GG
1      G           GG
0      G           GG
9      G           GG
8      G           GG
7      G           GG
6      G           GG
5      G           GG
4      G           GG
3      G           GG
2      G           GG
1      G           GG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 +++++++++++++++++++++++++++
3
2
1  C                      x
0  C    CCC   CCCCC  C    O
9  C CCCCCCCCCC   C  C    O
8  C C   C    C C CI CCC  O
7  C C x C C  CCC Cx   C  O
6  CCC I C C  CCC CIx  CC O
5  C CCCCC CCCCCC C    C  x
4  CCCC C       C     CC  x
3  C   CCCC     C     CC  x
2  C   CCCCCCC            x
1
0 ---------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456
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
