# Design Documentation for sg13g2_ebufn_8

## Substrate
```
  01234567890123456789012345678901234567890123
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppp
3                              p
2                              p
1  ppppppppppppppppppppppppppppppp     ppppppp
0  ppppppppppppppppppppppppppppppp     ppppppp
9  ppppppppppppppppppppppppppppppp     ppppppp
8  ppppppppppppppppppppppppppppppp     ppppppp
7
6
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn     nnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn     nnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn     nnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2        G G G G          G G G G       G G
1        G G G G          G G G G       G G
0        G G G G          G G G G       G G
9        G G G G          G G G G       G G
8        G G G G          G G G G       G G
7   GGGGGGGGGGGGG  GGGGGGGGGGGGGGGGGGGGGG G
6   GGGGGGGGGGGGG                     GGG GG
5        G G G G   G G        G G  G    G G
4        G G G G   G G        G G  G    G G
3        G G G G   G G        G G  GGG  G G
2        G G G G   G G        G G       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3                   +  +   +   +         +   +
2  cCCCcCCcCCCcCCCc & c+c c+c c+c c     c+c c+
1  C  C   C   C   C  C + C + CCCCC       + C +
0  cIcCcIcc i c i cCCCcCCCcCCCc    CCCCCCCcCc+
9  CI   I   I   I                          CCC
8  cIiIIIiIIiIIIi                   CCcC  c  C
7    I  CCCCCCCCCC                  C        C
6    I  CccCcCcCc  CCCCCCCCCCCCCCC  C iIi iI C
5   IIIIIIIIIIIII C   C      C   C  C        C
4  cIc cIcc i c i c _ c _ c-cCc-cCc C cCc-cC
3  C  C   C   C   C - C -  - C - C CCCCC - C -
2  CCCCCCCCCCCCCCCC _   _  -c  -c c c c c-c c-
1                   -   -  -   -         -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Internal1 | Internal11 | Internal13 | Internal15 | Internal16 | Internal2 | Internal4 | Internal5 | Internal6 | Internal7 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X |   |   | X |   | X |   | X | X |   |   |   |   |   |   |
| NMOS3 |   | X |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS1 | X |   | X |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |
| Poly1 |   |   | X |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly5 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 | X | X |   | X |   |   | X |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   | X |   |   |   | X |   |   | X | X |   |   | X | X |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O |   |   |   |
| NMOS3 |   |   |   |   |   | O | O |   |
| PMOS1 | O |   |   |   |   | O |   |   |
| PMOS2 |   |   |   |   |   | O | O |   |
