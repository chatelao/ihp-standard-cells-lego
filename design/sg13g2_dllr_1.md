# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNppNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNppNNNNNNNNNNNNNNNNNNNNNN
1 NppppppNpppppppppppppppppppNpppppN
0 NppppppNpppppppNNNNNpppppppNpppppN
9 NppppppNpppppppNNNNNpppppppNpppppN
8 NNNNNNNNpNNNNNNNNNNNpppppppNpppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnSnnnnnnnnnnnnnnnnnnnSnnnnnS
3 SnnnnnnSnnnnnnnnSSSSnnnnnnnSnnnnnS
2 SSSSSSSSSSSSSSSSSSSSnnnnnnnSSSnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2    G G       G GG G G G     G GG
1    G G       G GG G GGGG G  GGGG
0    G G       G GG G GGGG G  GGGG
9    G G       G GG G GGGG G  GGGG
8    G G       G  G G GGGG G  GGGG
7    G G     G   GG G GGGG G  GGGG
6    G G   G   G GG GGGGGG GGGGGGG
5    G G   G   G GG G G G     GGGG
4    G G   G   G  G G G G     GGGG
3    G G   G   G  G G G G     GGGG
2    G G   G   G  G G G G     G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +      +        ++   +     +
2    +   c  + cCcCc  ++   +     +
1  C + CCCCCCCC C C  ++ C + O C + O
0  c   cCc   Cc c c     c + o c + o
9  CCCCCCCCCCCC C C CCCCC + O C + O
8  c c  C c cCcCc c    CcCc oOc + o
7  C I IC C CCCCCCCCC  C  C  OC   O
6  c i iC cCc cCcCcCcCcCiIcCoOcCcCo
5  C    C CCCCCCCCCC   C     OC   O
4  c  -cC cCcCcCcCcC- cC  -Oo c - o
3     - C C -   CCCC- CC  -OO C - O
2     -     -     c - cC  -Oo   - o
1     -     -       -     -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | GATE_N | RESET_B | D | Internal1 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   |   |   |   | X |   | X |   |
| NMOS3 |   |   |   |   |   | X |   | X |
| NMOS4 |   |   |   |   | X |   |   |   |
| PMOS1 | X |   |   |   | X |   | X |   |
| PMOS2 |   |   |   |   |   | X |   | X |
| PMOS3 |   |   |   |   | X |   |   |   |
| Poly1 |   |   |   |   | X |   |   |   |
| Poly2 |   |   | X |   | X |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   | X |   |   |   |
| Poly6 |   |   |   | X | X |   |   |   |
| Poly7 |   |   |   |   |   | X | X |   |
| Poly8 |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | O | O | O | O |   |   |   |
| NMOS3 |   |   |   |   |   |   | O |   |   |
| NMOS4 | O | O |   |   |   |   |   |   |   |
| PMOS1 |   |   |   |   | O | O | O |   | O |
| PMOS2 |   |   |   |   |   |   | O |   |   |
| PMOS3 | O | O |   |   |   |   |   |   |   |
