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
3
2  ppppppppppppppppppppp
1  ppppppppppppppppppppp
0  ppppppppppppppppppppp
9  ppppppppppppppppppppp
8  ppppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
4
3   G G
2   G G
1   G G
0   G G
9   G G
8   G G
7   G G
6  GG GG
5   G G
4   G G
3   G G
2   G G
1   G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3  +      +  +
2  +      +  + CCCCCCCCC
1  + C  C +C + C   C   C
0  + C  C +C + C o C o C
9  + C  C +C + C o   o C
8    C  C  C   C ooooo
7    C  CCCCCCCC  O
6  i C i CCCCCCCC O
5    C   C  C   C OOOOO
4  - CCC C- C - C o   o C
3  - CCC C- C - CCCCC   C
2  -      -   -     CCCCC
1  -      -   -
0 -_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

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
Legend: M=Metal 2
