# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 NNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4
3
2  pppppppppppppppppp
1  pppppppppppppppppp
0  pppppppppppppppppp
9  pppppppppppppppppp
8  pppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789
4
3   G G G G G G
2   G G G G G G
1   G G G G G G
0   G G G G G G
9   G G G G G G
8   G G G G G G
7   G G G G G G
6   GGG GGG GGG
5   G G G G G G
4   G G G G G G
3   G G G G G G
2   G G G G G G
1   G G G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 &+&+&+&+&+&+&+&+&+&+
3     +        +    +
2     + CCCCCCC+    +
1     + C     C+ ooo+
0  CCCCCC CC  C+ ooo+
9  C     CCC  C+ ooo+
8  C   CCC    C+ ooo+
7  C   C      C    O
6  C i C i   iCC C O
5  C   C      CCCC O
4  C - C      C   oo-
3    - CCCCCCCC-  oo-
2    -         -    -
1    -         -    -
0 -_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  01234567890123456789
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
