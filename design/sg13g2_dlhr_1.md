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
2   G G G             G G
1   G G G             G G
0   G G G             G G
9   G G G             G G
8   G G G             G G
7   G G G             G G
6   GGGGG             GGG       G
5   G G G             G G
4   G G G             G G
3   G G G             G G
2   G G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++
2    &+     &CcCcC +&+  &+oO  &
1  CC++     +CCCCC +++CC++OOC +OO
0  cCcCcCccCcCcCcC    cC&+oOc &Oo
9  CC     CCCCCC CCCCCCC++OOC +OO
8  c   cC cCcCcCcCcCcCcCcCoOc  Oo
7  C I ICCCCCCCCCCCCCC IICCOC   O
6  c i iCccCcCcCc c cCciiCcOcCcCo
5  C    C CCCCCCC    C II  OC   O
4  cCc cC cCc  Cc    Cc c oOc cOo
3      CCCCCCC CC    C    O C  OO
2    c    c cCcCcCc  C  c o c cOo
1
0 c c c c c c c c c c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS10 | VSS11 | VSS12 | VSS13 | VSS14 | VSS15 | VSS16 | VSS17 | VSS18 | VSS19 | VSS2 | VSS20 | VSS21 | VSS22 | VSS23 | VSS24 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | D | GATE | RESET_B | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X | X | X | X | X | X |   |   |   | X |   |   |   |   |   | X | X | X | X | X | X | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   | X | X | X |   | X | X | X | X | X |   |   |   |   |   |   |   |   |   |   | X | X |
| PMOS1 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |
| Poly2 | X |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
