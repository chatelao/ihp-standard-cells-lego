# Design Documentation for sg13g2_nor3_1

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
4  G   G G
3  G   G G
2  G   G G
1  G   G G
0  G   G G
9  G   G G
8  G   G G
7  G   G G
6  G   G G
5  G   G G
4  G   G G
3  G   G G
2  G   G G
1  G   G G
0  G   G G
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 +++++++++
3  x
2  x
1  x     x
0  +     O
9  +  OOOO
8     O
7     O
6  x  Ox x
5     x
4  x  xxxx
3  x  xx x
2  x   x
1  x   x
0 ---------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

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
