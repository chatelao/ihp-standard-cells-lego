# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901234
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234
5
4  ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3  ppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234
5
4  G       G                G
3  G       G                G
2  G       G                G
1  G       G                G
0  G       G                G
9  G       G                G
8  G       G                G
7  G       G                G
6  G       G                G
5  G       G                G
4  G       G                G
3  G       G                G
2  G       G                G
1  G       G                G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234
5 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
4
3
2    CCCCCCCC  CCCCC CCCCCCCCCCCCCCCCCCCCC
1    C     CC  C   C                           O  C   OO
0    C CCC CCCCC C C    CCCCCCCCCCC            O  C   OO
9    C C   C     C C CCCC        CC CC    C    O  C   OO
8    C CCCCCCCCCCC C  CCC CCCCCC CC  C CCCCCCC O  C   OO
7  I C CC IxI C  C C  CC  C      CC  C C     C O  C    O
6  x C C  III C  C CCCCC CC xICCCCCC C       C O  CCCC O
5  I C CCCCCCCCCCCCC CCC  C   C   CCCCCCCCCC C xx C    x
4  I C   C   C       CCCC CCCCC C           CC xx C   xx
3    C   C   CCCCCCCCC        C CCCCCCC    CC  x  C   xx
2  CCC       CCCCCCCCCCCCCCCCCCCCCCCC C    CC  x  C   xx
1
0 -------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456789012345678901234
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
