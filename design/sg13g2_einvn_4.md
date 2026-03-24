# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppN
1 NpppppppppppppppppppppN
0 NpppppppppppppppppppppN
9 NpppppppppppppppppppppN
8 NpppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnnnnnnnnn
3 SnnnnnnnnnnnnnnnnnnnnnS
2 Snnnnnnnnnnnnnnnnnnnnnn
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2 G G             G G
1 G G             G G
0 G G             G G
9 G G             G G
8 G G             G G
7 G G             G G
6 GGG             GGG G
5 G G             G G
4 G G             G G
3 G G             G G
2 G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++
2  +&cCcC+&Cc+&CcCcCcCcC
1  ++CCCC++CC++CC  C  CC
0  +&cCcC+&Cc+&CcOoCoOcC
9  ++CCCC++CC++CCOOOOOCC
8  +&cCcC+&Cc+&CcOoOoOcC
7  IICCCCCCCCCCCCOOIIII
6  IIcC CccCcCcCcOoIiIi
5  IICC CCCCCCCCCOOOOOO
4  _-cCcCc-_cC-_cOoOoOoCc
3  --CCCCC--CC--CCCCCOOCC
2  _-cCcCc-_cC-_cCcCcCcCc
1 -----------------------
0 -_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | VSS2 | Z | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   | X | X |   | X |
| PMOS1 |   | X | X | X |   |
| PMOS2 |   |   |   | X |   |
| Poly1 |   |   |   | X |   |
| Poly2 | X | X | X |   |   |
| Poly3 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
