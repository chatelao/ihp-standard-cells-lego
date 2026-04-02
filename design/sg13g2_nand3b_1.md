# Design Documentation for sg13g2_nand3b_1

## Substrate
```
  012345678901
4 SSSSSSSSSSSS
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 NNNNNNNNNNNN
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 NNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3
2
1     ppppppp
0   ppppppppp
9   ppppppppp
8   ppppppppp
7
6
5   nnnnnnnnn
4   nnnnnnnnn
3   nnnnnnnnn
2
1
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3
2      G G G
1    G G G G
0    G G G G
9    G G G G
8    G G G G
7    G G G G
6    G G G G
5      G G G
4      G G G
3      G G G
2      G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3     +   +
2     +c c& c
1     + O + OO
0   Cc+cOc& oO
9   C + O   OO
8    c c c  cO
7    I I I   O
6    i i i CcO
5          C O
4  cCCCCCCCCoO
3     -     OO
2    c-     c
1     -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Input3 | Internal2 | Internal3 | Output1 | Output2 | Output3 | Output4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS1 | X | X |   |   |   |   | X | X | X | X | X |   |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X | X |   |   | X |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   | X |   |   |   | X | X | X |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   | X |   |   | X | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O | O | N |
| PMOS1 | O | O | O | O |
| PMOS2 |   |   |   |   |
