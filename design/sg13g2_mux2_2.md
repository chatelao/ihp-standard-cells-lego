# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 NNNNNNNNNNNNNNNNNNNN
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
4
3  pppppppppppppppppp
2  pppppppppppppppppp
1  pppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789
4  G G   G G G
3  G G   G G G
2  G G   G G G
1  G G   G G G
0  G G   G G G
9  G G   G G G
8  G G   G G G
7  GGG   G G G
6  G G   GGG G
5  G G   G GGG
4  G G   G G G
3  G G   G G G
2  G G   G G G
1  G G   G G G
0  G G   G G G
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 ++++++++++++++++++++
3     x        x    x
2     x CCCCCCCx    x
1     x C     Cx xxxx
0  CCCCCC CC  C+ OOO+
9  C     CCC  C+ OOO+
8  C   CCC    C+ OOO+
7  CxI C      C    O
6  CII Cx x I CC C O
5  C   Cx   x CCCC x
4  C x CIIxII C   xxx
3    x CCCCCCCCx  xxx
2    x         x    x
1    x         x    x
0 --------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789
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
