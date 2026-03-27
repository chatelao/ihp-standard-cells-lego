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
2   G G GG G
1   G G GG G
0   G G GG G
9   G G GG G
8   G G GG G
7   G G GG G
6   GGGGGGGG            G   G
5   G G GG G
4   G G GG G
3   G G GG G
2   G G GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++
2    &+     &       &+&   &
1    ++     +       +++ C + OO
0  c &+ CccC CcCcCc &+& c & oO
9  C ++ CCCC   CCCCC   CCC  OO
8  c &+ CccCcCcCcCcCcCcC  c oO
7  C   I C CCCCCCCCCCC  II C O
6  c i i  i cCcCcCc  Cc iI  oO
5  CC   CC CCCCCCCC  CC II   O
4  cC  cCccCcC   CcCcCcC  _ oO
3  CC  CCCCC     CC   CC  - OO
2    _-     _-_     _-    _
1 ----------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | GATE_N | RESET_B | Q |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   |   |   | X |
| PMOS1 | X |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X | X | X | X |
| Poly2 |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| PMOS1 | O |   |   |
| PMOS2 |   |   |   |
