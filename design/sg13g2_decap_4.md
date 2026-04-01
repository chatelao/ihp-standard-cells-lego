# Design Documentation for sg13g2_decap_4

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
1 ppppppp
0 ppppppp
9 ppppppp
8
7
6
5
4
3 nnnnnnn
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
2   GGG
1   GGG
0   GGG
9   GGG
8   GGG
7   G
6   G G
5     G
4   GGG
3   GGG
2   GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3 +   +++
2 +c  +&+
1 +   +++
0 +c  +&+
9 +   +++
8  c  +c
7     +
6   -c+c
5   -
4   -
3 ---   -
2 -_-  c-
1 ---   -
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| NMOS2 |   |   |
| PMOS1 | X |   |
| PMOS2 | X |   |
| Poly1 |   |   |
| Poly2 |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 |   | O |
| PMOS2 |   |   |
