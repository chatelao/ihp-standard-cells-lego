# Design Documentation for sg13g2_mux2_1

## Substrate
```
  012345678901234567
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
3
2  pppXppppppppXppp
1  pppXppppppppXpXX
0  pppXppppppppXpXX
9              X XX
8              X XX
7
6   X     X
5  nnnnnXnnnXnnnnnn
4  nnnnnnnXnnnnnnnn
3  nnXnnnnnnnnnnnnX
2  nnXnnnnnnnnnXnnX
1  nnXnnnnnnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
3
2   G X   G G  X
1   G X   G G  X XX
0   G X   G G  X XX
9   G     G G  X XX
8   G     G G  X XX
7   G     G G
6   X     X G
5   G   X G X
4   G     X G
3   GX    G G     X
2   GX    G G  X  X
1   GX    G G  X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567
3 ++++++++++++++++++
2     x CCCCCCCx
1     x C     Cx xx
0  C  x C CC  Cx xx
9  CCCCCCCCC  Cx xx
8  C   CCC    Cx xx
7  C   C      C   O
6  CxI C  x I CC CO
5  C   Cx I x    CO
4  C   CIIxII CCCCO
3  C x C      C   x
2    x CCCCCCCCx  x
1    x         x
0 ------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567
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
