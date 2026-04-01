# Design Documentation for sg13g2_ebufn_2

## Substrate
```
  012345678901234567
4 SSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3        p
2        p
1  ppppppppp ppppp
0  ppppppppp ppppp
9  ppppppppp ppppp
8  ppppppppp ppppp
7
6
5
4  nnnnnnnnn nnnnn
3  nnnnnnnnn nnnnn
2  nnnnnnnnn nnnnn
1
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
4
3
2   G G G G   G
1   G G G G   G
0   G G G G   G
9   G G G G   G
8   G G G G   G
7   G G GGGGGGG
6   G G       G G
5   G       G G G
4   G         G G
3   G         G G
2   G         G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3        +     +
2  c   c &c    +c
1  C   CCCCC   + C
0  c i c   CCCCCCCc
9    I C         C
8    c c    cC   Cc
7           C
6     CcCCC c i i
5           C
4  c i cCCc CCc-cCc
3  C   C -   C - C
2  cCCCc _c   c-c c
1        -     -
0 _-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Input4 | Internal1 | Internal2 | Internal5 | Internal6 | Internal7 | Internal8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X |   |   |   | X |   |   |   | X |   |
| NMOS3 |   | X |   |   |   |   |   | X |   |   |   | X |
| PMOS1 | X |   |   |   |   | X |   |   | X | X |   |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   | X |   |   |   | X | X |   |   | X |
| Poly3 |   | X |   |   | X |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |
| NMOS3 |   | O | O |   |   |
| PMOS1 | O | O |   |   | O |
| PMOS2 |   | O |   |   |   |
