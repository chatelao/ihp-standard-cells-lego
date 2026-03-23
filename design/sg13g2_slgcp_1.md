# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppN
0 pppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2   G G               G G
1   G G               G G
0   G G G
9   G G G             G G
8 G G GGG
7 G G G G             G G
6 GGGGGGGGG G G G G G GGG G G
5 G G G G               G
4   G G G               G
3   G G G               G
2   G   G               G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +        +         +
2 &+  Cc&+        &         & o
1  +  CC +  CCCC  +CCCCCCCC + O
0 &+  CcCccCcCcC  &Cc c cCc & o
9       C CCCCCCCCCCCCC CCC + O
8    IIiCccCcCcCcCcCcCc cCcC  o
7  I    CCCCCCCC   CCC ICCCCCCO
6  i cCiCccCcCcCcCcCcCiicCcCcCO
5    CC CCCCCCCCCCCCCCC CCCC  O
4  _CcCcCcc cCcCcCcCcCc_  cC- o
3  -CCCCCCCCCCCCC-CCCCC-  CC- O
2  _   _  cCcCcCc_cCcCc_    -_o
1  -   -         -     -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | GATE | SCE | VSS | GCLK | VDD |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |   |   |
| NMOS2 |   |   |   | X | X |   |
| PMOS1 |   |   |   | X | X | X |
| PMOS2 |   |   |   |   |   | X |
| Poly1 |   | X | X | X |   |   |
| Poly2 | X |   |   | X |   |   |
| Poly3 |   |   |   | X |   |   |
| Poly4 |   |   |   | X |   |   |
| Poly5 |   |   |   | X |   |   |
| Poly6 |   |   |   | X |   |   |
| Poly7 |   |   |   | X |   |   |
| Poly8 |   |   |   | X |   |   |
| Poly9 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | S |   |   |   |   |   |   |   | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |
