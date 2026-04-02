# Design Documentation for sg13g2_buf_2

## Substrate
```
  012345678
4 SSSSSSSSS
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 NNNNNNNNN
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 NNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
GOLDEN STANDARD

```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 NpppppppN
1 NpppppppN
0 NpppppppN
9 NpppppppN
8 NpppppppN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SnnnnnnnS
3 SnnnnnnnS
2 SnnnnnnnS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
GOLDEN STANDARD

```
  012345678
4
3
2
1
0   G   G G
9   G   G G
8   G   G G
7   G   G G
6   G   G G
5   G   G G
4   G   G G
3   G   G G
2   G   G G
1
0
```
Legend: G=Polysilicon (at X=3, 7, 8)

## Metal 1
GOLDEN STANDARD

```
  012345678
4 &+&+&+&+&
3  +   +
2  &   &
1  +   +
0  &   &   C
9  C   C   C
8  C   OC  C
7  C   OC II
6  COOOOI i
5      O CCC
4    - O   C
3    - O-  C
2    -  _
1    -  -
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, C=Internal Connection (uppercase used for all to simplify)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | Input1 | Internal1 | Internal2 | Internal3 | Output1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   |   | X |   | X |   |   | X |
| PMOS1 | X |   |   |   |   | X |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   | X |   |   |   |   |

