# Design Documentation for sg13g2_mux2_1

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4
3
2  pppppppppppppppp
1  pppppppppppppppp
0  pppppppppppppppp
9  pppppppppppppppp
8  pppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
4
3   G G G
2   G G G
1   G G G
0   G G G
9   G G G
8   G G G
7   G G G
6  GG GGG
5   G G G
4   G G G
3   G G G
2   G G G
1   G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3     +        +
2     + CCCCCCC+
1     + C     C+ oo
0  CCCCCC CC  C+ oo
9  C     CCC  C+ oo
8  C   CCC    C+ oo
7  C   C      C   O
6  i   i      CC CO
5  C   C         CO
4  C - C      CCCCo
3  C - CCCCCCCC-  o
2    -         -
1    -         -
0 -_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  012345678901234567
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
