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
1 NpppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
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
8   G G G    G G G     G G       G G
7   G G G    G G G     G G       G G
6   GGGGG    GGGGG     GGG       GGG
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
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     &        +        +           +
2     +        + ccccccc&   ccccccc &
1  cc +        + c     c& c c     c & O
0  cc +   cccccccc ccc cccc c c ccc & O
9  cc +   cc       ccccc  c c c ccccc O
8  cc +   cc  I I      c  c c c c   c O
7  C I I  C   I I   CC cIIC C CCC I C O
6  C i icCC C i i C C  ciIC C C C i C O
5  C    c C C     C CCCcCcC C CCCc   OO
4  cccccc c cccccccccc   ccccccccc - oO
3  c  - c   c  -   ccc - c     ccc - oO
2     - ccccc  -       - ccccccc   -
1     _        -       -           -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

