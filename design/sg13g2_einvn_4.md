# Design Documentation for sg13g2_einvn_4

## Substrate
```
  0123456789012345678901234
5 NNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234
5
4  ppppppppppppppppppppppp
3  ppppppppppppppppppppppp
2  ppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234
5
4   G                 G
3   G                 G
2   G                 G
1   G                 G
0   G                 G
9   G                 G
8   G                 G
7   G                 G
6   G                 G
5   G                 G
4   G                 G
3   G                 G
2   G                 G
1   G                 G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234
5 +++++++++++++++++++++++++
4
3
2    CC C   C   CCCCCCCCC
1    CC C   C   C   C   C
0    CC C   C   C O C O C
9    CC C   C   C O   O C
8     C C   C   C OOOOO
7  Ix C CCCCCCCCC  OIIxI
6  II C  CCCCCCCCC OIIII
5     C  C   C   C x
4    CCC C   C   C xxxxx C
3    CCC C   C   C       C
2    CCC C   C   CCCCCCCCC
1
0 -------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234
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
