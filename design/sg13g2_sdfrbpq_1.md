# Design Documentation for sg13g2_sdfrbpq_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2   G G  G G G             G G             G G
1   G G  G G G             G G             G G
0   G G  G G G             G G             G G
9   G G  G G G             G G             G G
8   G G  G G G             G G             G G
7   G G  G G G             G G             G G
6   GGG  GGGGG             GGG             GGG                G
5   G G  G G G             G G             G G
4   G G  GGGGG             G G             G G
3   G G  G G G             G G             G G
2   G G  G G G             G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +    ++         +                          +++
2     +cCccCcCc+    &+ CcCcCcC +  c   cCcCcCcCcCcCcCcCcCcC&+&
1     +C      C+ CC ++       C +CCCCC                     +++ O
0  c   c  cC  c+ Cc &+c cCc cCcCc c c   cCcCcCcCcCc       &+& o
9  CCCCC CCC  C+ CC ++C C   C     C   CCC       C CC    CC  + O
8  c   cCcc   c+ Cc   c c cCcCcCcCc   cCc cCcCcCc cCc cCcCcC& o
7  CII    I I CC  C     C C II C  C    C CCIII  C C C C    C  O
6  cIi cIii i cCcCcCcC  c   iIc c c cCcC CcIiIcCc cCc c  CcCc o
5  C    I   I     C     CCCCCCC CCCC C C  CIIIC     CCCCCC C OO
4  c _ cIiiIi cCc c       c c c     cC    c cCc c c        C Oo
3  C - CCCCCCCC-  C CCC - C - CCCCCCCC       CC CCCCCC -  CC- O
2    _    c    -      c _   _ cCcCcCcCcCcCcCcCcCcCcCc c-  c _
1    -         -        -   -                          -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | RESET_B | SCE | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal8 | Internal9 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X |   | X |   |   | X | X | X | X | X |   |   |   | X |
| PMOS1 | X |   |   |   |   |   |   |   | X |   | X | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly3 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |
| PMOS1 | O | O | O | O |   |
| PMOS2 |   |   |   |   |   |
