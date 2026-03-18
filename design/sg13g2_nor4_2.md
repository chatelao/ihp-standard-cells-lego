# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4      NN     NNNNNNNNN
3                 SSSSN
2                 SSSSN
1        NN        NN N
0        NN        NN N
9                     N
8                     N
7                     S
6                  SS S
5                  SS S
4        SS        SS S
3        SS        SS S
2                     S
1                     S
0                     S
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4      pp     ppppppppp
3 N     NN     NNNNNNNN
2 N     pp     pppppppN
1 N                  pN
0 N     pp       pp  pN
9 N     pp       pp  pN
8 N                  pN
7 S     SS     SSSSSSSS
6 S       SS        S S
5 S       SS        S S
4 S     nn     nnnnnnnS
3 S       nn        n S
2 S       nn        n S
1      SS     SSSSSSSSS
0      nn     nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890
4
3   G G   G GG G G G
2
1
0
9
8
7   G G   G GG G G G
6   GGG   GGGGGG GGG
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
  012345678901234567890
4 c+c c+& c c &+&+&+&+&
3  +   +
2  +   + ccCcCcCc cCcCC
1  + C + C  C   C C   C
0  + c + cc c c c c o C
9  + CCCCCC C CCCCC O C
8                   o C
7                   O
6   Ii    Ii  iI Ii oO
5    O    OO  O  OOOO
4  - o    o   o     o -
3  - O ---O - O --- O -
2  -   ---  -   ---   -
1  -   ---  -   ---   -
0  _ c _-_ c-c-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

