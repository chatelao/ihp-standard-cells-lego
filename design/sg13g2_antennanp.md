# Design Documentation for sg13g2_antennanp

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
2  pppp
1
0
9
8
7
6
5  nnnn
4  nnnn
3  nnnn
2  nnnn
1  nnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345
5
4   G
3   G
2   G
1   G
0   G
9   G
8   G
7   G
6   G
5   G
4   G
3   G
2   G
1   G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345
5 ++++++
4
3
2
1
0   II
9   xI
8   II
7   x
6   I
5   I
4   II
3   xI
2   II
1
0 ------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, x=Connection (upper side)

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
