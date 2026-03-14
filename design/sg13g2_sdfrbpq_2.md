# Design Documentation for sg13g2_sdfrbpq_2

## Substrate
```
  012345678901234567890123456789012345678901234567890123456789012345678
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567890123456789012345678
5
4  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1
0
9
8
7         X                   X
6   X   X    X                                 X
5  nnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnn
4  nnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678901234567890123456789012345678
5
4  G G   G GG G              G G              G G
3  G G   G GG G              G G              G G
2  G G   G GG G              G G              G G
1  G G   G GG G              G G              G G
0  G G   G GG G              G G              G G
9  G G   G GG G              G G              G G
8  G G   G GG G              G G              G G
7  G G   GXGG G              GXG              G G
6  GXG  XG GGXG              G G              GXG
5  G G   X GG G              G G              G G                 XX
4  G G   G XG G              G G              G G                 XX
3  G G   G GG G              G G              G G                 X
2  G G   G GG G              G G              G G                 X
1  G G   G GG G              G G              G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789012345678901234567890123456789012345678
5 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
4
3
2       CCCCCCCC  CC    CCCCCCCC   CCCC CCCCCCCCCCCCCCCCCCCCC
1       C  C   C  CC    C CCC CC   C  C                          O
0  CCCCCC  C   C  CC    C CCC CCCCCCC C    CCCCCCCCCCC           O
9  C     CCC   C  CC    C C   C     C C  CCC        CC C    C    O
8  C   CCC     C  CC    C CCCCCCCCCCC C   CC CCCCCC CC CCCCCCCCC O
7  C   C  xI I C   C    C CC  xI C  C C   C  CIII   CC  CC     C O
6  CxI CxIII x CC CCCCC C C   II C  C CCC CCCCIxI CCCCC C    C C OOO
5  C   C x   I    CC    C CCCCCCCCCCCCC C C  CIII C  CCCCCCCCC C  xx
4  C   C IIxII CCCCC    C   C   C       C C  C    CC           C  xx
3  C   C       C   C  CCC   C   C CCCCCCC    CCCC CCCCCCCC    CC  x
2      CCCCCCCCC   C            CCCCCCCCCCCCCCCCCCCCCCCC C    CC  x
1
0 ---------------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678901234567890123456789012345678
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
