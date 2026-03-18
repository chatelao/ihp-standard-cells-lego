# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4      NN         NN    N
3                       N
2                       N
1        NN         NN  N
0        NN         NN  N
9                       N
8                       N
7                   SS  S
6                   SS  S
5                       S
4        SS         SS  S
3        SS         SS  S
2                       S
1                       S
0                       S
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4      pp         pp    p
3 N     NN     NNNNNNNNNN
2 N     pp     pppppppppN
1 N                    pN
0 N     pp        pp   pN
9 N     pp        pp   pN
8 N                    pN
7 S     SS     SSSSSSSSSS
6 S       SS       SSSSSS
5 S       SS       SSSSSS
4 S     nn     nnnnnnnnnS
3 S       nn       nnnnnS
2 S       nn       nnnnnS
1      SS         SS    S
0      nn         nn    n
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3 G G             G G
2
1
0
9
8
7 G G             G G
6 GGG             GGG
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
  01234567890123456789012
4 c+c c+& & c+c c &+c c &
3  +      +  +
2  +      &  + CcCcCcCcC
1  + C  C +C + C   C   C
0  + C  c &C + C O C O C
9  + C  C +C + C O   O C
8    C  c  C   C OoOoO
7  IIC  CCCCCCCC  OIIII
6  iIC   CCCCCCCC OiIII
5    C   C  C   C OOOOO
4  _ cCc c- C - C O   O C
3  - CC  C- C - CCCCC   C
2  _      -   -     CcCcC
1  -      -   -
0  _ c _-c-c c-c c-_ c c-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

