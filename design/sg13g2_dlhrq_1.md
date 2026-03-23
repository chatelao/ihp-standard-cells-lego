# Design Documentation for sg13g2_dlhrq_1

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
2 G G   G
1 G G   G             G
0 G G G G
9 G G G G             G
8 G G G G
7 G G G G             G G
6 GGGGGGGGG G G G G G GGG G
5 G G G G             G G
4 G G G G
3 G G   G             G
2 G G   G             G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +      +       +   +
2  cC+&     &CcCcC  & cC& o
1  CC+      +CCCCC  + CC+ OO
0  cCcCcCccCcCcCcCcCcCcC& oO
9  CCC CCCC CCCCCCCCCCCC+ OO
8   Cc cCcc cCcCcCcCcCcC& oO
7  ICCIICCC CCCCCCCCCCCI CCO
6  iCcIiCcc cCcCcCc cCciiCcO
5 CCCC CCCCCCCCCCCC CCCCCCCO
4 CcCc cCccCcCcCcC  cCc_cCoO
3 CC  -CCCCCCCCCCC -CC  - OO
2    _-cC  _-CcCcC _cC _-
1     -     -      -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | GATE | RESET_B | VSS | Q | VDD |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |   |   |
| NMOS2 |   |   |   | X | X |   |
| PMOS1 |   |   |   | X | X | X |
| PMOS2 |   |   |   |   |   | X |
| Poly1 | X | X |   | X |   |   |
| Poly3 |   |   | X | X |   |   |
| Poly4 |   |   |   | X |   |   |
| Poly5 |   |   |   | X |   |   |
| Poly6 |   |   |   | X |   |   |
| Poly7 |   |   |   | X |   |   |
| Poly8 |   |   |   | X |   |   |
| Poly9 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | N |   |   |   |   |   |   |   |   |
| PMOS1 | O |   | S |   |   |   |   |   |   | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |
