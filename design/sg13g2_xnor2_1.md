# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4      NN     NN
3             SS
2
1       NN
0       NN
9
8
7   SS SS SS  SS
6   SS SS SS  SS
5             SS
4
3       SS
2       SS
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4      pp     pp
3 N     NN     N
2 N     pp     N
1 N            N
0 N     pp     N
9 N     pp     N
8 N            N
7 S     SS     S
6 S     SS     S
5 S     SS     S
4 S     nn     S
3 S     nn     S
2 S     nn     S
1      SS     SS
0      nn     nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3     G G G
2
1
0
9
8
7     G G G
6     GGGGG
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
  01234567890123
4 c+c c+& c c &+
3  +    +     +
2  +    &     &
1  +  C +   O +
0  +  c &   o &
9  + CC     O
8    C IIIIIoOoO
7    C III I   O
6    C iIi I C O
5  - CCCCCCCCC O
4  _ cC CcCcC OO
3  -    CC  C OO
2  _      -
1  -      -
0  _ c _-c-c c-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

