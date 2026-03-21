# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 ppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppN
1 Npppppppppppppppppppppppppppppppppppp
0 Npppppppppppppppppppppppppppppppppppp
9 NpppppppppppppppppppppppppppppppppppN
8 Npppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3   G G G    G G G     G G       G G
2   G G G    G G G     G G       G G
1   G G G    G G G     G G       G G
0   G G G    G G G     G G       G G
9   G G G    G G G     G G       G G
8   G G G    GGGGG     G G       G G
7   G G G    G G G     G G       G G
6   GGGGG    GGGGG     GGG       GGG  G
5   G G G    G G G     G G       G G
4   G G G    G G G     G G       G G
3   G G G    G G G     G G       G G
2   G G G    G G G     G G       G G
1   G G G    G G G     G G       G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&&&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     &        + CcCcCcC&   cCcCcCc &
1  CC +        + C     C+ C C     C + o
0  cC &   cCcCcCcc CcC ccCc c c cCc & o
9  CC +   CC       CcCCC  C C C CCcCC O
8  cC &   cC  i i      C  c c c c   c o
7  C I I  C   I I   cC CIIC C CCc I C O
6  c i iCcc c i i c c  ciIc c c c i c o
5  C    C C C     C CCcCCCC c cCCC   OO
4  cCcCcC c cCcCcCcCcc   CcCcCcCcC _ Oo
3  C  - C   C  -   CcC - C     CCC - OO
2     - cccCc  _       _ ccCcCcc   _
1     -        -       -           -
0 -_-___-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

