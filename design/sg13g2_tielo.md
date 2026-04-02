# Design Documentation for sg13g2_tielo

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
3  ppp
2  ppppp
1    ppp
0  ppppp
9    ppp
8
7
6
5  nnnnn
4  nnnnn
3    nnn
2  nnnnn
1  nnn
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
0   G G
9   G G
8  GG G
7   GG
6   G  G
5   G G
4   G G
3   G G
2     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3   +
2  c+
1
0  c   c
9  C   C
8  c c c
7    C C
6    C c
5    C
4  cCC i
3      I
2  c- Ii
1   -
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Internal1 | Internal2 | Internal3 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   |   |
| PMOS1 | X |   |   |   | X | X |
| Poly1 |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   | X |
| Poly3 |   |   |   |   | X |   |
| Poly4 |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 | O | O | N |   |
| PMOS1 |   | O |   | O |
