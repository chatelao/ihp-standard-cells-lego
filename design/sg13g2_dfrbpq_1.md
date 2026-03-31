# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNpNNNNNNNNNNNpNNNpNNNNNNNN
2 NppppNNNNNNNNNNNNNNNNNNpNNNNNNNNNNNpNNNpNNNNNNNN
1 NNNNNppNNNNpNNNNNNNNppppppNNNppNNNNpNNNpNNpppppN
0 NNNNNppNpppppppppNNNppppppNNNppNNNNpNNNpNNpppppN
9 NppppppNNNNNNNNNNNNNppppppNNNpppppppppppNNpppppN
8 NNNNNNNNNNNNNNNNNNNNppppppNNNpppppppppppNNpppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSnnSSSSSSSSSSSSSSnnnnnSSnnnnnSSSSSSSSSSSSSSS
4 SSSSSnnSSSSSSSSSSSSSSnnnnnSSnnnnnSSSSSSSSSnnnnnS
3 SnnnnnnSnnnnnSSSSSSSSnnnnnSSSSnnnnnnnnnnSSnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSnSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3
2  G   G   G  G G G G G G G         G  GG G G GG
1  G   G   G  G G G G G G G         G   G G G GG
0  G   G   G  G G G G G G G         G   G G G GG
9  G   G   G  G G GGG G G G         G   G G G GG
8  G   G   G  G G G G G G G  G      G   G G G GG
7  G   GG  G GG G G G G G G         G   G G G GG
6  G   G      G G G G GGG G      G  G   GGGGG GG
5  G   G      G G G G G G G         G   G G G GG
4  G   G      G G G G G G G         G   G G G GG
3  G   G      G G G G G G G         G   G G G GG
2  G   G      G GGGGGGGGG G         G   G G G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +
2  + cCcCccC +cCcCc cCcCcCcCcCcCcCcCcCcC +    +
1  + C     C +C   C                      +  C +OO
0  + cCcC cCcCc c c   cCcCcCcCcCc        +  c +Oo
9  + CC   C     C C  CCC       CCCC    C +  C +OO
8    cCcCccCcCcCc c cCcCcCcCcCcCc c   cCc   c +Oo
7  I CC C II C  C C  C  C      CC C CCCCCC  C   O
6  i cCi  iIcCcCc cCcC Ci iIcCcCcCc c   cCc cCcCo
5  I CCCCCCCCCCCCCCC C  C   C  CCCCCCCCCCC  C   O
4  i c  Cc  c   c  C CcCcCcCc c c       cC  c -Oo
3  CCC- C - CCCCCCCC        C CCCCCCC-  CC  C -OO
2  c  -   - cCcCcCcCcCcCcCcCcCcCcCc c-  c     -
1     -   -                          -        -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | RESET_B | Internal1 | Internal2 | Internal3 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   | X |   |   |   |
| NMOS2 |   |   |   |   |   | X |   |   |   |
| NMOS5 |   |   |   |   |   |   | X |   | X |
| NMOS6 |   |   |   |   |   | X |   |   |   |
| PMOS1 | X |   |   |   |   | X |   |   |   |
| PMOS2 |   |   |   |   |   |   | X |   | X |
| PMOS3 |   |   |   |   |   | X |   |   |   |
| PMOS4 |   |   |   |   |   | X |   |   |   |
| PMOS5 |   |   |   |   |   | X |   |   |   |
| Poly1 |   |   |   | X |   | X |   |   |   |
| Poly2 |   |   |   |   | X | X |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |
| Poly4 |   |   | X |   |   | X |   | X |   |
| Poly5 |   |   | X |   |   | X |   | X |   |
| Poly6 |   |   |   |   |   | X |   | X |   |
| Poly7 |   |   |   |   |   | X | X |   |   |
| Poly8 |   |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | O | O |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | O | O |   | N |   |   |
| NMOS3 | O | O |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   | O |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   |   |   |   | O | O |   |   |   |
| NMOS6 |   |   | O | O |   |   |   |   |   |   |   |
| PMOS1 |   |   |   | O | O | O | O |   |   |   |   |
| PMOS2 |   |   |   |   |   |   | O | O |   |   |   |
| PMOS3 | O | O |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   | O | O |   |   |   |   |   | O |   |
| PMOS5 | O | E |   |   |   |   |   |   |   |   |   |
