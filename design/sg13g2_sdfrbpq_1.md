# Design Documentation for sg13g2_sdfrbpq_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNppNNNNNNNNNNpNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNppNNNNNNNNNNpNNNNNNNNN
1 NNNppppppppppppppNNNNNpppNNNppNNNNNNNNppppppNNpppNNNpNNNpppppN
0 NppppppppppppppppNNNNNpppNpppppppppNNNppppppNNpppNNNpNNNpppppN
9 NppppppppppppppppNpppppppNNNNNNNNNNNNNppppppNNpppppppppppppppN
8 NppppppppppppppppNNNNNNNNNNNNNNNNNNNNNppppppNNpppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSnnnSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSSSSSnnnSSSSSSSSSSSSnnnnnnnSnnnnnSSSSSSSSnnnS
3 SnnnnnnnnnnnnnnnnSnnnnnnnSnnnnnSSSSSSnnnnnnnSSSSnnSnnnnnnSnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSnSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2         G G            GG  GG   G G G G   G       G G GG  G
1   G     G G            GG  GG  GGGG G G   G       G G G   G
0   G     G G            GG  GG  GGGG G G   G       G G G   G
9   G     G G            GG  GG  GGGGGG G   G       G G G   G
8   G     G G            GG  GG  GGGG G G   G  G    G G G   G
7   GGG   G G          G GG  GGG GGGG G G   G       GGG G   GG
6   GGG G G G  G G   G G GG  GG   GGG G GG  GG     GG G GG  GG
5   G     G G          G GG  GG   GGG G G   G       G G G   G
4   G     G G          G GG  GG   G G G G   G       G G G   G
3   G     G G          G GG  GG   G G G G   G       G G G   G
2         G G          G  G  GG   GGGGGGG   G       G G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          + +
2     +cCccCcCc+     + CcCcCcC +  c   cCcCcCcCcCcCcCcCcCcC+ +
1     +C      C+ CC  + C     C +CCCCC                     + + O
0  c   c  cC  c+ Cc  +cCcCc cCcCc cCc   cCcCcCcCcCc       + + o
9  CCCCC CCC  C+ CC  +CCC   C     CC   CC       C CC    C   + O
8  c   cCcc   c+ Cc   cCc cCcCcCcCcC  cCc cCcCcCc cCc cCcCcC+ o
7  CII C  I I CC  C    CC C IICC  CC   C CCIII  C C C C    C  O
6  cIi cIii i cCcCcCcC Cc i iIi c cCcCcC CcIiIcCc cCc c  CcCc o
5  C   CI   I   C C    CCCCCCCC CCCC C C  CIIIC  CCCCCCCCC C OO
4  c - cIiiIi cCc c    C  c c c     cC    c c cCc c        C Oo
3  C - CCCCCCCC-  C CCCC- C - CCCCCCCC    CCCCCCCCCCCC -  CC- O
2    -    c    -      c -   - cCcCcCcCcCcCcCcCcCcCcCc c-  c -
1    -         -        -   -                          -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | RESET_B | SCD | SCE | Internal1 | Internal2 | Internal3 | Internal4 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   | X |   |   |   |
| NMOS2 |   |   |   |   |   |   |   | X |   |   |   |
| NMOS3 |   |   |   |   | X |   | X |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   | X |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   |   | X |
| NMOS8 |   |   |   |   |   |   |   | X |   |   |   |
| PMOS1 |   |   |   |   |   |   | X |   |   |   |   |
| PMOS2 | X |   |   |   |   |   |   | X |   | X | X |
| PMOS3 |   |   |   |   |   |   |   | X |   |   |   |
| PMOS4 |   |   |   |   |   |   |   | X |   |   |   |
| Poly1 |   |   |   |   | X |   | X |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   | X |   |   |   |
| Poly11 |   |   |   |   |   | X |   |   |   |   |   |
| Poly2 |   |   |   |   | X |   | X |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   | X |   |   |   |
| Poly5 |   |   | X |   |   |   |   | X |   |   |   |
| Poly6 |   |   |   |   |   |   |   | X |   | X |   |
| Poly7 |   |   | X |   |   |   |   | X |   | X |   |
| Poly8 |   |   |   |   |   |   |   | X | X | X |   |
| Poly9 |   |   |   |   |   |   |   | X |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   | NE |   |   |   |   |   |   |   |   |
| NMOS3 | O | O |   |   |   |   |   |   |   |   | O |   |   |   |   |   |
| NMOS4 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |
| NMOS7 |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |
| NMOS8 |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O |   |   |   |   |   |   |   |   | O |   |   |   |   |   |
| PMOS2 |   |   |   |   |   | O | O | O | O | O |   |   |   |   |   | W |
| PMOS3 |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |
