# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2   G   G               G
1   G   G               G
0   G G G
9   G G G               G
8   G G G
7   G G G               G G
6  GGGGGGGG G G G G G G GGG G G G
5   G   G               G G
4   G   G               G
3   G   G               G
2   G   G               G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +      +        ++   +     +
2  cC+&cCcc & cCcCc &+&   &     & o
1  CC+ CCCCCCCCCCCC  ++CCC+ OCC + O
0  cC  cCccCcCcCcCc & &CcC& oCc & o
9  CCCCCCCCCCCCCCCCCCCCCCC  OCC + O
8  c c  CccCcCcCcCcCcCcCcCcCoOc & o
7  C I ICCCCCCCCCCCCCCCCCCCCCOCCCCO
6  c i iCccCcCcCcCcCcCcCiicCcOcCcCO
5  C   CCCCCCCCCCCCCCCCC     OC   O
4  cC_-cCccCcCcCcCcCc_cC _- oCc_- o
3  CC -CCCC -   CCCC -CC  - OCC - O
2    _-cCcc -_  cCcC _cC _- o  _- o
1     -     -        -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | GATE_N | RESET_B | VSS | Q | Q_N | VDD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |   |   |   |
| NMOS2 |   |   |   | X | X | X |   |
| PMOS1 |   |   |   | X | X | X | X |
| PMOS2 |   |   |   |   |   |   | X |
| Poly1 | X | X |   | X |   |   |   |
| Poly10 |   |   |   | X |   |   |   |
| Poly11 |   |   |   | X |   |   |   |
| Poly2 |   |   | X | X |   |   |   |
| Poly3 |   |   |   | X |   |   |   |
| Poly4 |   |   |   | X |   |   |   |
| Poly5 |   |   |   | X |   |   |   |
| Poly6 |   |   |   | X |   |   |   |
| Poly7 |   |   |   | X |   |   |   |
| Poly8 |   |   |   | X |   |   |   |
| Poly9 |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | S |   |   |   |   |   |   |   |   |   | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |
