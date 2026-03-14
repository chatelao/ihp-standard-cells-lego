# Design Documentation for sg13g2_ebufn_4

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4
3
2  ppppppppppppppppppppppppp
1  ppppppppppppppppppppppppp
0  ppppppppppppppppppppppppp
9  ppppppppppppppppppppppppp
8  ppppppppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
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
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +       +   +
2    +       +   + CCCCCCCCC
1  C +      C+ C + C   C   C
0  CCCCCCC  CCCC + C o C o C
9  C     CCCCC C   C o   o C
8  C   CCCC  C CCCCC ooooo
7  C      C  CCCCCCCCCCC O
6  i   i  C         CCCC O
5  C      C CCCCCCCC OOOOO
4  C -    C C- C - C o   o C
3  C - CCCC C- C - C   C   C
2    -    C  -   - CCCCCCCCC
1    -       -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  012345678901234567890123456
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
