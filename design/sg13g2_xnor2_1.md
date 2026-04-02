# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 SSSSSSSSSSSSSS
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 NNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3
2
1  pppppppppppp
0  pppppppppppp
9  pppppppppppp
8  pppppppppppp
7
6
5  nnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2         n
1
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
4
3
2            G
1    G       G
0    G       G
9    G       G
8    G       G
7   G        G
6   G GG G G G
5   G
4   G
3   G
2   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +    +     +
2  +    +c  c &
1  +    +   O +
0  & cC +c  o &
9  + CC     O
8    C IIII oOO
7    C III
6    C iIicI Cc
5  - C
4  _ CCc c  c o
3  -    CC  C O
2  -      _   c
1  -      -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Internal1 | Internal2 | Internal3 | Output1 | Output2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   | X |   | X | X | X | X |   |
| PMOS1 | X |   |   |   |   | X |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |
| Poly2 |   |   | X |   |   |   |   |   |
| Poly3 |   |   | X |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 | O | N |   |   |   |   |
| PMOS1 | S |   |   |   | O | O |
| PMOS2 |   |   |   |   |   |   |
