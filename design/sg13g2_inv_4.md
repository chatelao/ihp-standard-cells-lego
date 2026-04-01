# Design Documentation for sg13g2_inv_4

## Substrate
```
  01234567890
4 SSSSSSSSSSS
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 NNNNNNNNNNN
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 NNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3
2
1  ppppppppp
0  ppppppppp
9  ppppppppp
8  ppppppppp
7
6
5
4  nnnnnnnnn
3  nnnnnnnnn
2
1
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
4
3
2   G G
1   G G
0   G G
9   G G
8   G G
7   GGGGGG
6   GGGGGG
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
  01234567890
4 &+&+&+&+&+&
3  +   +   +
2  & c & cc+
1  + O + O +
0  & o & oc+
9  + O   O
8  c c   cO
7   IIIII O
6   IiIiIcO
5         O
4  _ oOOOoO
3  - O - O -
2  _ c _ cc-
1  -   -   -
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Output1 | Output2 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X |   | X |   |
| PMOS1 | X |   |   | X | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
