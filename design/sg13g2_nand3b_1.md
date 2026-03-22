# Design Documentation for sg13g2_nand3b_1

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
4 SnnnnnnnnnnS
3 SnnnnnnnnnnS
2 SnnnnnnnnnnS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2   G G G G
1   G G G G
0   G G G G
9   G G G G
8   G G G G
7   G G G G
6   GGGGGGG
5   G G G G
4   G G G G
3   G G G G
2   G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3     +   +
2     &   &
1     + O + OO
0  cC & Oo& oO
9   C + OOOOOO
8  cC     o oO
7   CI I I   O
6   CI I IcCcO
5   C      C O
4  cCcCcCccCoO
3     -     OO
2    _-
1     -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Internal3 | Internal1 | VDD | Internal2 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 | X | X |   | X |
| PMOS1 | X | X | X |   |
| PMOS2 |   |   | X |   |
| Poly1 | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS2 | Poly1 |
| PMOS1 | Poly1 |
