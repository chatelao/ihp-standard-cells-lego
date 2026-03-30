# Design Documentation for sg13g2_sighold

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
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
3 ppppppppp
2 ppppppppp
1 ppppppppp
0 ppppppppp
9 ppppppppp
8 ppppppppp
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 nnnnnnnnn
3 nnnnnnnnn
2 nnnnnnnnn
1 nnnnnnnnn
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678
4
3
2  G
1  G
0  G
9  G
8  G
7  G
6  G
5  G
4  G
3  G
2  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 +++++++++
3   +++++
2   +++++
1
0     &
9  C     C
8  C  c  C
7  CCCCCCC
6  c     c
5  CCCC  C
4  C  _  C
3
2   -----
1   -----
0 ---------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS2 | SH |
| --- | --- | --- | --- |
| NMOS1 |   | X |   |
| PMOS1 | X |   | X |
| Poly1 |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| PMOS1 | O |
