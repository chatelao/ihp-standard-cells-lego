# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4      NN          NN     NNNNNNNN
3
2
1        NN              NN
0        NN              NN
9
8
7
6
5
4        SS              SS
3        SS              SS
2
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4      pp          pp     pppppppp
3 N     NN          NN     NNNNNNN
2 N     pp          pp     ppppppN
1 N                              N
0 N     pp          pp       pp  N
9 N     pp          pp       pp  N
8 N                              N
7 S     SS          SS     SSSS  S
6 S       SS            SS     SSS
5 S       SS            SS       S
4 S     nn          nn     nnnn  S
3 S       nn            nn     nnS
2 S       nn            nn       S
1      SS          SS     SSSSSSSS
0      nn          nn     nnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3   G G G             G G
2
1
0
9
8
7   G G G             G G
6   GGGGG             GGG
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
  01234567890123456789012345678901
4 c c &+& c & c c c+&+c c+&+&+&+&+
3     +     +      +++   +    +
2     &     & cCcC +&+   +    &
1     +     + C  C +++ C + OC + O
0  Cc cCc c c cCcC     C +oOc & o
9  C        C C CC CCCCC   OC + O
8  C    cCcCc c c  CcCcCcC Oc   o
7  C I I C CCCC CCCCC C  C OC   O
6  C i i C CCCC C   C Ci C OCCCCO
5  C     CCCCCCCC     CI   O
4  c _-cCcCc   cC  _ cC - Oo  -
3    --CCCCCCCC    - CC - O   - O
2    _-       CcCc _ cC - O C - O
1    --     -      -    -     -
0  c _-_-c c-c c c _-c c-c-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

