# Design Documentation for sg13g2_nor3_1

## Substrate
```
  0123456789
5 NNNNNNNNNN
4 NNNNNNNNNN
3 NNNNNNNNNN
2 NNNNNNNNNN
1 NNNNNNNNNN
0 NNNNNNNNNN
9 NNNNNNNNNN
8 NNNNNNNNNN
7 SSSSSSSSSS
6 SSSSSSSSSS
5 SSSSSSSSSS
4 SSSSSSSSSS
3 SSSSSSSSSS
2 SSSSSSSSSS
1 SSSSSSSSSS
0 SSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789
5
4  pppppppp
3  pppppppp
2  pppppppp
1
0
9
8
7
6
5  nnnnnnnn
4  nnnnnnnn
3  nnnnnnnn
2  nnnnnnnn
1  nnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789
5
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
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789
5 ++++++++++
4
3
2
1         O
0     OOOOO
9     OOOOO
8     O
7     O
6  x  Ox x
5     x
4     xxxxx
3     x   x
2     x   x
1
0 ----------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789
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
