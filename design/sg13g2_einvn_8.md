# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4 ppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678
4
3
2 G G                       G G
1 G G                       G G
0 G G                       G G
9 G G                       G G
8 G G                       G G
7 G G                       G G
6 GGG                     G GGG G G G G
5 G G                       G G
4 G G                       G G
3 G G                       G G
2 G G                       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++++++++++++++
2  +&    +& &+  &+  &+ CcCcCcCcCcCcCcCcC
1  ++C C + C + C++CC++ CC  C   C  CC  CC
0  +&c c +cC +cC&+cC&+ CcO CoOcCoOcCoOcC
9  ++C C + C + C++CC   CCO   O   O  OOCC
8  +&c c   Cc  C  cCcCcCcOoOoOoOoOoOoO
7  IIC CCCCCCCCCCCCC     OOO IIIIIIIIII
6  iIc  CccCcCcCcCcCcCcCcOoO iiIiIiIiIi
5  IICCCC   C   C  CC  CCOOOOOOOOOOOOOCC
4  c cCcCc  c   cc Ccc CcOoOoOoOoOoOoOcC
3    CCCC   C   C  CC  CCCCCCCCC  CC  CC
2  c cCc   c c   c   c CcCcCcCcCcCcCcCcC
1
0  c c c c c c c c c c c c c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS10 | VSS11 | VSS12 | VSS13 | VSS14 | VSS15 | VSS16 | VSS17 | VSS18 | VSS19 | VSS2 | VSS20 | VSS21 | VSS22 | VSS23 | VSS24 | VSS25 | VSS26 | VSS27 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | A | TE_B | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X | X | X | X | X | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   | X | X | X | X | X | X | X |   |   |   |
| NMOS2 |   | X |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   |   | X |
| PMOS1 | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O | O |   |   |   |   |   |
| PMOS1 | O | O |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |
