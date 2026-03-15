# Design Documentation for sg13g2_and4_1

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
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NppppppppppppN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SnnnnnnnnnnnnS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3     G   G
2     G   G
1     G   G
0     G   G
9     G   G
8     G   G
7     G   G
6    GGG GGG
5     G   G
4     G   G
3     G   G
2     G   G
1     G   G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3   +  +   +
2   +  &   &
1   +C + C +  OO
0   +x & x &  OO
9  CCCCCCCCCC OO
8  x         xOO
7  C I I I I C O
6  C i i i i C O
5  C           O
4  Cx      -  oO
3  CC      -  OO
2          -
1          -
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
