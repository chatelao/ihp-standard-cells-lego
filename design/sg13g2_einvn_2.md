# Design Documentation for sg13g2_einvn_2

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
2  pXpppppXpppppp
1  pXpppppXpppppp
0  pXpppppXpppppp
9             X
8             X
7   X
6
5  nnnnnnnnnnnnnX
4  nnnnnnnnnnnnnn
3  nnnnnnnnnnnnnn
2  nXnnnnnXnnnnnn
1  nXnnnnnXnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
3
2  GXG    X    G G
1  GXG    X    G G
0  GXG    X    G G
9  G G        XG G
8  G G        XG G
7  GXG         G G
6  GGG         G G
5  G G         GXG
4  G G         G G
3  G G         G G
2  GXG    X    G G
1  GXG    X    G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345
3 ++++++++++++++++
2   x     x CCCCC
1   x C C x C   C
0   x C C x C   C
9     C C   C x C
8  IIIC CCCCC x C
7  IxIC       O
6  IIICC      O
5  IIIC       O x
4     C CCCCC O I
3     C C   C
2   x C C x CCCCC
1   x     x
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
