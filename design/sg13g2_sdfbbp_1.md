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
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2  G G G G G   G G         G GGGG   G G G           G G
1  G G G G G   G G         G G G                    G G
0  G G G G G   G G         G GGGG   G   G           G G
9  G G G G G   G G         GGG G                    G G
8  G G G G G   G G         G GGG  G       G G       G G
7  G GGG G G   G G         G GGG                    G G
6  GGG GGG G   GGG         G GGG            G       GGG G     G
5  G G G G G   G G         G G G                    G G
4  G G G GGG   G G         G G G                    G G
3  G G G G G   G G         G G G                    G G
2  G G G G G   G G         G G G                    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +       +    ++        +      +      +++    +    +     +
2    +&cCccC&+    &+        & iIiI&+iIiIiI&+&    +&   &     &
1  C + C   C + C C++C       + I  I +I    I    C  +    + OOC + O
0  cCcCc c   CcCcC&+c cCcC  & iCiI +i cCiIcCcCcCCCcCCCC oOc & o
9        CC  C   C  CC C  C + IC IIII CCCICC  CCC      COOC   O
8   I I   c cC CcCcC C Cc cCc iCcCiCc c cIiIiI  c  Cc cCoOc   o
7   I I IiC  C C   C C  C C C I     C C C    I  C  C   C OCC  O
6   I   Iic  CcCIIcCcCcCc cCc i c c c c cCcCiCcCc cCcIcCoOcC  o
5      CCCCCCC CII  CCCCC CCCCCCC   C C CC      C  C     OC   O
4      c  - cCcCCCCCcCc cCcCcCcCcCcCC_c cCc - c c cCc - oOc - o
3  -      - C   C     C C            -C  C  - C   C   - OOC - O
2  _      - cCcCc -         - cCcCcC _cCcC _- cCcCc  _-     -_
1  -      -       -         -        -      -         -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | Input1 | SET_B | Internal1 | Internal10 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal8 | Internal9 | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS2 |   |   |   | X |   | X | X | X | X | X |   |   | X | X |   | X |
| PMOS1 |   |   | X | X | X |   | X | X | X | X | X | X | X | X | X |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly1 | X |   |   | X | X |   |   |   |   |   |   |   |   |   |   | X |
| Poly10 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly13 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   | X |   |   | X |   |   |   | X |   |
| Poly5 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly8 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | NMOS1 | NMOS2 | PMOS1 | PMOS2 | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 |   |   |   |   | O | O | O | O |   |   |   | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly13 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
