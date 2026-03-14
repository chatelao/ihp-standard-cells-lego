# Design Documentation for sg13g2_and4_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4
3  pppppppppppppp
2  pppppppppppppp
1  pppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnn
4  nnnnnnnnnnnnnn
3  nnnnnnnnnnnnnn
2  nnnnnnnnnnnnnn
1  nnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3   G G GGGG
2   G G GGGG
1   G G GGGG
0   G G GGGG
9   G G GGGG
8   G G GGGG
7   GGGGGGGG
6   G G GGGG
5   G G GGGG
4   G G GGGG
3   G G GGGG
2   G G GGGG
1   G G GGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 ++++++++++++++++
3   x  x   x    x
2   x  x   x    x
1   xC x C x  xxx
0   +C + C +  OO+
9  CCCCCCCCCC OO+
8  C         C O
7  C x x xxI C O
6  C I I III C O
5  C           x
4  CC      x  xxx
3  CC      x  xxx
2          x    x
1          x    x
0 ----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345
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
