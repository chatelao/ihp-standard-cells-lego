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
2   G   G    G   G     G         G
1   G   G    G   G     G         G
0   G   G    G G G     G G       G
9   G   G    G G G     G G       G G
8   G   G    G G G     G G       G G
7   G G G    G G G     G G       G G
6  GGGGGGGG GGGGGGG G GGGGG G G GGGGG
5   G G G    G G G     G G       G
4   G G G    G G G       G       G
3   G   G    G   G       G       G
2   G   G    G   G       G       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     &        +&CcCcCcC& cCcCcCcCc &
1  CC +   CCC  +CCCCCCCC+ CCCC    C + O
0  cC &   cCcCcCcCcCcCcCcCcCcCcCcCc & o
9  CC +   CCCCCCCCCCCCCCCCCCCCCCCCCCCCO
8  cC &   cCc I I cCcCcC  cCcCcCcCcCcCo
7  C I I  CCC I I  CCCCCIICCCCCCC I CCO
6  c i iCccCcCi iCcCcCcCiIcCcCcCc i cCO
5  C    CCCCCC   CCCCCCCCCCCCCCCCCC  OO
4  cCcCcCccCcCcCcCcCcCc_cCcCcCcCcCc_ Oo
3  CC - CCCCC  -  CCCC -CCCCCCCCCCC- OO
2  cC_- CccCc  _  cCcC _cCcCcCcC   _  o
1     -        -       -           -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A0 | A1 | A2 | A3 | S0 | S1 | VSS | X | VDD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |   |   |
| NMOS2 |   |   |   |   |   |   | X | X |   |
| PMOS1 |   |   |   |   |   |   | X | X | X |
| PMOS2 |   |   |   |   |   |   |   |   | X |
| Poly1 | X |   |   |   | X |   | X |   |   |
| Poly2 |   | X | X |   |   |   | X |   |   |
| Poly3 |   |   |   | X |   |   | X |   |   |
| Poly4 |   |   |   |   |   | X | X |   |   |
| Poly5 |   |   |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |   |   |
| PMOS1 | O | O | O | O |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |
