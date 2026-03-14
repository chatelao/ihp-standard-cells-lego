# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4
3  pppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppp
1  pppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
4
3    G G                 G
2    G G                 G
1    G G                 G
0    G G                 G
9    G G                 G
8    G G                 G
7    G G                 G
6    G G                 G
5    G G                 G
4    G G                 G
3    G G                 G
2    G G                 G
1    G G                 G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++
3
2              CCCC
1  C   CCCC    C  C               o
0  C   C  CCCC CC C     C   O C   O
9  CCCCCCCCCCC CC C     C   O C   O
8  C     C  CC CC C CCCCC   O C   O
7  C i i CC CC CCCCCC  CCCCCOOC   O
6  C I I CCCCC C   CCC C i C OCCCCO
5  C     CCCCCCC CCCCC C I   oC   o
4  C    CCCCCCCCCCCC  CC    ooC   o
3  C    CCC        C  CC    o C   o
2       CCC     CCCC  CC    o     o
1
0 ----------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, i=Metal 1 Input Connection, o=Metal 1 Output Connection

## Metal 2
```
  0123456789012345678901234567890123
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
