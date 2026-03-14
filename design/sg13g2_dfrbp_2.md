# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4
3  ppppppppppppppppppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppppppppppppppppppp
1  ppppppppppppppppppppppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4 G G    G G             G G
3 G G    G G             G G
2 G G    G G             G G
1 G G    G G             G G
0 G G    G G             G G
9 G G    G G             G G
8 G G    G G             G G
7 G G    GGG             G G
6 GGG    G G             GGG
5 G G    G G             G G
4 G G    G G             G G
3 G G    G G             G G
2 G G    G G             G G
1 G G    G G             G G
0 G G    G G             G G
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 +++++++++++++++++++++++++++++++++++++++++++++++++++++
3  x         x                           x  x   x   x
2  x CCCCCCC x CCCC CCCCCCCCCCCCCCCCCCCC x  x   x   x
1  x C      Cx C  C                      x xx   x xxx
0  + CCCC C CCCCC C   CCCCCCCCCCC        + O+ CC+ OO+
9  + CC   C     C C   C        CCC     C   O+ CC+ OO+
8    CC CCCCCCCCC C  CC CCCCCC CCCCCCCCCCC O+ CC+ OO+
7    CC C xI C  C C  C  C II   CC  CC    C O   C   O
6  x CC   II C CC CC C CC xI CCCCC C    CC OO  CCC OO
5    CCCCCCCCC CCCCC C  C II C  CCCCCCCCCC  x   C   xxO
4    C  C   C      C    CCCC CCCCCCC     C  x   C x xxO
3  CCCx   x C CCCCCC         C      Cx  CCx x x C x x -
2     x   x CCCCCCCCCCCCCCCCCCCCCCC  x    x   x   x   -
1     x   x                          x    x   x   x   -
0 -----------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012
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
