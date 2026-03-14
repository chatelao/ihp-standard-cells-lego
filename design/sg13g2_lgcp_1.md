# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4
3  ppppppppppppppppppppppppp
2  ppppppppppppppppppppppppp
1  pppppppppppppppppppppppXp
0
9
8
7      X           X
6                   X
5  nnnnnnnnnnnnnnnnnnnnnnnXn
4  nnnnnnnnnnnnnnnnnnnnnnnXn
3  nnnnnnnnnnnnnnnnnnnnnnnXn
2  nnnnnnnnnnnnnnnnnnnnnnnXn
1  nnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
4
3      G            G
2      G            G
1      G            G     X
0      G            G
9      G            G
8      G            G
7      X           XG
6      G            X
5      G            G     X
4      G            G     X
3      G            G     X
2      G            G     X
1      G            G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456
4 +++++++++++++++++++++++++++
3
2
1  C                      x
0  C    CCC   CCCCC  C    O
9  C CCCCCCCCCC   C  C    O
8  C C   C    C C CI CCC  O
7  C C x C C  CCC Cx   C  O
6  CCC I C C  CCC CIx  CC O
5  C CCCCC CCCCCC C    C  x
4  CCCC C       C     CC  x
3  C   CCCC     C     CC  x
2  C   CCCCCCC            x
1
0 ---------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456
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
