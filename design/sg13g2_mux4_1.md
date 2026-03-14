# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456789
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789
5
4  pppppppppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789
5
4    G G       G G        G         G
3    G G       G G        G         G
2    G G       G G        G         G
1    G G       G G        G         G
0    G G       G G        G         G
9    G G       G G        G         G
8    G G       G G        G         G
7    G G       G G        G         G
6    G G       G G        G         G
5    G G       G G        G         G
4    G G       G G        G         G
3    G G       G G        G         G
2    G G       G G        G         G
1    G G       G G        G         G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789
5 ++++++++++++++++++++++++++++++++++++++++
4
3
2                 CCCCCCC   C CCCCCCCC
1  CC      CC     C CCC C   C C      C  O
0  CC      CCCCCCCC CCC CCCCC C C CC C  O
9  CC      CC       CCCCC   C C C CC CCCO
8  CC      CC  I I       C  C C C C   CCO
7  C x x   C   x x   CCC Cx C C CCC xICCO
6  C I I C C C I I C C   CI C C C C IICCO
5  C     C C C     C C   C  C C CCC     x
4  CCCCCCCCC CCCCCCCCCCCCCC C    CCCC   x
3  CC    CCC C        C   C CCCCCCCCC   x
2  CC    CCCCC      CCC   CCCCCCCC      x
1
0 ----------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456789
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
