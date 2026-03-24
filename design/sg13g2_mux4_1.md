# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 ppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppN
0 Npppppppppppppppppppppppppppppppppppp
9 NpppppppppppppppppppppppppppppppppppN
8 Npppppppppppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3
2   G G G    G G G     G G       G G
1   G G G    G G G     G G       G G
0   G G G    G G G     G G       G G
9   G G G    G G G     G G       G G
8   G G G    GGGGG     G G       G G
7   G G G    G G G     G G       G G
6   GGGGG    GGGGG     GGG       GGG  G
5   G G G    G G G     G G       G G
4   G G G    G G G     G G       G G
3   G G G    G G G     G G       G G
2   G G G    G G G     G G       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++++++++++++
2    +&        +&CcCcCcC&+cCcCcCcCc+&
1  CC++   CCC  +CCCCCCCC++CCCC    C++OO
0  cC+&   cCcCcCcCcCcCcCcCcCcCcCcCc+&Oo
9  CC++   CCCCCCCCCCCCCCCCCCCCCCCCCCCOO
8  cC+&   cCcIiIiIcCcCcC  cCcCcCcCcCcOo
7  CIIII  CCCIIIII CCCCCIICCCCCCCIIICOO
6  cIIIICccCcIIIIIcCcCcCIIcCcCcCcIIIcOo
5  CIIIICCCCCIIIIICCCCCCCCCCCCCCCCC--OO
4  cCcCcCccCcCcCcCcCcC__cCcCcCcCcCc_-Oo
3  CC-- CCCCC --  CCCC--CCCCCCCCCCC--OO
2  cC_- CccCc -_  cCcC-_cCcCcCcC   _-Oo
1 -------------------------------------
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A2 | VSS2 | X | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   | X | X |   | X |
| PMOS1 | X | X | X | X |   |
| PMOS2 |   |   |   | X |   |
| Poly1 |   |   |   | X |   |
| Poly2 | X |   |   |   | X |
| Poly3 |   | X |   |   | X |
| Poly4 |   |   |   |   | X |
| Poly5 |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |
| PMOS1 | O | O | O | O |   |
| PMOS2 |   |   |   |   |   |
