# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  01234567890123456
5 NNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456
5
4  ppppppppppppppp
3  ppppppppppppppp
2  pppppppppppppXX
1
0
9
8
7   X
6
5  nnnnnnnnnnnnnnX
4  nnnnnnnnnnnnnXX
3  nnnnnnnnnnnnnXX
2  nnnnnnnnnnnnnXX
1  nnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456
5
4   G
3   G
2   G           XX
1   G
0   G
9   G
8   G
7   X
6   G
5   G            X
4   G           XX
3   G           XX
2   G           XX
1   G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456
5 +++++++++++++++++
4
3
2        C      xx
1        C C    OO
0  C     C C    OO
9  CCCCC C C    OO
8      C C CCCC OO
7  IxI C C    C  O
6  III C CCCCCCC O
5      C C    C  x
4  CCCCC C CCCC xx
3  C     C      xx
2               xx
1
0 -----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456
5
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
