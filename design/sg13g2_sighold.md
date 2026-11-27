# Design Documentation for sg13g2_sighold

## Substrate
```
  012345678
4 NNNNNNNNN
3 SNNNNNNNN
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
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 ppppppppN
2 ppppppppN
1 ppppppppN
0 NNppppppN
9 ppppppppN
8 ppppppppN
7 NNNNNNNNN
6 SSSSSSSSS
5 SSSSSSSSS
4 nnnnnnnnS
3 SSnnSSSSS
2 nnnnnnnnS
1 nnnnnnnnS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2
1
0  GG
9  GG GG
8  GG GG
7  GG GG
6  GG GG
5  GG GG
4  GG GG
3  GG GG
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3 +++++++++
2   &&+&&+
1
0
9  C     I
8 Cc    Ii
7 CCIIIIII
6 CCcCc II
5 CCCCC II
4 Cc    Ii
3
2   _-_-_
1 ---------
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | SH |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |
| PMOS1 | X |   | X | X |
| Poly1 |   |   | X |   |
| Poly2 |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | O | O |
| PMOS1 | O | O |

