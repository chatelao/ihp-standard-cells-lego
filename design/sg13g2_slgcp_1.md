# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  012345678901234567890123456789
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3                       p
2                       p
1  ppppp p     pppppp ppppppppp
0  ppppp ppp pppppppp ppppppppp
9  ppppp ppp ppp  ppp ppppppppp
8        ppp ppp  ppp       ppp
7
6
5
4  nnnnnnn nnn    nn nnnnnn nnn
3  nnnnnnn nnnnnnnnn nnnnnn nnn
2      n
1      n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789
4
3
2   G     G      G G     G
1   G     G      G G     G
0   G     G      G G     G
9   G     G      G G     G
8  GG G   G     GG G   GGG
7  GG G   G  GG    G  GGG    G
6   G     G       GG  GGGGG  G
5   G   G  GG     G   G GG   G
4   G   G   G     G   G GG   G
3   G   G   G     G   G GG   G
2       G   G     G   G GG   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +        +         +
2  &   c &        +         + c
1  +   C +        + CCCCC C + I
0  &   cCCCCcCcC  c c   C c & i
9       C    C C    CCC   C + I
8  c IIiC cCc cCcCCCcCc   c   i
7  I  I C CCCCCC     C I   C  I
6  I  CCC c c CCCCc  CcI CcCcCI
5          CC C      C     C  I
4  _ c   c  C c   CCcCc-  cC_ i
3  - CCCCCC CC    C  C -  CC- I
2  -   _  c CCCCc CCCCc-    _ c
1  -   -               -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Internal1 | Internal2 | Internal3 | Internal4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   | X |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |
| NMOS3 |   | X |   |   |   |   |   | X |   |
| NMOS4 |   | X | X |   |   |   |   |   |   |
| PMOS1 |   |   |   |   |   | X |   |   |   |
| PMOS2 | X |   |   |   |   | X |   |   |   |
| PMOS3 | X |   | X |   |   |   |   |   | X |
| PMOS4 | X |   |   |   |   | X |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |
| Poly4 |   | X |   |   | X | X |   | X |   |
| Poly5 |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   | X |   |   |   |   |   |
| Poly7 |   |   |   |   |   | X |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   |   |   |   | O |   |   |   |   |
| NMOS2 |   | O | O |   |   |   |   |   |   |   |
| NMOS3 |   |   |   | O |   |   |   |   |   |   |
| NMOS4 |   |   |   |   | O |   |   |   |   |   |
| PMOS1 |   |   |   |   |   |   | O |   |   |   |
| PMOS2 |   |   | O |   |   |   |   |   | S | O |
| PMOS3 |   |   |   | O | S |   |   |   |   |   |
| PMOS4 |   |   |   |   |   | O |   | S |   |   |
