# Design Documentation for sg13g2_nand2b_2

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4
3
2  pppppppppppp
1  pppppppppppp
0  pppppppppppp
9  pppppppppppp
8  pppppppppppp
7
6
5
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2  nnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
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
  01234567890123
4 &+&+&+&+&+&+&+
3 +   +   +   +
2 +   +   +   +
1 +   + o + o +
0 + C + o + o +
9 + C + ooooo +
8    C+     o
7    C      O
6    iC  i  O
5    C      O
4 - CCCCCCC o C
3 -   C - C   C
2 -     - CCCCC
1 -     -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  01234567890123
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
