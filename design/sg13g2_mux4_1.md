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
3  ppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppp
1  ppppppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456
4
3    G G      G G       G         G
2    G G      G G       G         G
1    G G      G G       G         G
0    G G      G G       G         G
9    G G      G G       G         G
8    G G      G G       G         G
7    G G      G G       G         G
6    G G      G G       G         G
5    G G      G G       G         G
4    G G      G G       G         G
3    G G      G G       G         G
2    G G      G G       G         G
1    G G      G G       G         G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 +++++++++++++++++++++++++++++++++++++
3
2                CCCCCC     CCCCCCC
1                C     C  C C     C
0  CC     CC     C CCC C  C C     C   O
9  CC     CCCCCCCC CCC CCCC C C CCC   O
8  CC     CC       CCCCC  C C C CCCCC O
7  C      CC  I I      C  C C C C   C O
6  C i i  C   i i   CC CiIC C CCC i C O
5  C I ICCC C I I C C  C  C C CCC     O
4  CCCCCC C CCCCCCCCCCCCCCC C  CCC   oO
3  C    C C C        C   CCCCCCCCC   oO
2  C    CCCCC      CCC   CCCCCCC     oO
1
0 -------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, i=Metal 1 Input Connection, o=Metal 1 Output Connection

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
