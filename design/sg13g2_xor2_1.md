# Design Documentation for sg13g2_xor2_1

## Substrate
```
  012345678901234
5 NNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234
5
4  ppppppppppppp
3  ppppppppppppp
2  ppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnn
4  nnnnnnnnnnnnn
3  nnnnnnnnnnnnn
2  nnnnnnnnnnnnn
1  nnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234
5
4   G     G
3   G     G
2   G     G
1   G     G
0   G     G
9   G     G
8   G     G
7   G     G
6   G     G
5   G     G
4   G     G
3   G     G
2   G     G
1   G     G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234
5 +++++++++++++++
4
3
2      C  C   C O
1      C  C   C O
0      C  CCCCC O
9     CCCCCCCCC O
8     C       C O
7     C       C O
6  Ix C IIxII C O
5     C         O
4     C      xxxO
3     C      x
2
1
0 ---------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234
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
