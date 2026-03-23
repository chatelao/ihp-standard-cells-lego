# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2   G   G             G
1   G   G             G
0   G G G
9   G G G             G
8   G G G
7   G G G             G G
6  GGGGGGGG G G G G G GGG G G G
5   G   G             G G
4   G   G
3   G   G             G
2   G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +      +++   +    +
2     &     &CcCcC +&+  &+o   &
1  CC +     +CCCCC +++CC +OOCC+ O
0  cCcCcCccCcCcCcC    cC&+oOcC& o
9  CC  CCCCCCCCCCCCCCCCC  OOCC+ O
8  c   cCccCcCcCcCcCcCcCcCoOcC  o
7  C I ICCCCCCCCCCCCCCC  CCOCC  O
6  c i iCccCcCcCc cCcCiiiCcOcCcCO
5  CC  CCCCCCCCCC   CCCI   OCCCCO
4  cC_-cCccCc  Cc  _cCc_-_oOc_- o
3    --CCCCCCCCCC  -CCC - OCCC- O
2    _-cCcc_ CcCcC _cCc_-_oCc_- o
1    --     -      -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | GATE | RESET_B | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |
| NMOS2 |   |   |   | X | X |   | X |
| PMOS1 |   |   |   | X | X | X |   |
| PMOS2 |   |   |   |   |   | X |   |
| Poly1 | X | X |   |   | X |   |   |
| Poly10 |   |   |   |   | X |   |   |
| Poly11 |   |   |   |   | X |   |   |
| Poly3 |   |   | X |   | X |   |   |
| Poly4 |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   | X |   |   |
| Poly9 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | N |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O |   | S |   |   |   |   |   |   |   |   | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |
