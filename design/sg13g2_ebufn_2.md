# Design Documentation for sg13g2_ebufn_2

## Substrate
```
  0123456789012345678
5 NNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678
5
4  ppppppppppppppppp
3  ppppppppppppppppp
2  ppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678
5
4            G GG G
3            G GG G
2            G GG G
1            G GG G
0            G GG G
9            G GG G
8            G GG G
7            G GG G
6            GGGGGG
5            G GG G
4            G GG G
3            G GG G
2            G GG G
1            G GG G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678
5 +++++++++++++++++++
4
3
2  CCCCC    C
1  C   CCCCCC     CC
0  C O C   CCCCCCCCC
9    O C   C      CC
8    O     C CC   CC
7    O     C C     C
6    OCCCCCC CxI x C
5    x       CII I C
4  C x CCCCC CC    C
3  C x C   C  C   CC
2  CCCCC   C  C   CC
1
0 -------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678
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
