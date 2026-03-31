# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNpNNNNNNNNNNppNNNNNNNNNNNNNNNNN
2 NppppNNNNNNNNNNNNNNNNNNpNNNNNNNNNNppNNNNNNNNNNNNNNNNN
1 NNNNNppNNNNpNNNNNNNNppppppNNNppNNNppNNNppppNNNpppppNN
0 NNNNNppNpppppppppNNNppppppNNNppNNNppNNNppppppNpppppNN
9 NppppppNNNNNNNNNNNNNppppppNNNppppppppppppppppNpppppNN
8 NNNNNNNNNNNNNNNNNNNNppppppNNNppppppppppppppppNpppppNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSnnSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSSSSSSSSSSSSSS
4 SSSSSnnSSSSSSSSSSSSnnnnnnnSSnnnnnSSSSSSSnnnnnnnSnnnnn
3 SnnnnnnSnnnnnSSSSSSnnnnnnnSSSSnnnnnnnnnnnnnnnnnSnnnnn
2 SSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSnSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3
2  G   G   G  G G G G G G G       G G GGG     G
1  G   G   G  G GGG G G G G       G G G G     G
0  G   G   G  G GGG G G G G       G G G G     G
9  G   G   G  G GGGGGGG G G       G G G G     G
8  G   G   G  G G G GGG G G  G    G G G G     G
7  G   GG  G GG G G G G G G       G G G G     G
6  G   G      G G G G GGG GG     GG G G GGGGGGGG GGGG
5  G   G      G G G G G G G       G G G G    GGG   G
4  G   G      G G G G G G G       G G G G    GGG   G
3  G   G      G G G G G G G       G G G G    GGG   G
2  G   G      G GGGGGGG G G       G G G G    GGG   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +         +                           +  +   +   +
2  + cCcCccC +  c   cCcCcCcCcCcCcCcCcCcC +  +   +   +
1  + C     C + CCCC                      + O+   + OO+
0  + cCcC cCcCcCc c   cCcCcCcCcCc        + O+ cC+ oO+
9  + CC   C     C C  CCC       CCC     C   O+ CC+ OO+
8    cCcCccCcCcCc c  CcCcCcCcCcCcCc cCcCcCoO+ cC+ oO+
7    CC C II C  C C  C CCIII   CC C C    C O   C   O
6  i cCi  iIcCcCc cCcC CiIiIcCcCcCc   c cC Oo  CcC Oo
5    CCCCCCCCC CCCCC C  CIIIC  CCCCCCCCCCC  O   C   OOO
4    c  Cc  c   c  Cc   c c c c c        C  o   c - oOo
3  CCC- C - C CCCCCC    CCCCC CCCCCCC-  CC- O - C - O -
2  c  -   - cCcCcCcCcCcCcCcCcCcCcCc c-  c -   -   -   -
1     -   -                          -    -   -   -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | RESET_B | Internal1 | Internal2 | Internal3 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   | X |   |   |   |   |
| NMOS2 |   |   |   |   |   | X | X |   |   | X |
| NMOS5 |   |   |   |   |   |   |   |   | X |   |
| NMOS6 |   |   |   |   |   | X |   |   |   |   |
| PMOS1 | X |   |   |   |   | X | X | X |   | X |
| PMOS2 |   |   |   |   |   |   |   |   | X |   |
| PMOS3 |   |   |   |   |   | X |   |   |   |   |
| PMOS4 |   |   |   |   |   | X |   |   |   |   |
| PMOS5 |   |   |   |   |   | X |   |   |   |   |
| Poly1 |   |   |   | X |   | X |   |   |   |   |
| Poly2 |   |   |   |   | X | X |   |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |   |
| Poly4 |   |   | X |   |   | X |   | X |   |   |
| Poly5 |   |   | X |   |   | X |   | X |   |   |
| Poly6 |   |   |   |   |   | X |   | X |   |   |
| Poly7 |   |   |   |   |   | X |   | X |   |   |
| Poly8 |   |   |   |   |   | X | X | X |   | X |
| Poly9 |   |   |   |   |   |   |   |   | X |   |

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
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |
| PMOS3 | O | O |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   | O | O |   |   |   |   |   | O |   |
| PMOS5 | O | E |   |   |   |   |   |   |   |   |   |
