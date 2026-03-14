# Design Documentation for sg13g2_and4_2

## Substrate
```
  0123456789012345
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
3
2  pXppXpppXppppX
1  pXppXpppXppXXX
0  pXppXpppXppXXX
9             XXX
8             XXX
7
6    X X XX
5  nnnnnnnnnnnnnn
4  nnnnnnnnnnnnnn
3  nnnnnnnnXnnXXX
2  nnnnnnnnXnnXXX
1  nnnnnnnnXnnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
3
2   X GXGGGX    X
1   X GXGGGX  XXX
0   X GXGGGX  XXX
9   G G GGGG  XXX
8   G G GGGG  XXX
7   G G GGGG
6   GXGXGXXG
5   G G GGGG
4   G G GGGG
3   G G GGGX  XXX
2   G G GGGX  XXX
1   G G GGGX    X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345
3 ++++++++++++++++
2   x  x   x    x
1   xC x C x  xxx
0   xC x C x  xxx
9    C   C    xxx
8  CCCCCCCCCCCxxx
7  C         C O
6  C x x xxI C O
5  C I I III   O
4  C          OO
3  CC      x  xxx
2  CC      x  xxx
1          x    x
0 ----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345
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
