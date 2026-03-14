# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4
3  pppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppp
1  pppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789
4
3  G  G                G
2  G  G                G
1  G  G                G
0  G  G                G
9  G  G                G
8  G  G                G
7  G  G                G
6  G  G                G
5  G  G                G
4  G  G                G
3  G  G                G
2  G  G                G
1  G  G                G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 ++++++++++++++++++++++++++++++
3
2
1      C            CCCCC     o
0      CCCCCCC C    C   C C   O
9       C    C C    C   CCC   O
8       C  C C CCCCCCCC  CC   O
7  i IiIC CCCC C    CC   CCC  O
6  I  CCC C CCCCCCC CC i C CCCO
5     C   CCC C     CC   C C  o
4     C  CC C C CCC CC    CC  o
3    CCCCCCCCCC C CCCC    CC  o
2          CCCCCC CCCC        o
1
0 ------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, i=Metal 1 Input Connection, o=Metal 1 Output Connection

## Metal 2
```
  012345678901234567890123456789
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
