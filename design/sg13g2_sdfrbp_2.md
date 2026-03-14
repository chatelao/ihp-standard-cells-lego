# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3  G G   G G G             G G             G G
2  G G   G G G             G G             G G
1  G G   G G G             G G             G G
0  G G   G G G             G G             G G
9  G G   G G G             G G             G G
8  G G   G G G             G G             G G
7  G G   GGG G             GGG             G G
6  GGG   G GGG             G G             GGG
5  G G   G G G             G G             G G
4  G G   G G G             G G             G G
3  G G   G G G             G G             G G
2  G G   G G G             G G             G G
1  G G   G G G             G G             G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3     x        x     x         x                          x   x   x   x
2     x CCCCCCCx     x CCCCCCC x CCCC CCCCCCCCCCCCCCCCCCCCx   x   x   x
1     x C     Cx CC  x C     C x C  C                     x x x   x xxx
0  CCCCCC CC  C+ CC  + CCCC CCCCCCC C   CCCCCCCCCCC       + O + CC+ OO+
9  C     CCC  C+ CC  +CCC   C     C C   C       C CC    C   O + CC+ OO+
8  C   CCC    C+ CC    CC CCCCCCCCC C CCC CCCCCCC CCC CCCCCCO + CC+ OO+
7  C   C  x I C   C    CC C xI C  C C  C  CIII  C C C C    CO    C   O
6  CxI Cx I x CC CCCCC CC   II CC C CC C CCIxICCC CCC    C COOO  CCC OO
5  C   Cx   I    CC    CCCCCCCCCCCCCCC C  CIIIC  CCCCCCCCC C  x   C   xx
4  C x CIIxII CCCCC    C  C   C      C    CCCCC CCCCCC     C  x   C x xx
3  C x CCCCCCCCx  C  CCCx   x C CCCCCC        C      C x  CCx x x C x xx
2    x         x        x   x CCCCCCCCCCCCCCCCCCCCCC   x    x   x   x  x
1    x         x        x   x                          x    x   x   x  x
0 -----------------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012345678901234567890
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
