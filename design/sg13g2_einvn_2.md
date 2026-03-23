# Design Documentation for sg13g2_einvn_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 NNNNNNNNNNNNNNNN
2 NppppppppppppppN
1 NppppppppppppppN
0 NppppppppppppppN
9 NppppppppppppppN
8 NppppppppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2 G            G G
1 G            G G
0 G            G G
9 G G          G G
8 G G          G G
7 G G          G G
6 GGGG G       GGG
5 G G          G G
4 G G          G G
3 G            G G
2 G            G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3   +     +
2   & CcC &CcCcCc
1   + CCC +CC  CC
0   & CcCc&Cc oCc
9     CCCCCCC OCC
8  IIICcCccCc oCc
7  IIICCC     O
6  iIiCcC     O i
5  IIICC      O I
4     CcCccCc o I
3   - CCCC-CCCCCC
2   -_CcC_-CcCcCc
1   -     -
0 -_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | TE_B | VSS | Z | VDD |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |
| NMOS2 |   |   | X | X |   |
| PMOS1 |   |   | X | X | X |
| PMOS2 |   |   |   |   | X |
| Poly1 |   | X |   |   |   |
| Poly2 | X |   |   |   |   |
| Poly3 |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
