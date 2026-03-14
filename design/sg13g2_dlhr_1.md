# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4
3  pppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppp
1  pppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901
4
3    G G               G
2    G G               G
1    G G               G
0    G G               G
9    G G               G
8    G G               G
7    G G               G
6    G G               G
5    G G               G
4    G G               G
3    G G               G
2    G G               G
1    G G               G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 ++++++++++++++++++++++++++++++++
3     x     x      xxx   x    x
2     x     x CCCC xxx   x    x
1     x     x C  C xxx C xxxC x x
0  CCCCCCCCCC CCCC     C +OOC + O
9  C        C C CC CCCCC  OOC + O
8  C    CCCCC C C  CCCCCCC OC   O
7  C x x C CCCC CCCCC C  C OC   O
6  C I I C CCCC C   C Cx C OCCCCO
5  C     CCCCCCCC     CI   xC   x
4  C xxCCCCC   CC  x CC x xxC x x
3    xxCCCCCCCC    x CC x x C x x
2    xx       CCCC x CC x x C x x
1    xx     x      x    x     x
0 --------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901
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
