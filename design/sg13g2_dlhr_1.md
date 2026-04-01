# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 NNNNpNNNNNpNNNNNNNNNNNNNNNNNNNNN
2 NNNNpNNNNNpNNNNNNNNNNNNNNNNNNNNN
1 NNNNpNNNpppppppppppppppppNpppppN
0 NppppppNppppppNNNNNppppppNpppppN
9 NppppppNppppppNNNNNppppppNpppppN
8 NppppppNNNNNNNNNNNNppppppNNNpppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnSSnnSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnSSnnnnnnnnnnSnnnnnnSSSnnnS
3 SSSnnnSSnnnnnnnnnnSnnnnnnSnnnnnS
2 SSSSSSSSSSnnnnSSSSSnnnnnnSnnnnnS
1 SSSSSSSSSSnSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2    G G GG GGG G G G G G G GG G
1    G G GGGGGG G G G G G G GG G
0    G G GGGGGG G G G G G G GG G
9    G G GGGGGG GGGGG G G G GG G
8    G G GGGGGG G GGG G G G GG G
7    G G GGGGGGGG G G G G G GG G
6    G G GGGGGG G G GGGGGGGGGG G
5    G G GG GGGGG G G GGGGG GG G
4    G G GG GGG G G G GGGGG GG G
3    G G GG GGG G G G GGGGG GG G
2    G G GG GGG G G G GGGGG GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +      +++  +     +
2     +     + cCcC +++  +     +
1     +     +C   C +++ C+ OOC + O
0  cCcCcCccCcCcC C    cC+ oOc + o
9  C      C CC C C CCCCC  OOC + O
8  c   cC c cCcCcC CcCcCcCoOc   o
7  C I ICCC CCCCCCCCCC I CCOC   O
6  c i iCcc cCc c c cC IiCcOcCcCo
5  C    C CCCCCCC    C I   OC   O
4  c --cC c c  Cc  - Cc - oOc - o
3    --CCCCCCC     - C  - O C - O
2    --   c -CcCcC - C  - o c - o
1    --     -      -    -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | GATE | RESET_B | Internal1 | Internal2 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   | X |   |   |   |
| NMOS2 |   |   |   |   |   | X |   | X |   |
| NMOS3 |   |   |   |   |   |   | X |   | X |
| NMOS4 |   |   |   |   |   | X |   |   |   |
| PMOS1 | X |   |   |   |   | X |   | X |   |
| PMOS2 |   |   |   |   |   |   | X |   | X |
| Poly1 |   |   | X |   |   | X |   |   |   |
| Poly2 |   |   |   | X |   | X |   |   |   |
| Poly3 |   |   |   |   | X | X | X | X |   |
| Poly4 |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   | O |   |
| NMOS2 |   |   | O |   |
| NMOS3 |   |   | O | O |
| NMOS4 | O | O |   |   |
| PMOS1 | O | O | O |   |
| PMOS2 |   |   | O | O |
