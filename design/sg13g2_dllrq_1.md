# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3 NNNNNNNNNNpNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNpNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNpppppppppppppppppN
0 NNpppppNpppppppppppppppppppN
9 NNpppppNppppppNNNNNNpppppppN
8 NNpppppNppppppNNNNNNpppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnSnnnnnnnnSSSSnnnnnnnS
3 SSSnnnnSnnnnnnnnnnnnnnnnnnnS
2 SSSnnSSSnnnnnnnnnnnnnnnnnnnS
1 SSSnnSSSSSnnnSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567
4
3
2      G GG  G   GG G GG GGG
1      G GGG G   GG G GG GGG
0      G GGG G   GG G GG GGG
9      G GGG G   GG G GG GGG
8      G GGG G   GG G GG GGG
7    G G GGG G   GG G GG GGG
6    G G GGG G G  G G G  GGG
5      G GGG G    G G GG GGG
4      G GGG   G  G G G  GGG
3      G GGG   G  G G G  GGG
2      G GGG   G  G G G  GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +       +++   +
2     +     +       +++   +
1     +             +++ C + OO
0  cC +cCccCcCcCcCc +++ c + oO
9  CC +CCC     CC C CCCCCCCCOO
8  cC +cCccCcCcCc c cCcCc cCoO
7  C I I C C  CCCCCCCC C I C O
6  c i i c CcCcCcCc  CcCcIiCcO
5  CC    C CCCCCCCC  C C I   O
4  cC  cCccCcC   CcCcCcC  - oO
3  CCCCCCCCCCC   C    CC  - OO
2        c       C   -cC  - oO
1     -     ---      -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | GATE_N | RESET_B | Internal1 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   | X | X |
| PMOS1 |   |   |   |   |   | X |   |
| PMOS2 | X |   |   |   |   | X | X |
| Poly1 |   |   |   | X |   | X |   |
| Poly2 |   |   |   |   |   | X |   |
| Poly4 |   |   |   |   |   | X |   |
| Poly5 |   |   |   |   |   | X |   |
| Poly6 |   |   |   |   |   | X |   |
| Poly7 |   |   |   |   | X | X |   |
| Poly9 |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | N | N |   |
| PMOS1 | O | E |   |   |   |   |   |   | S |   |
| PMOS2 |   | O |   | O | O | O | O | O |   |   |
