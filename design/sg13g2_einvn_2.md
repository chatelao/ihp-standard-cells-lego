# Design Documentation for sg13g2_einvn_2

## Substrate
```
  0123456789012345
4 SSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3
2
1   ppp ppppppppp
0   ppp ppppppppp
9       ppppppppp
8       ppppppppp
7
6
5
4       nnnnnnnnn
3   nnn nnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3
2    G   G G
1    G   G G
0    G   G G
9    G   G G
8    G   G G
7    G   G G
6    G GGGGG GGGG
5    G   G G
4    G   G G
3    G   G G
2    G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3   +     +
2   +c c c& cCCCc
1   + C C + C   C
0   +cCcCc& c i c
9       C   C I C
8  IIi   c  c i c
7  III        I
6  IIi c      I i
5  III        I I
4       CcCCc i I
3   - C C - CCCCC
2   -c c c_ c   c
1   -     -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Internal10 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS3 |   |   | X |   |   |   | X |   |   |   |   |   |
| PMOS1 | X |   | X |   |   |   |   |   | X | X |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X | X |   |   | X |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   | X | X | X | X |   | X | X |
| Poly3 |   |   |   | X |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   | O |   |
| PMOS1 |   | O |   |
| PMOS2 | O |   |   |
| PMOS3 |   |   |   |
