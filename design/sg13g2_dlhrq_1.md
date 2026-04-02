# Design Documentation for sg13g2_dlhrq_1

## Substrate
```
  012345678901234567890123456
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3
2
1  pppppp ppppppppppppppppp
0  pppppp pppppp     pppppp
9  pppppp pppppp     pppppp
8      pp                pp
7
6
5         n
4  nnnnnn nnnnnn    nnnnnnn
3  nnnnnn nnnnnnnnnnnnnnnnn
2         nnnnnnnnnn
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
4
3
2     G       G G        G
1     G       G G        G
0     G       G G        G
9     G       G GG G     G
8     G       G          G
7     GGGG  GG      GG G G
6  GG         GG G     G G
5             GG       G G
4             G        G G
3             G        G G
2             G        G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +      +       +   +
2  c &      & CCCC  & c & c
1  C +      +    C  + C + II
0  cCCCCCCCCC  CcCc   c & iI
9  CCC      C  C C CCCC + II
8    C cC c C CC      c c iI
7  I CIICCC CCC     C  I   I
6  i CIiCcC c c cC  c  IcCcI
5    C  C CCCCC  C   CCCCC I
4  c   cCCcCCC CcC  cC  c cI
3     - C    C   C - C  - II
2    c-c    _CCCCCc-c   -
1     -     -      -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Internal1 | Internal2 | Internal3 | Internal5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   | X | X |   | X | X |   |   |
| NMOS3 |   |   |   |   | X |   | X |   |
| PMOS1 |   |   |   |   | X |   |   |   |
| PMOS2 | X |   | X |   |   |   |   | X |
| PMOS3 | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   | X |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O |   |   |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 |   |   |   |   |   | O |   |   |   |   |   |
| PMOS2 |   |   | O |   |   |   |   |   | O | O |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |
