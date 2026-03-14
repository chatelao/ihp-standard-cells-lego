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
3  ppppppppppppppppppp
2  ppppppppppppppppppp
1  ppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890
4  G G   G G G G G G
3  G G   G G G G G G
2  G G   G G G G G G
1  G G   G G G G G G
0  G G   G G G G G G
9  G G   G G G G G G
8  G G   G G G G G G
7  G G   G G G G G G
6  GGG   GGG GGG GGG
5  G G   G G G G G G
4  G G   G G G G G G
3  G G   G G G G G G
2  G G   G G G G G G
1  G G   G G G G G G
0  G G   G G G G G G
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 +++++++++++++++++++++
3  x   x
2  x   x CCCCCCCC CCCCC
1  x C x C  C   C C   C
0  + C + CC C C C C O C
9  + CCCCCC C CCCCC O C
8                   O C
7                   O
6   xI    xI  xI Ix OO
5    xxxxxxxxxxxxxxxx
4  x x    x   x     x -
3  x x xxxx x x xxx x -
2  x   xxx  x   xxx   -
1  x   xxx  x   xxx   -
0 ---------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
