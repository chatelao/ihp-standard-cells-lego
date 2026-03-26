# Design Documentation for sg13g2_buf_8

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
2 Npppppppppppppppppppppp
1 NpppppppppppppppppppppN
0 Npppppppppppppppppppppp
9 NpppppppppppppppppppppN
8 Npppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2   G G
1   G G
0   G G
9   G G
8   G G
7   G G
6   GGGG              G
5   G G
4   G G
3   G G
2   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++
2   &+  &   &   &  +&  +&
1 CC++CC+ O + O +OO++OO++
0 Cc&+Cc& o & o &Oo+&Oo+&
9 CCCCCCC OOOOOOOOOOOOO++
8 CcCcCcC oOoOoOoOoOoOo+&
7   IIIIC            OO
6   IiIiCccCcCcCcCcCcOoO
5       C            OO
4 CcCcCcC oOoOoOoOoOoOoc
3 CC  CC  O   O  OO  OO
2 Cc cCc co  coc Ooc Ooc
1
0  c c c c c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS10 | VSS11 | VSS12 | VSS13 | VSS14 | VSS15 | VSS16 | VSS17 | VSS18 | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | A | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X | X | X |   |   |   |   |   |   |   | X | X | X | X | X | X | X | X |   |   |
| NMOS2 |   | X |   |   |   | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   |   | X |
| PMOS1 | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
