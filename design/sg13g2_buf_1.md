# Design Documentation for sg13g2_buf_1

## Substrate
```
  0123456
4 SSSSSSS
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 NNNNNNN
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 NNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
4 ppppppp
3
2
1  ppppp
0  ppppp
9  ppppp
8    ppp
7
6
5
4  nnnnn
3  nnnnn
2
1
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
4
3
2     G
1     G
0     G
9     G
8  G  G
7     G
6    GG
5     G
4     G
3     G
2     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3    +
2  c & c
1  C + O
0  c   o
9    C O
8  iIC o
7    C O
6    cCO
5  CCC O
4  c c o
3    - O
2    - c
1    -
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Internal1 | Internal2 | Output1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   | X |   | X |
| PMOS1 |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   |
| Poly2 |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O | S |
| PMOS2 |   |   |
