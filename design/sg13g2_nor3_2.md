# Design Documentation for sg13g2_nor3_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
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
4
3  pppppppppppppp
2  pppppppppppppp
1  pppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnn
4  nnnnnnnnnnnnnn
3  nnnnnnnnnnnnnn
2  nnnnnnnnnnnnnn
1  nnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3  GGGGGGGG  G G
2  GGGGGGGG  G G
1  GGGGGGGG  G G
0  GGGGGGGG  G G
9  GGGGGGGG  G G
8  GGGGGGGG  G G
7  GGGGGGGG  G G
6  GGGGGGGG  GGG
5  GGGGGGGG  G G
4  GGGGGGGG  G G
3  GGGGGGGG  G G
2  GGGGGGGG  G G
1  GGGGGGGG  G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 ++++++++++++++++
3
2
1    C   CCCCCCCC
0    C   C  C   C
9    C    C   O C
8    CCCCCC OOO C
7           O
6   xx  xxOOO xI
5         x x
4    xxxxxx xxx
3    x    x   x
2
1
0 ----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345
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
