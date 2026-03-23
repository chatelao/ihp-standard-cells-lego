# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2       G         G
1       G         G
0     G G
9     G G         G G
8     G G           G
7     GGG         GGG
6  G GGGGGG G G G G G G G
5     G G         G
4     G G         G
3       G         G
2       G         G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +        +     +   +
2  cC+&       &     &   & o
1  CC+  CCC  CCCCCC +CC + O
0  cCcCcCcc cCcCcCc &Cc & o
9  CCCCCCCCCCCCCCCC  CCC+ O
8  cCc I ccCcCcCcCcI CcC& o
7  CCC i CCCCCCCCCCiI CCCCO
6  cCcCiCccCcCcCcCc i cCcCO
5  CCCCCCCCCCCCCCCC-  CC  O
4  cCcCcCcc  _-_c  _  cC _o
3  CC CCCCC CC-CC  -  CC -O
2  cC_CcCccCcC-_   _     _o
1    -        -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | GATE | GCLK | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   |   | X |   | X |
| PMOS1 |   |   | X | X | X |
| PMOS2 |   |   |   | X |   |
| Poly1 |   | X |   |   | X |
| Poly2 | X |   |   |   | X |
| Poly3 |   |   |   |   | X |
| Poly4 |   |   |   |   | X |
| Poly5 |   |   |   |   | X |
| Poly6 |   |   |   |   | X |
| Poly7 |   |   |   |   | X |
| Poly8 |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O |   |   |   |   |   |   |   |   |
| PMOS1 | O | O |   |   |   |   |   |   | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |
