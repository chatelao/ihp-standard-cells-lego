# Design Documentation for sg13g2_inv_1

## Substrate
```
  012345
5 NNNNNN
4 NNNNNN
3 NNNNNN
2 NNNNNN
1 NNNNNN
0 NNNNNN
9 NNNNNN
8 NNNNNN
7 SSSSSS
6 SSSSSS
5 SSSSSS
4 SSSSSS
3 SSSSSS
2 SSSSSS
1 SSSSSS
0 SSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345
5
4  pppp
3  pppp
2  ppXp
1
0
9
8
7
6  X
5  nnXn
4  nnXn
3  nnXn
2  nnXn
1  nnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345
5
4  G
3  G
2  G X
1  G
0  G
9  G
8  G
7  G
6  X
5  G X
4  G X
3  G X
2  G X
1  G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345
5 ++++++
4
3
2    x
1    O
0    O
9    O
8    O
7    O
6  x O
5    x
4    x
3    x
2    x
1
0 ------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345
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
