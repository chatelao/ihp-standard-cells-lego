# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  012345678901234567890123456789012345678901234567890123456789012345678901
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567890123456789012345678901
5
4  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678901234567890123456789012345678901
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
  012345678901234567890123456789012345678901234567890123456789012345678901
5 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
4
3
2       CCCCCCCC  CC    CCCCCCCC   CCCC CCCCCCCCCCCCCCCCCCCCC            O
1       C  C   C  CC    C CCC CC   C  C                          O   C   O
0  CCCCCC  C   C  CC    C CCC CCCCCCC C    CCCCCCCCCCC           O   C   O
9  C     CCC   C  CC    C C   C     C C  CCC        CC C    C    O   C   O
8  C   CCC     C  CC    C CCCCCCCCCCC C   CC CCCCCC CC CCCCCCCCC O   C   O
7  C   C  xI I C   C    C CC  xI C  C C   C  CIII   CC  CC     C O   C   O
6  CxI CxIII x CC CCCCC C C   II C  C CCC CCCCIxI CCCCC C    C C O   C  OO
5  C   C x   I    CC    C CCCCCCCCCCCCC C C  CIII C  CCCCCCCCC C xxx C   O
4  C   C IIxII CCCCC    C   C   C       C C  C    CC           C xxx C   O
3  C   C       C   C  CCC   C   C CCCCCCC    CCCC CCCCCCCC    CC x   C   O
2      CCCCCCCCC   C            CCCCCCCCCCCCCCCCCCCCCCCC C    CC x   C   O
1
0 ------------------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678901234567890123456789012345678901
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
