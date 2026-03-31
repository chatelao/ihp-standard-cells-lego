# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 NNNNNNNpNNNNNNNNNNNpNNNNNNNNNN
2 NNNNNNNpNNpNNNppNNNpNNNNNNNNNN
1 NpppNpppNNppppppNpppNNNNNNpppN
0 NpppNpppNNpppNNNNpppppNNpppppN
9 NpppNppppppppNNNNpppppNNpppppN
8 NNNNNNNNNNNNNNNNNpppppNNpppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSnnnnnnnnnnSSSSSSSSnnnnnnS
4 SnnnSnnnnnnnnnnSSnnnnnnnnnnnnS
3 SnnnSnnnSSSSnnnSSnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSnnSSSSnnSSS
1 SSSSSSSSSSSSSSSSSSSnnSSSSnnSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2   G   G G   G G G   G G G G
1   G   G G   G G G   G G GGG
0   G   G G   G G G   G G GGG
9   G   G G   G G G   G G GGG
8   G   G G   G G G   G G GGG
7   G G G GG GG G G   G GGGGG
6  GG G G G  GG G G   GGGGGGGG
5   G G G G  GGGG G   G G G G
4   G   G G  GGGG G   G G G G
3   G   G G  GGGG G   G G G G
2   G   G GG  GGG G   G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +           +      +
2  + &   +cCc cCcC   +      +
1  + C CCCCC  C             + O
0  + c c ccCcCc cCcCcCcCcCc + o
9  + C C  C  CC CCCCCCCCCCC + O
8    c      cCc cCcCc  CcC    o
7  IICC     CCCCCC  C  CCCIICCO
6  iIcC CccCc i cC  c cCcCiIcCo
5    CC C  CCCCCCCC C  C CC COO
4    c cC- Cc     c c  Cc c cOo
3  - C CC-  CCCCC   CCCCCCCCCOO
2  -     -cCcCcCcCcCc     c
1  -     -            -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | GATE | Internal1 | Internal2 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   | X |   | X |
| NMOS2 |   |   |   |   |   | X |   |
| NMOS3 |   |   |   |   | X |   |   |
| PMOS1 | X |   |   |   | X |   |   |
| PMOS2 |   |   |   |   | X |   | X |
| PMOS3 |   |   |   |   |   | X |   |
| Poly1 |   |   | X |   |   |   |   |
| Poly3 |   |   |   |   | X |   |   |
| Poly4 |   |   |   | X | X |   |   |
| Poly5 |   |   |   |   | X |   |   |
| Poly6 |   |   |   | X | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | W | O |   |
| NMOS2 | O |   |   |   |   |   |   |
| NMOS3 |   | O | O | O |   |   | W |
| PMOS1 |   | O | O | O | EW | O |   |
| PMOS2 |   |   |   |   |   | O |   |
| PMOS3 | O |   |   |   |   |   |   |
