# Design Documentation for sg13g2_nor2b_2

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4
3
2  pppppppppp
1  pppppppppp
0  pppppppppp
9  pppppppppp
8  pppppppppp
7
6
5
4  nnnnnnnnnn
3  nnnnnnnnnn
2  nnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3   G G G G
2   G G G G
1   G G G G
0   G G G G
9   G G G G
8   G G G G
7   G G G G
6   GGG GGG
5   G G G G
4   G G G G
3   G G G G
2   G G G G
1   G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +       +
2    +       +
1  C + CCCCC +
0  C + C   C +
9  C +   o C +
8  C   ooo
7  CCC O
6  C i O i
5  C   OOOOO
4    - o   o -
3    - o - o -
2    -   -   -
1    -   -   -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  012345678901
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
