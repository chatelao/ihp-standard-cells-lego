# Design Documentation for sg13g2_nand2b_1

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
6
5  nnnnnnn
4  nnnnnnn
3  nnnnnnn
2  nnnnnnn
1  nnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
4
3  G G
2  G G
1  G G
0  G G
9  G G
8  G G
7  G G
6  G G
5  G G
4  G G
3  G G
2  G G
1  G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 +++++++++
3
2
1     x
0  C  O
9  C  OOOO
8  CCCCC O
7      C O
6  x x CCO
5      C x
4  CCCCCxx
3  C    xx
2       xx
1
0 ---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

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
