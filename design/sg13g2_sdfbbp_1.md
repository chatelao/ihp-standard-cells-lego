# Design Documentation for sg13g2_sdfbbp_1

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
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pppppppppppNpppppNNNNNNNpppppppNpNNNNNNNpNpNNNNNppppppNNNNpNNN
1 pppppppppppNpppppNNNNNNNpppppppNNNNNNNNNNNNNNNNNNpppppNNNNNNNN
0 pppppppppppNpppppNNNNNNNpppppppNNNNNNNNNNNNNNNNNNppppppNNNpNpN
9 pppppppppppNpppppNNNNNNNpppppppNNNNNNNNNNNNNNNNNNpppppNNNNNNNN
8 pppppppppppNpppppNNNNNNNpppppppNNNNNNNNNNNNNNNNNNppppppNNNNNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnnnnnnnnSnnnnnSSSSSSSnnnnnnnSSSSnSSSSSSSSSSSSSnnnnnnSSSSSnS
3 nnnnnnnnnnnSnnnnnSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSnnnnnSSSSSSSS
2 nnnnnnnnnnnSnnnnnSSSSSSSnnnnnnnSSSSnSSSSSnSSSSSSSnnnnnSSSSSnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2  G   G G G   G G         G G G                    G
1  G   G G G   G G         G G G                    G
0  G G G G G   G G         G G G                    G G
9  G G G G G   G G         G G G                    G G
8  G G G G G   G G         G G G                    G G
7  G GGG G G   G G         G GGG                    G G
6  GGG GGG G   GGG         G GGGG G G G G G G       GGG
5  G G G G G   G G         G G G                    G G
4  G G G G G   G G         G G G                    G
3    G G G G   G G         G G G                    G
2    G G G G   G G         G G G                    G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +       +    ++        +      +      +++    +    +     +
2    +&CCCCC&+    &+        & IIII&+IIIIII&+&    +&   +     &
1  C + C   C + C C++C       + I  I +I    I    C  +    + OOC + O
0  CCCCC C   CCC C&+c cCcC  & IC Ic+I cCCIcCcCcCCCcCCCC oOc & o
9        CC  C   C  CC C  C + IC IIII CCCICC  CCC      COOC   O
8   I I   C CC CCCCC C Cc CCC ICCCcCc c cIiIII  c cCC  CoOc   o
7   I I IiC  C C   C C  C C C I     C C C    I  C  C   C OCC  O
6   I   Iic cCcCIIcCcCcCc cCc i i i i i iCiCiCcCc cC I CcOcC  O
5      CCCCCCC CII  CCCCC CCCCCCC   C C CC      C  C     OC   O
4      C  - CC CCCCCcCc cCCCCCCCCCcCc_c cCc - c c cCC - oOc - o
3  -      - C   C     C C            -C  C  - C   C   - OOC - O
2  -      - CCCCC - c       -  CCCcC _cCcC _- cCcCc  _-     -_
1  -      -       -         -        -      -         -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | Input1 | Input2 | Input3 | Input4 | Input5 | Input6 | Input7 | SET_B | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS10 |   |   |   |   |   |   |   |   |   | X |   |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS7 |   |   |   |   |   |   |   |   |   |   | X |   | X |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS9 |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS1 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS10 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS11 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS12 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS4 |   |   |   |   |   |   |   |   |   |   | X | X |   |
| PMOS5 |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS6 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS7 |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS8 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| PMOS9 |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly1 | X |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   | X |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly5 |   | X |   |   |   |   |   |   | X |   |   |   |   |
| Poly7 |   |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   | X |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O |   |   |   |   |   |   |   |   |   |   |
| NMOS3 |   |   | O |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   | O | O |   |   |   |   |   |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS7 |   |   |   |   |   | O |   |   |   |   |   |   |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS9 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS10 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   | O |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   | O | O |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   | O |   |   |   |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS9 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS10 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS11 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS12 |   |   |   |   |   |   |   |   |   |   |   |   |
