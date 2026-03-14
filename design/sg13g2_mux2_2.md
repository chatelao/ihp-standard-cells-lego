# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
3
2  pppXppppppppXppppX
1  pppXppppppppXpXXXX
0  pppXppppppppXpXXXX
9              X XXXX
8              X XXXX
7
6   X     X
5  nnnnnXnnnXnnnnnnnn
4  nnnnnnnXnnnnnnnnnn
3  nnXnnnnnnnnnnnnXXX
2  nnXnnnnnnnnnXnnXXX
1  nnXnnnnnnnnnXnnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789
3
2  G GX  G G G X    X
1  G GX  G G G X XXXX
0  G GX  G G G X XXXX
9  G G   G G G X XXXX
8  G G   G G G X XXXX
7  G G   G G G
6  GXG   GXG G
5  G G  XG GXG
4  G G   GXG G
3  G X   G G G    XXX
2  G X   G G G X  XXX
1  G X   G G G X    X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789
3 ++++++++++++++++++++
2     x CCCCCCCx    x
1     x C     Cx xxxx
0  C  x C CC  Cx xxxx
9  CCCCCCCCC  Cx xxxx
8  C   CCC    Cx xxxx
7  C   C      C    O
6  CxI C  x I CC C O
5  C   Cx I x    C O
4  C   CIIxII CCCC O
3  C x C      C   xxx
2    x CCCCCCCCx  xxx
1    x         x    x
0 --------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789
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
