# Design Documentation for sg13g2_nand3_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4
3  ppppppp
2  ppppppp
1  ppppppp
0
9
8
7
6
5  nnnnnnn
4  nnnnnnn
3  nnnnnnn
2  nnnnnnn
1  nnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
4
3  G G  G
2  G G  G
1  G G  G
0  G G  G
9  G G  G
8  G G  G
7  G G  G
6  G G  G
5  G G  G
4  G G  G
3  G G  G
2  G G  G
1  G G  G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 +++++++++
3
2
1    o   o
0    O   O
9    O   O
8    OOOOO
7      O
6  i i OiI
5      o
4      ooo
3        o
2        o
1
0 ---------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, i=Metal 1 Input Connection, o=Metal 1 Output Connection

## Metal 2
```
  012345678
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
