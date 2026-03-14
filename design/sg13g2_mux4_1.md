# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4
3
2  ppppppppppppppppppppppppppppppppppp
1  ppppppppppppppppppppppppppppppppppp
0  ppppppppppppppppppppppppppppppppppp
9  ppppppppppppppppppppppppppppppppppp
8  ppppppppppppppppppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456
4
3   G G G G G G
2   G G G G G G
1   G G G G G G
0   G G G G G G
9   G G G G G G
8   G G G G G G
7   G G G G G G
6  GG GGG GGG GG
5   G G G G G G
4   G G G G G G
3   G G G G G G
2   G G G G G G
1   G G G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     +        + CCCCCCC+   CCCCCCC +
1  CC +        + C     C+ C C     C + O
0  CC +   CCCCCCCC CCC CCCC C C CCC + O
9  CC +   CC       CCCCC  C C C CCCCC O
8  CC +   CC           C  C C C C   C O
7  C      C         CC C  C C CCC   C O
6  i   iCCCiC  i  C C  C  C C C C   C O
5  C    C C C     C CCCCCCC C CCCC   OO
4  CCCCCC C CCCCCCCCCC   CCCCCCCCC - oO
3  C  - C   C  -   CCC - C     CCC - oO
2     - CCCCC  -       - CCCCCCC   -
1     -        -       -           -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456
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
Legend: M=Metal 2
