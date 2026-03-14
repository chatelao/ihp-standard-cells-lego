# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3   G   G G G               G               G
2   G   G G G               G               G
1   G   G G G               G               G
0   G   G G G               G               G
9   G   G G G               G               G
8   G   G G G               G               G
7   G   G G G               G               G
6   G   G G G               G               G
5   G   G G G               G               G
4   G   G G G               G               G
3   G   G G G               G               G
2   G   G G G               G               G
1   G   G G G               G               G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3
2       CCCCCCC
1       C     C  CC    CCCCCCC   CCCC CCCCCCCCCCCCCCCCCCCC          x
0  C    C CC  C  CC    CCCC CC   C  C   CCCCCCCCCC          O   C   O
9  CCCCCCCCC  C  CC    CC   CCCCCCC C   C         C         O   C   O
8  C   CCC    C  CC   CCC CCCCCCCCC C CCC CCCCCCC CCC CCCCCCO   C   O
7  C   C      C   C    CC C       C C  C  C     C C C C    CO   C   O
6  CxI C  x I CC CC    CC C xI C  C C  C CCIxICCC CCC C    CO   CC OO
5  C   Cx I x    CCCCC CC      CC   CC C  CIIIC     CCCCCC Cx   C   x
4  C   CIIxII CCCCC    CCCCCCCCC CCCCC C  C   C CCCCC      Cxxx C   x
3  C   C      C   C    C  C   C CCCCCC    CCCCC CCCCCC     Cx   C   x
2      CCCCCCCC   C  CCC      CCCCCCCCCCCCCCCCCCCCCC C    CCx   C   x
1
0 --------------------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012345678901234567
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
