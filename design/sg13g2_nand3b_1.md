# Design Documentation for sg13g2_nand3b_1

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4
3  pppppppppp
2  pppppppppp
1  pppppXpppX
0
9
8
7
6    X X X
5  nnnnnnnnnn
4  nnnnnnnnnX
3  nnnnnnnnnX
2  nnnnnnnnnX
1  nnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3    G G G
2    G G G
1    G GXG  X
0    G G G
9    G G G
8    G G G
7    G G G
6    X X X
5    G G G
4    G G G  X
3    G G G  X
2    G G G  X
1    G G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901
4 ++++++++++++
3
2
1       x   xO
0   C   O   OO
9   C   O   OO
8   C   OOOOOO
7   C        O
6   Cx x x C O
5   CI I I C O
4   CCCCCCCCxO
3           xO
2           xO
1
0 ------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901
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
