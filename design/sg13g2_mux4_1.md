# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4      NN          NN          NN     N
3                                 SSSSN
2                                 SSSSN
1        NN              NN        NN N
0        NN              NN        NN N
9                                     N
8                                     N
7                                     S
6                                  SS S
5                                  SS S
4        SS              SS        SS S
3        SS              SS        SS S
2                                     S
1                                     S
0                                     S
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4      pp          pp          pp     p
3 N     NN          NN         NN    NN
2 N     pp          pp         pp    pN
1 N                                  pN
0 N     pp          pp         pp    pN
9 N     pp          pp         pp    pN
8 N                                  pN
7 S     SS          SS          SS
6 S       SS              SS        S S
5 S       SS              SS        S S
4 S     nn          nn         nn    nS
3 S       nn              nn        n S
2 S       nn              nn        n S
1      SS          SS          SS     S
0      nn          nn          nn     n
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3   G G G    G G G     G G       G G
2
1
0
9
8
7   G G G    G G G     G G       G G
6   GGGGG    GGGGG     GGG       GGG
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
  0123456789012345678901234567890123456
4 c c &+& c c c+c c+& c & c c c+& c & &
3     +        +        +           +
2     +        + CcCcCcC+   cCcCcCc +
1  CC +        + C     C+ C C     C + O
0  cC +   cCcCcCcC  c  CcCc c c cCc + O
9  CC +   CC       CCCCC  C C C CCCCC O
8  cC +   c   I I      C  c c c c   c O
7  C I I  C   I I   CC CIIC C CCC I C O
6  c i iCcc c i i c c  CiIc c c c i c o
5  C    C C C     C CCCCCCC C CCC     O
4  cCcCcC c cCcCcCcCcC   CcCcCcCcC - OO
3  C  - C   C  -   CCC - C     CC  -  O
2     - CccCc  -       - CcCcCcC   -
1     -        -       -           -
0  c c-_-c c c _ c _-c _ c c c _-c _ c-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

