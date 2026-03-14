# Design Documentation for sg13g2_buf_2

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4
3  ppppppp
2  ppppppp
1  ppppppp
0
9
8
7
6       X
5  nnnXnnn
4  nnnXnnn
3  nnnXnnn
2  nnnXnnn
1  nnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
4
3      G G
2      G G
1      G G
0      G G
9      G G
8      G G
7      G G
6      GXG
5     XG G
4     XG G
3     XG G
2     XG G
1      G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678
4 +++++++++
3
2
1        C
0        C
9   CCCCCC
8  CC OC C
7  C  OC
6  COOOCxI
5     xC
4     xCCC
3     x  C
2     x
1
0 ---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678
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
