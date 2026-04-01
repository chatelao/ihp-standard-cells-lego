# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 ppppppppppppppppppppppppppppppppppppp
3
2
1   ppp        p pppppppp ppppp  pppppp
0   ppppppppppppppppppppp ppppp  pppppp
9   ppppppppppppppppppppp ppppp  pppppp
8   ppppppppppppppppppppp        pppppp
7
6
5                         nnnnn  nnnnnn
4  nnnnnnnnnnnnnnnnnnnnn nnnnnn  nnnnnn
3  nnnnnnnnnnnnnnnnnnnnn nnnnnn  nnnnnn
2                        nn
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456
4
3
2                 G   G    G G
1           G G G G   G    G G
0           G G G G   G    G G
9           G G G G   G    G G
8           G G G G   G    G G
7           G G G   GGG GG G G G  G G
6    G GGG  G G G G G   GG G      G G
5      G    G     G G GG   G
4      G            G      G
3      G            G      G
2      G            G      G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     +        +cCCCCCC & c cCCCCCC &
1  CC +        + C      + C C     C + O
0  cCc+   CCc    CcCcC CCCc c c cCC & o
9  CC +   CC       CCC    C C C CCC   O
8  cCc+   CCc I I c c  C  c c c c   C O
7  C I I  C   I I   CCCCIIC C  CC I C O
6  C i iCcC c i i c   cCiIC C   c i c O
5  C    C C C     C    C  C C CCCC   OO
4  cCCCCC c CCCCCCCC Cc cCC c cCCCc-cOo
3  C  - C   C  -   CCC - C     CCC - OO
2  c c- CCCCC c-  c    -cCCCCCCC   -  c
1     -        -       -           -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | Input1 | Input2 | Input3 | Input4 | Input5 | Input6 | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Output1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   |   | X |   |   |   |   |   |   | X |   |   |   |   |   |   |
| NMOS4 |   | X |   |   |   |   |   |   |   |   | X |   |   |   |   | X |
| PMOS1 | X |   |   |   |   |   |   |   |   | X |   | X |   |   | X |   |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS3 |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| PMOS4 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |   |   |   | X |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS3 | O | O |   | N | N | N |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   | N | N |   |   |   |
| PMOS1 |   | O |   | O |   |   |   | O | O | S |   |   |   |   | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   | S | S |   |   |   |
| PMOS3 |   |   | O |   |   |   |   |   |   |   |   |   | O |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
