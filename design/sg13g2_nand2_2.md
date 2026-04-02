# Design Documentation for sg13g2_nand2_2

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
2   G G G G
1   G G G G
0   G G G G
9   G G G G
8   G G G G
7   G G GGG
6   GGG G G
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
  01234567890
4 &+&+&+&+&+&
3  +   +   +
2  & c & cc+
1  + O + O +
0  & oOOOoc+
9  +   O   +
8  &   O Ic
7    I O I
6    i O c
5        O
4  cCCCc ocC
3  C - C   C
2  c _ cCCcC
1    -
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Internal1 | Output1 | Output2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |
| NMOS2 |   |   |   |   | X | X |   |
| PMOS1 | X | X |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   |   |
| Poly2 | X | X |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
