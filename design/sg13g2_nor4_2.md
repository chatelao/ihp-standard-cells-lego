# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4
3
2  ppppppppppppppppppp
1  ppppppppppppppppppp
0  ppppppppppppppppppp
9  ppppppppppppppppppp
8  ppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890
4
3   G G G G G G G G
2   G G G G G G G G
1   G G G G G G G G
0   G G G G G G G G
9   G G G G G G G G
8   G G G G G G G G
7   G G G G G G G G
6   GGG GGG GGG GGG
5   G G G G G G G G
4   G G G G G G G G
3   G G G G G G G G
2   G G G G G G G G
1   G G G G G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3  +   +
2  +   + CCCCCCCC CCCCC
1  + C + C  C   C C   C
0  + C + CC C C C C o C
9  + CCCCCC C CCCCC o C
8                   o C
7                   O
6    i   i   i   i  OO
5    OOOOOOOOOOOOOOOO
4  - o    o   o     o -
3  - o ---o - o --- o -
2  -   ---  -   ---   -
1  -   ---  -   ---   -
0 -_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  012345678901234567890
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
