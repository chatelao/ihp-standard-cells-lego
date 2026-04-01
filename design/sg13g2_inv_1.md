# Design Documentation for sg13g2_inv_1

## Substrate
```
  01234
4 SSSSS
3 NNNNN
2 NNNNN
1 NNNNN
0 NNNNN
9 NNNNN
8 NNNNN
7 NNNNN
6 NNNNN
5 SSSSS
4 SSSSS
3 SSSSS
2 SSSSS
1 SSSSS
0 SSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234
4 ppppp
3 ppppp
2 ppppp
1 ppppp
0 ppppp
9 ppppp
8 ppppp
7 ppppp
6 ppppp
5 nnnnn
4 Snnnn
3 SSSSS
2 SSSSS
1 SSSSS
0 nnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234
4
3
2  GG
1  GG
0  GG
9  GG
8  GG
7  GG
6  GG
5  GG
4  GG
3  GG
2  GG
1
0
```
Legend: G=Polysilicon

## Metal 1
GOLDEN STANDARD

```
  01234
4 &+&+&
3  +
2  & o
1  + O
0  & o
9  + O
8  & o
7    O
6  i O
5    O
4  _ o
3  - O
2  _ o
1  -
0 _-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Y |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| PMOS1 | X |   | X | X |
| Poly1 |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |

