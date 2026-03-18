# Design Documentation for sg13g2_nand2b_1

## Substrate
```
  012345678
4 NNNNNNNNN
3        SN
2        SN
1    NN   N
0    NN   N
9         N
8         N
7 SSSSSSSSS
6 SSSSSSSSS
5       SSS
4         S
3    SS   S
2    SS   S
1         S
0         S
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 NpppppppN
1 N      pN
0 N  pp  pN
9 N  pp  pN
8 N      pN
7 SSSSSSSSS
6 S  SS  SS
5 S  SS  SS
4 SnnnnnnnS
3 S  nn  nS
2 S  nn  nS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3 G G G
2
1
0
9
8
7 G G G
6 GGGGG
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3    +  +
2    +  &
1    +O +
0  C +oOoO
9  CCCCC O
8      C O
7      C O
6  i i CCO
5  CCCCC O
4  c    Oo
3    -  OO
2    _
1    -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

