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
2          G   G G           G G                    G
1  G   G G G   G G           G G                    G
0          G   G G           G G
9  G G G G G   G G           G G                    G G
8  G G G   G   G G         G G G
7  G GGG G G   G G         G GGG                    G G
6  GGG GGGGG  GGGGG G G G GGGGGGG G G G G G G G G G GGG   G
5  G G G G G   G G         G G G                    G G
4    G   G     G G         G G G
3    G G G     G G           G G                    G
2    G G G     G             G G                    G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +       +    ++        +      +      +++    +    +     +
2  cC+&cCccC&+cCcC&+cC      & IIII&+IIIIII&+& cC +&   & o   & o
1  CC+ CCCCC +CCCC++CCCC    + ICCI +I CCCICCCCCC +    + OOC + O
0  cCcCcCc   CcCcC&+cCcCcCc & ICcI&+I cCcIcCcCcCcCcCcCcCoOc & o
9  CCCCCCCCCCCCCCC  CCCCCCC & ICCIIII CCCICC  CCCCCCCCCCOOC   O
8   I I CccCcC CcCcCcCcCcCcCcCICcCcCcCcCcIiIIIcCc  CcCcCoOc   o
7   I i IiCC C C  CCCCCCCCCCCCiCCCCCCCCCC    I  CCCCCCCC OCC  O
6  iii  iicC CcCiIiCcCcCcCcCcCiCiCiCiCiCiCiCiCcCcCcCiicC OcC  O
5      CCCCCCC CII CCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCC  CC OC   O
4  _   c  __cCcCcCcCcCcCcCcCcCcCcCcCc_cCcCc -CcCcCcCcC- oOc - o
3  -   C  -CCC CCCCCCCCCCCC   CCCCCC -CCCCC -CCCCCCCCC- OOC - O
2  _      -_cCcCc_-        _- cCcCcC _cCcCc_-CcCcCc  _- o   -_o
1  -      -       -         -        -      -         -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | D | RESET_B | SCD | SCE | SET_B | VSS | Q | Q_N | VDD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |   |   |   |
| NMOS2 |   |   |   |   |   |   | X | X | X |   |
| PMOS1 |   |   |   |   |   | X | X | X | X | X |
| PMOS2 |   |   |   |   |   |   |   |   |   | X |
| Poly1 |   | X |   | X | X |   | X |   |   |   |
| Poly10 |   |   |   |   |   | X | X |   |   |   |
| Poly11 |   |   |   |   |   | X | X |   |   |   |
| Poly12 |   |   |   |   |   | X | X |   |   |   |
| Poly13 |   |   |   |   |   | X | X |   |   |   |
| Poly14 |   |   |   |   |   | X | X |   |   |   |
| Poly15 |   |   |   |   |   | X | X |   |   |   |
| Poly16 |   |   |   |   |   |   | X |   |   |   |
| Poly17 |   |   |   |   |   |   | X |   |   |   |
| Poly18 |   |   |   |   |   |   | X |   |   |   |
| Poly19 |   |   |   |   |   |   | X |   |   |   |
| Poly3 | X |   |   |   |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   | X | X |   |   |   |
| Poly6 |   |   | X |   |   |   | X |   |   |   |
| Poly7 |   |   |   |   |   |   | X |   |   |   |
| Poly8 |   |   |   |   |   |   | X |   |   |   |
| Poly9 |   |   |   |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 | Poly24 | Poly25 | Poly26 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | N |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O |   | O | O |   | S |   |   |   |   |   |   |   |   |   |   |   |   |   | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
