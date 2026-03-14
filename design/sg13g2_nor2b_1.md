# Design Documentation for sg13g2_nor2b_1

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
1  pppppXX
0
9
8
7
6  X    X
5  nnnnXnn
4  nnnnXnn
3  nnnnXnn
2  nnnnXnn
1  nnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
4
3  G    G
2  G    G
1  G    XX
0  G    G
9  G    G
8  G    G
7  G    G
6  X    X
5  G   XG
4  G   XG
3  G   XG
2  G   XG
1  G    G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678
4 +++++++++
3
2
1       xx
0  C    OO
9  C    OO
8  CCC OOO
7    C O
6  x C OxI
5    C x
4  CCC x
3      x
2      x
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
