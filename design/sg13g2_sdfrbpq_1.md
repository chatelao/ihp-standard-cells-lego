# Design Documentation for sg13g2_sdfrbpq_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123456
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123456
5
4  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123456
5
4   G     G  G                G                G
3   G     G  G                G                G
2   G     G  G                G                G
1   G     G  G                G                G
0   G     G  G                G                G
9   G     G  G                G                G
8   G     G  G                G                G
7   G     G  G                G                G
6   G     G  G                G                G
5   G     G  G                G                G
4   G     G  G                G                G
3   G     G  G                G                G
2   G     G  G                G                G
1   G     G  G                G                G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123456
5 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
4
3
2       CCCCCCCC  CC    CCCCCCCC   CCCC CCCCCCCCCCCCCCCCCCCCC
1       C  C   C  CC    C CCC CC   C  C                            O
0  CCCCCC  C   C  CC    C CCC CCCCCCC C    CCCCCCCCCCC             O
9  C     CCC   C  CC    C C   C     C C  CCC        CC C    C      O
8  C   CCC     C  CC    C CCCCCCCCCCC C   CC CCCCCC CC CCCCCCCCC   O
7  C   C  xI I C   C    C CC  xI C  C C   C  CIII   CC  CC     C   O
6  CxI CxIII x CC CCCCC C C   II C  C CCC CCCCIxI CCCCC C    C CC  O
5  C   C x   I    CC    C CCCCCCCCCCCCC C C  CIII C  CCCCCCCCC C  xx
4  C   C IIxII CCCCC    C   C   C       C C  C    CC           C  xx
3  C   C       C   C  CCC   C   C CCCCCCC    CCCC CCCCCCCC    CC   x
2      CCCCCCCCC   C            CCCCCCCCCCCCCCCCCCCCCCCC C    CC   x
1
0 -------------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456789012345678901234567890123456
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
