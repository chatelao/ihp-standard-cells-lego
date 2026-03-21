# Design Documentation for sg13g2_and3_1

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 Nppppppppppp
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSnS
4 SnnnnnnnnnnS
3 SnnnnnnnnnnS
2 SnnnnnnnnnnS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3     G G G
2     G G G
1     G G G
0     G G G
9     G G G
8     G G G
7     G G G
6     GGGGG
5     G G G
4     GGG G
3     G G G
2  G GGGG G
1     G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&&&+&+&+&+
3    +   ++
2    +   +&
1   C+ C ++ OO
0   C+ c +& oO
9   C  C    OO
8   CcCcCcc  o
7   C II ICC O
6   c Ii icC O
5   C      OoO
4      i _ o
3      I - O
2  iIiIi _
1        -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)
