# Design Documentation for sg13g2_dllr_1

## Substrate
```
  012345678901234567890123456789012345
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345
5
4  pppppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345
5
4    G G                  G
3    G G                  G
2    G G                  G
1    G G                  G
0    G G                  G
9    G G                  G
8    G G                  G
7    G G                  G
6    G G                  G
5    G G                  G
4    G G                  G
3    G G                  G
2    G G                  G
1    G G                  G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345
5 ++++++++++++++++++++++++++++++++++++
4
3
2      CCCC     CCCC
1   C  C  CCCCC CCCC     CC   O C   OO
0   C  C CCCC C CCCC     CC   O C   OO
9   CCCC C   CC C CC CCCCCC   O C   OO
8   C    CCC CC C C     CCCCC OOC   OO
7   Cx x CC  CC C CCCC  C   C  OC    O
6   CI I CC CC  C CC CC C xICC OCCCC O
5   C    CC CCCCC CC C  C      xC    O
4   C   CCCCCCCCCCCC C  C    xxxC   xO
3   C   CCCC         C  C    xx C   xO
2       CCCC     CCCCC  C    xx     xO
1
0 ------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345
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
