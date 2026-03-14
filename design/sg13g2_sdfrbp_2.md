# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123456789012345
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123456789012345
5
4  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppXppp
1
0
9
8
7         X                   X
6   X   X    X                                 X
5  nnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnnnXXX
4  nnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnnnXXX
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnnXnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnnXnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123456789012345
5
4  G G   G GG G              G G              G G
3  G G   G GG G              G G              G G
2  G G   G GG G              G G              G G                        X
1  G G   G GG G              G G              G G
0  G G   G GG G              G G              G G
9  G G   G GG G              G G              G G
8  G G   G GG G              G G              G G
7  G G   GXGG G              GXG              G G
6  GXG  XGGGGXG              GGG              GXG
5  G G   X GGGG              G G              G G                 XX      XXX
4  G G   G XG G              G G              G G                 XX      XXX
3  G G   G GG G              G G              G G                 X       X
2  G G   G GG G              G G              G G                 X       X
1  G G   G GG G              G G              G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123456789012345
5 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
4
3
2       CCCCCCCC  CC    CCCCCCCC   CCCC CCCCCCCCCCCCCCCCCCCCC            x
1       C  C   C  CC    C CCC CC   C  C                          O   C   O
0  CCCCCC  C   C  CC    C CCC CCCCCCC C    CCCCCCCCCCC           O   C   O
9  C     CCC   C  CC    C C   C     C C  CCC        CC C    C    O   C   O
8  C   CCC     C  CC    C CCCCCCCCCCC C   CC CCCCCC CC CCCCCCCCC O   C   O
7  C   C  xI I C   C    C CC  xI C  C C   C  CIII   CC  CC     C O   C   O
6  CxI CxIII x CC CCCCC C C   II C  C CCC CCCCIxI CCCCC C    C C OOO CCCCOO
5  C   C x   I    CC    C CCCCCCCCCCCCC C C  CIII C  CCCCCCCCC C  xx  C   xxx
4  C   C IIxII CCCCC    C   C   C       C C  C    CC           C  xx  C   xxx
3  C   C       C   C  CCC   C   C CCCCCCC    CCCC CCCCCCCC    CC  x   C   x
2      CCCCCCCCC   C            CCCCCCCCCCCCCCCCCCCCCCCC C    CC  x   C   x
1
0 ----------------------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456789012345678901234567890123456789012345
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
