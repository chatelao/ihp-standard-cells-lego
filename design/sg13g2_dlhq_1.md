# Design Documentation for sg13g2_dlhq_1

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
6 SSSSSSSSSSSSSSSSNNNNNNNSSSSSSS
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
3        p           p
2        p  p   pp   p
1  ppp ppp  pppppp ppp      ppp
0  ppp ppp  ppp    ppppp  ppppp
9  ppp pppppppp    ppppp  ppppp
8                  ppppp  ppppp
7
6
5      nnnnnnnnnn        nnnnnn
4  nnn nnnnnnnnnn  nnnnnnnnnnnn
3  nnn nnn    nnn  nnnnnnnnnnnn
2                    nn    nn
1                    nn    nn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789
4
3
2   G   G
1   G   G                  G
0   G   G                  G
9   G   G                  G
8   G   G                  G
7   G G G GG GG G       GGGG
6   G G G    G  G     GGGGGGGG
5   G G G    G G  G
4   G   G    G G  G
3   G   G    G G
2   G   G  G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +           +      +
2  & c c &  c   c   c+      + c
1  + C CCCC   C             + I
0  & c c    CCC C       CCc & i
9  + C C  C  CC CCCCCCCCCCC + I
8  c   c  c CCc CCcCC cCCCc c i
7  II C     CCC  C  C  CCCII  I
6  iIcC CCC C c cC  C  CcCiIcCI
5     C     CCC     C  C C  C I
4  c c c _ CC c c c c  Cc c C i
3  - C C -          C    CCCC I
2  -     -cCCCCCCCCCc c     c c
1  -     -            -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | Input1 | Input3 | Internal1 | Internal10 | Internal12 | Internal13 | Internal14 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   | X |   |   |   |   |   |   | X |   |   |   |
| NMOS2 |   | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   | X |   |   |   |   |   |   | X |   |   | X |   | X |   |   |
| PMOS1 | X |   |   |   |   | X | X | X |   | X |   |   |   |   |   |   |
| PMOS2 | X |   |   | X |   | X |   |   |   |   |   |   |   |   |   |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   | X | X |   |   |   |   |   |   | X |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | W |   |   | N |   |
| NMOS2 | O |   |   |   |   |   |   |   |   |   |
| NMOS3 |   | O |   | O | O |   | W | N |   |   |
| PMOS1 |   | O |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   | O |   |
| PMOS3 | O |   |   |   |   |   |   |   |   |   |
