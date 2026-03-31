# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNppNNNNNNNNNNpNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNppNNNNNNNNNNpNNNNNNNNNNNNNNN
1 NNNppppppppppppppNNNNNpppNNNppNNNNNNNNppppppNNpppNNNpNNNpppNpNNNpppN
0 NppppppppppppppppNNNNNpppNpppppppppNNNppppppNNpppNNNpNNNpppNpppNpppN
9 NppppppppppppppppNpppppppNNNNNNNNNNNNNppppppNNpppppppppppppNpppNpppN
8 NppppppppppppppppNNNNNNNNNNNNNNNNNNNNNppppppNNpppppppppppppNpppNpppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSnnnSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSSSSSnnnSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSnnnnnSnnnS
3 SnnnnnnnnnnnnnnnnSnnnnnnnSnnnnnSSSSSSnnnnnnnSSSSnnSnnnnnnSnnnnnSnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSnSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3
2         G G            GG  GG   G G G G   G       G G GGG        G
1   G     G G            GG  GG  GGGG G G   G       G G G G    G   G
0   G     G G            GG  GG  GGGG G G   G       G G G G    G   G
9   G     G G            GG  GG  GGGGGG G   G       G G G G    G   G
8   G     G G            GG  GG  GGGG G G   G  G    G G G G    G   G
7   GGG   G G          G GG  GGG GGGG G G   G       GGG G G    G   G
6   GGG G G G  G G   G G GG  GG   GGG G GG  GG     GG G GGGGGGGG GGG
5   G     G G          G GG  GG   GGG G G   G       G G G G    G   G
4   G     G G          G GG  GG   G G G G   G       G G G G    G   G
3   G     G G          G GG  GG   G G G G   G       G G G G    G   G
2         G G          G  G  GG   GGGGGGG   G       G G G G    G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          +   +   +
2     +cCccCcCc+     + CcCcCcC +  c   cCcCcCcCcCcCcCcCcCcC+   +   +
1     +C      C+ CC  + C     C +CCCCC                     + O +   + O
0  c   c  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       + o + c + o
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   O + C + O
8  c   cCcc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcCo + c   o
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    CO   C   O
6  cIi cIii i cCcCcCcC Cc i iIi c cCcCcC CcIiIcCc cCc c  CcCo   cC Oo
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC COOO C   O
4  c - cIiiIi cCc c    C  c c c     cC    c c cCc c        CoOo c - o
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CCO - C - O
2    -    c    -      c -   - cCcCcCcCcCcCcCcCcCcCcCc c-  c   -   -
1    -         -        -   -                          -      -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | RESET_B | SCD | SCE | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   |   |   |   | X |   | X |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   | X |   |   | X |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| NMOS9 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS1 |   |   |   |   |   |   | X |   |   |   |   |   |   |
| PMOS2 | X |   |   |   |   |   |   | X |   |   | X |   | X |
| PMOS3 |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS5 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS6 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   | X |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   | X |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   | X |   | X |   |   |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   | X |   |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   | X |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   | X |   |   | X |   |   |
| Poly7 |   |   | X |   |   |   |   | X |   |   | X |   |   |
| Poly8 |   |   |   |   |   |   |   | X | X |   | X |   |   |
| Poly9 |   |   |   |   |   |   |   | X |   |   | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   | NE |   |   |   |   |   |   |   |   |
| NMOS3 | O | O |   |   |   |   |   |   |   |   | O |   |   |   |   |   |
| NMOS4 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |
| NMOS8 |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |
| NMOS9 |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O |   |   |   |   |   |   |   |   | O |   |   |   |   |   |
| PMOS2 |   |   |   |   |   | O | O | O | O |   |   |   |   |   |   | W |
| PMOS3 |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |
| PMOS5 |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS6 |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |
