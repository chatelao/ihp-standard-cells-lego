# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567
4
3
2   G G G               G G
1   G G G               G G
0   G G G               G G
9   G G G               G G
8   G G G               G G
7   G G G               G G
6   GGGGG               GGG G
5   G G G               G G
4   G G G               G G
3   G G G               G G
2   G G G               G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++
2    +&     &       &+&  +& oO
1  CC++CCC  +       +++CC++ OO
0  cC+&cCccCcCcCcCc &+&Cc+& oO
9  CC++CCCCC   CCCCCCCCCCCCCOO
8  cC+&cCccCcCcCcCcCcCcCcCcCoO
7  CIIIICCCCCCCCCCCCCC CIIICOO
6  cIIIICccCcCcCcCcC CcCiIiCoO
5  CC  CCCCCCCCCCCCC CCCIIICOO
4  cC  cCccCcC   CcCcCcCc - oO
3  CCCCCCCCCCC   CCC--CCC - OO
2    _-  c  -_-  Cc -_cCc_- oO
1 ----------------------------
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | RESET_B | VSS2 | Q | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   | X | X |   | X |
| PMOS1 |   | X | X | X |   |
| PMOS2 |   |   |   | X |   |
| Poly1 |   |   |   | X |   |
| Poly2 | X | X |   | X |   |
| Poly3 |   | X | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
