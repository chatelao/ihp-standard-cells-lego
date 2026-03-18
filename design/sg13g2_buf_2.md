# Design Documentation for sg13g2_buf_2

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
3       G G
2
1
0
9
8
7       G G
6       GGG
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
3  +    +
2  +    +
1  +    +C
0  +CcCcCc
9  CC  C C
8  c  Oc
7  C  OC
6  cOoOcIi
5     OCCC
4   - O  c
3   - O -C
2   -   -
1   -   -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

