# Design Documentation for sg13g2_inv_4

## Substrate
```
  01234567890
4 NNNNNNNNNNN
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4
3
2  ppppppppp
1  ppppppppp
0  ppppppppp
9  ppppppppp
8  ppppppppp
7
6
5
4  nnnnnnnnn
3  nnnnnnnnn
2  nnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
4
3   G
2   G
1   G
0   G
9   G
8   G
7   G
6  GG
5   G
4   G
3   G
2   G
1   G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  +   +   +
2  +   +   +
1  + o + o +
0  + o + o +
9  + oooooo
8         o
7         O
6  i      O
5         O
4  - oooooo
3  - o - o -
2  -   -   -
1  -   -   -
0 -_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  01234567890
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
