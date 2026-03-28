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
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567
4
3
2  GG   GG G  G G G     G   G
1  GG   GG GG G G G     G   G
0  GG   GG GG G G G     G   G
9  GG   GG GG G G G   G G   G
8  GG   GG GG G G G   G G   G
7  GG G GG GG G G G   G G   G
6  GGGGGGGGGG G G G   G G   G
5  GG G GG GG G G G   G G   G
4  GG G GG GG G G G   G G   G
3  GG G GG GG G G G   G G   G
2  GG G GG GG G G G   G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +       +++   +
2     +     &       &+&   &
1     +             +++ C + OO
0  cC +cCccCcCcCcCc &+& c & oO
9  CC +CCC     CC C CCCCCCCCOO
8  cC +cCccCcCcCc c cCcCc cCoO
7  C I I C C  CCCCCCCC C I C O
6  c i i ciCcCcCcCc  CcCiI CcO
5  CC    C CCCCCCCC  C C I   O
4  cC  cCccCcC   CcCcCcC  _ oO
3  CCCCCCCCCCC   C    CC  - OO
2        c       C   -cC  _ oO
1     -     ---      -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | D | GATE_N | RESET_B | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X | X |   |   |   | X |
| PMOS1 | X |   | X |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X | X | X | X |   |
| Poly2 |   |   | X |   |   |   |   |
| Poly3 |   |   | X |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |
| Poly6 |   |   | X |   |   | X |   |
| Poly7 |   |   | X |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |
