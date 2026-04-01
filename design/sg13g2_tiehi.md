# Design Documentation for sg13g2_tiehi

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
3 pppp
2 pppppp
1    ppp
0 pppppp
9 pppppp
8 pppppp
7
6
5
4 nnnnnn
3    nnn
2    nnn
1    n
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
8     G
7     GG
6 GG G
5    GG
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
3
2  c
1
0      i
9      I
8  c   i
7  CCC C
6 Cc c c
5 C    C
4 Cc   c
3
2    _
1    -
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Internal1 | Internal2 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   | X | X |
| PMOS1 | X | X |   | X | X |   |
| Poly1 |   |   |   |   | X |   |
| Poly2 |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O |   |   |
| PMOS1 |   |   | O |
