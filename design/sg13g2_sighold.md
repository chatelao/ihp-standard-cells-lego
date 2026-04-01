# Design Documentation for sg13g2_sighold

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
```
  012345678
4 ppppppppp
3  ppppppp
2  ppppppp
1  ppppppp
0
9  ppppppp
8  ppppppp
7
6
5
4  nnnnnnn
3
2  nnnnnnn
1  nnnnnnn
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
4
3
2
1
0
9     GG
8     GG
7   G GG
6     GG
5     GG
4     GG
3     GG
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3   +++++
2   +&+&+c
1
0
9
8  c     i
7  CIIIIII
6  C c   I
5  CCCC  I
4  c     i
3
2   -_-_-
1   -----
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Internal1 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   |   | X |   | X |
| PMOS1 |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   |   |   |   |
| Poly2 |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O |   |
| PMOS1 | O | S |
| PMOS2 |   |   |
