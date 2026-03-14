# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  01234567890123456789012345678901
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
5
4  pppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901
5
4  G  G                 G
3  G  G                 G
2  G  G                 G
1  G  G                 G
0  G  G                 G
9  G  G                 G
8  G  G                 G
7  G  G                 G
6  G  G                 G
5  G  G                 G
4  G  G                 G
3  G  G                 G
2  G  G                 G
1  G  G                 G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
5 ++++++++++++++++++++++++++++++++
4
3
2                               x
1      C     C C     CCCCCC C   O
0      CCCCCCC C     C    C C   O
9        C   C C     C C  C C   O
8    IxI C C   C CCCCC C  C C   O
7  x     CCCCC C     C Cx C  C  O
6  I  CCCCC  C CCCCC C CI CC CCCO
5     C   C CC C     C C     C  x
4    CC  CC  C CCCCC CCC    CC  x
3    CCCCCCC CCCC  C  CC    CC  x
2            CCCC  CCCCC        x
1
0 --------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901
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
