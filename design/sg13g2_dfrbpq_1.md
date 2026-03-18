# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4      NN          NN          NN          NN
3
2
1        NN              NN              NN
0        NN              NN              NN
9
8
7
6
5
4        SS              SS              SS
3        SS              SS              SS
2
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4      pp          pp          pp          pp
3 N     NN          NN          NN         NN    N
2 N     pp          pp          pp         pp    N
1 N                                              N
0 N     pp          pp          pp         pp    N
9 N     pp          pp          pp         pp    N
8 N                                              N
7 S     SS          SS          SS     SSSSSSSS  S
6 S       SS              SS            SS     SSS
5 S       SS              SS            SS       S
4 S     nn          nn          nn     nnnnnnnn  S
3 S       nn              nn            nn     nnS
2 S       nn              nn            nn       S
1      SS          SS          SS          SS
0      nn          nn          nn          nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3 G G     G G            G G
2
1
0
9
8
7 G G     G G            G G
6 GGG     GGG            GGG
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
  012345678901234567890123456789012345678901234567
4 c+c c+& c c+c c c+& c c c c c+& c c c c+c+& & c
3  +         +                           +    +
2  + CcCcCcC +cCcCc c c cCc c c cCcCcCcC +    &
1  + C      C+C   C                      +  C + O
0  + CcCc c cCc c c    Cc cCc c c        +  c & o
9  + CC   C     C C    C       CCCCC   C +  C + O
8    Cc cCcCcCcCc c cCcCcCcCcC Cc  C   C    c & o
7  I CC C II C  C C  C  C      CC  CCCCCCCC C   O
6  i CC   Ii C CC CCCC CC iI CCCCC CCCCCC C CCCCO
5  I CCCCCCCCC CCCC CC  C    C  CCCC      C C   O
4  I c  C   C       CcCcCcCc cCcCcCc     cC C -oO
3  CCC-   - C CCCCCCC        C      C-  CC  C -OO
2     -   - Cc c cCc c c c cCc c cC  _        -
1     -   -                          -        -
0  c c-_-c-c c c c _-c c c c c _-c c _ c c _-c-c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

