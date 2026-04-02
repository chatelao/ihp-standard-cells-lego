# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3           p
2           p
1           ppppppppppppppppp
0   ppppp ppppppppppppppppppp
9   ppppp pppppp      ppppppp
8   ppppp pppppp      ppppppp
7
6
5  nnnnnn
4  nnnnnn nnnnnnnn    nnnnnnn
3    nnnn nnnnnnnnnnnnnnnnnnn
2    nn   nnnnnnnnnnnnnnnnnnn
1    nn     nnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567
4
3
2            G   G     G G G
1          G G   G     G G G
0          G G   G     G G G
9          G G   GG G  G G G
8          G G   GG G  G G G
7    G G   G G   G  G  G G G
6    G G GGG G G  G G G  G G
5          G G    G   GG G G
4          G   G         G G
3          G   G         G G
2          G   G         G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +       +++   +
2     +     &       +++   & c
1     +             +++ C + I
0  cCc+cCCCCCCCCCCC c c c & i
9  CC + C      CC C CCCCC   I
8  cCc+cC c     c c cCCC   Ci
7  C I I       CCCCCCC C I C
6  C i i c  cCcC  c  CcC IcCc
5  CC        C CCCC  C C I
4  cC  cC c  C       CcC  _ i
3  CCCCCCCCCCC   C     C  - I
2    c      c c   c c-cC  _ i
1     -     ---      -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | Input1 | Input3 | Input4 | Input5 | Internal1 | Internal3 | Internal5 | Internal6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   |   |   | X |   |   | X |
| PMOS1 | X |   |   |   |   |   |   | X |   |   |   |
| PMOS2 | X |   |   |   |   |   | X | X |   | X |   |
| Poly1 |   |   |   |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   | X |   |   |   |
| Poly7 |   |   |   |   |   |   |   | X |   |   |   |
| Poly8 |   |   |   |   | X |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   | X |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   | X |   |   |   |
| Poly12 |   |   |   |   |   |   |   | X |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | N |   | N | N | N |   |   |   |   |
| PMOS1 |   |   |   |   |   |   |   | S | S |   |   |   |   |
| PMOS2 | O |   | O | O | O |   |   |   |   |   | S | O | O |
