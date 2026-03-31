# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNpNNNNNNNNNNppNNNpNNNNNNNNNN
2 NppppNNNNNNNNNNNNNNNNNNpNNNNNNNNNNppNNNpNNNNNNNNNN
1 NNNNNppNNNNpNNNNNNNNppppppNNNppNNNppNNNpppNNpppppN
0 NNNNNppNpppppppppNNNppppppNNNppNNNppNNNpppNNpppppN
9 NppppppNNNNNNNNNNNNNppppppNNNpppppppppppppNNpppppN
8 NNNNNNNNNNNNNNNNNNNNppppppNNNpppppppppppppNNpppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSnnSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSSSSSSSSSSS
4 SSSSSnnSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSnnnSnnnnnS
3 SnnnnnnSnnnnnSSSSSSnnnnnnnSSSSnnnnnnnnnnnnnSnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSnSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3
2  G   G   G  G G G G G G G       G G GGG G    G G
1  G   G   G  G GGG G G G G       G G G G G    G G
0  G   G   G  G GGG G G G G       G G G G G    G G
9  G   G   G  G GGGGGGG G G       G G G G G    G G
8  G   G   G  G G G GGG G G  G    G G G G G    G G
7  G   GG  G GG G G G G G G       G G G G G    G G
6  G   G      G G G G GGG GG     GG G G GGGG GGGGG
5  G   G      G G G G G G G       G G G G G    G G
4  G   G      G G G G G G G       G G G G G    G G
3  G   G      G G G G G G G       G G G G G    G G
2  G   G      G GGGGGGG G G       G G G G G    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +   +
2  + cCcCccC +  c   cCcCcCcCcCcCcCcCcCcC +    +   +
1  + C     C + CCCC                      + C  + O +
0  + cCcC cCcCcCc c   cCcCcCcCcCc        + C  + o +
9  + CC   C     C C  CCC       CCC     C   C  + O +
8    cCcCccCcCcCc c  CcCcCcCcCcCcCc cCcCcCcC    o
7    CC C II C  C C  C CCIII   CC C C    C C    O
6  i cCi  iIcCcCc cCcC CiIiIcCcCcCc   c cC CcC  oOo
5    CCCCCCCCC CCCCC C  CIIIC  CCCCCCCCCCC  C   O
4    c  Cc  c   c  Cc   c c c c c        C- c - o -
3  CCC- C - C CCCCCC    CCCCC CCCCCCC-  CC- C - O -
2  c  -   - cCcCcCcCcCcCcCcCcCcCcCc c-  c -   -   -
1     -   -                          -    -   -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | RESET_B | Internal1 | Internal2 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   | X |   |   |
| NMOS2 |   |   |   |   |   | X |   |   |
| NMOS5 |   |   |   |   |   |   |   | X |
| NMOS6 |   |   |   |   |   | X |   |   |
| PMOS1 | X |   |   |   |   | X | X |   |
| PMOS2 |   |   |   |   |   |   |   | X |
| PMOS3 |   |   |   |   |   | X |   |   |
| PMOS4 |   |   |   |   |   | X |   |   |
| PMOS5 |   |   |   |   |   | X |   |   |
| Poly1 |   |   |   | X |   | X |   |   |
| Poly2 |   |   |   |   | X | X |   |   |
| Poly3 |   |   |   |   |   | X |   |   |
| Poly4 |   |   | X |   |   | X | X |   |
| Poly5 |   |   | X |   |   | X | X |   |
| Poly6 |   |   |   |   |   | X | X |   |
| Poly7 |   |   |   |   |   | X | X |   |
| Poly8 |   |   |   |   |   | X | X |   |
| Poly9 |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | O | O |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | O | O | O |   |   |   |
| NMOS3 | O | O |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   | O |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   |   |   |   |   |   | O |   |   |
| NMOS6 |   |   | O | O |   |   |   |   |   |   |   |
| PMOS1 |   |   |   | O | O | O | O | O |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   | O |   |   |
| PMOS3 | O | O |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   | O | O |   |   |   |   |   | O |   |
| PMOS5 | O | E |   |   |   |   |   |   |   |   |   |
