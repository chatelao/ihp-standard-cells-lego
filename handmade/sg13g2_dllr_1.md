# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2   G G      G G G  G
1   G G      G G G  G
0   G G      G G G  G
9   G G      G G G  G
8   G G      G G G  G
7   G G      G G G  G
6   G G    GGG G G GG
5   G G      G G G G
4   G G      G GGG G
3   G G      G G G G
2   G G      G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +      +        +++   ++++++++
2     +  c   &+cCcCc  &+&   &     &
1   c +CCCCCCCCCC C +++ C + O C +OO
0   C &cCcc cCcCc c     c & o c &Oo
9   c CCCCCCCCCCC C CCCCC + O C +OO
8   Ci iC c cCcCc c cCcCcCc oOc &Oo
7   C  IC C CCCCCCCCC CC  C  OCCCCO
6  cIi iCciCcCcCcCcCcCcCiIcCoOcCcCo
5  C   CC CCCCCCCCCC  CCII   OC   O
4  cC_-cC cCcCcCcCcC_-cC -_OoOc _ o
3  CC--CC C --  CCCC--CC --OOOC - O
2    _-cC c _-  cCcC_-cC -_OoO  _ o
1     _      _-_    -           -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | D | GATE_N | RESET_B | Q | Q_N |
| ---   |---| --- | --- | --- | --- | --- | --- | --- | --- |
| PMOS1 | X |   | X | X | X | X |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X | X | X |   |   |   | X | X |
| Poly1 |   |   | X |   | X | X | X |   |   |
| Poly2 |   |   |   |   |   |   | X |   |   |
| Poly3 |   |   |   |   |   |   |   | X |   |
| Poly4 |   |   |   |   |   |   |   |   | X |
| Poly5 |   |   | X |   | X | X | X |   |   |
| Poly6 |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   |   | X |   |
| Poly8 |   |   |   |   |   |   |   |   | X |
| Poly9 |   |   |   |   |   |   |   | X |   |
| Poly10 |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PMOS1 | O | O |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   | O | O | O | O | O | O | O | O | O |
| NMOS1 | O | O |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | O | O | O | O | O | O |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   | O | O | O |
