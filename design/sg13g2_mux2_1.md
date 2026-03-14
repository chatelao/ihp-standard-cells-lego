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
3  pppppppppppppppp
2  pppppppppppppppp
1  ppppppppppppppXX
0
9
8
7
6   X     X
5  nnnnnXnnnXnnnnnX
4  nnnnnnnXnnnnnnnX
3  nnnnnnnnnnnnnnnX
2  nnnnnnnnnnnnnnnX
1  nnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
4
3   G     G G
2   G     G G
1   G     G G    XX
0   G     G G
9   G     G G
8   G     G G
7   G     G G
6   X     X G
5   G   X G X     X
4   G     X G     X
3   G     G G     X
2   G     G G     X
1   G     G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567
4 ++++++++++++++++++
3
2       CCCCCCC
1       C     C  xx
0  C    C CC  C  OO
9  CCCCCCCCC  C  OO
8  C   CCC    C  OO
7  C   C      C   O
6  CxI C  x I CC CO
5  C   Cx I x    Cx
4  C   CIIxII CCCCx
3  C   C      C   x
2      CCCCCCCC   x
1
0 ------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
