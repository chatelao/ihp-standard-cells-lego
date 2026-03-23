# Design Documentation for sg13g2_nor2b_2

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NppppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 Snnnnnnnnnnn
3 SnnnnnnnnnnS
2 Snnnnnnnnnnn
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2 G
1 G G     G
0 G G
9 G G     G
8 G G
7 G G     G G
6 GGGG    GGG
5 G G     G
4 G G
3 GGG     G
2 G G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +       +
2   &+CcCccC&+
1  C +CCCCCC +
0  c +Cc ocC&+
9  C +   OCC +
8  c   oOocC&
7  CCCCO  III
6  cCcCO  iii
5  C   OOOOO
4  c _ o _oO _
3  i - O - O -
2  I _   _   _
1    -   -   -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B_N | VSS | Y | VDD |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |
| NMOS2 |   |   | X | X |   |
| PMOS1 |   |   | X | X | X |
| PMOS2 |   |   |   |   | X |
| Poly1 |   | X | X |   |   |
| Poly3 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | N |   |   |
| PMOS1 | O |   | S | O | O |
| PMOS2 |   |   |   |   |   |
