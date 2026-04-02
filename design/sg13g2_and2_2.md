# Design Documentation for sg13g2_and2_2

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
8      ppppp
7
6
5  nnnnnnnnn
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
2   G
1   G
0   G
9   G
8   G
7   GG GGG
6   GG GGG
5   G
4   G
3   G
2 GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  +   +  +
2  & c & c&
1  + C + O+
0  & c & o&
9    C   O+
8  CCCCC oc
7  C   C O
6  C i c O
5  C     O
4  c   _ o_
3 III  - O-
2 IiI  -  -
1      -  -
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Internal1 | Output1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   |   | X | X |
| PMOS1 | X |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X | X |   |   |
| Poly2 |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | N |
| PMOS1 | O | S |
| PMOS2 |   |   |
