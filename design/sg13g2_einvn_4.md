# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4
3  ppppppppppppppppppppp
2  ppppppppppppppppppppp
1  ppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
4   G               G
3   G               G
2   G               G
1   G               G
0   G               G
9   G               G
8   G               G
7   G               G
6   G               G
5   G               G
4   G               G
3   G               G
2   G               G
1   G               G
0   G               G
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 +++++++++++++++++++++++
3  x      x  x
2  x      x  x CCCCCCCCC
1  x C  C xC x C   C   C
0  + C  C +C + C O C O C
9  + C  C +C + C O   O C
8    C  C  C   C OOOOO
7  IxC  CCCCCCCC  OIxII
6  IIC   CCCCCCCC OIIII
5    C   C  C   C xxxxx
4  x CCC Cx C x C x   x C
3  x CCC Cx C x CCCCC   C
2  x      x   x     CCCCC
1  x      x   x
0 -----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012
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
