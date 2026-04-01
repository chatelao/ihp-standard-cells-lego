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
3 NpppppppN
2 NpppppppN
1 NpppppppN
0 NNNNNNNNN
9 NpppppppN
8 NpppppppN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SnnnnnnnS
3 SSSSSSSSS
2 SnnnnnnnS
1 SnnnnnnnS
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
2   +++++
1
0
9  C     C
8  c   c c
7  CCCCCCC
6  c     c
5  CCCC  C
4  c     c
3
2   -----
1   -----
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | SH |
| --- | --- | --- | --- |
| NMOS1 |   | X |   |
| NMOS2 |   |   | X |
| PMOS1 |   |   | X |
| PMOS2 | X |   |   |
| Poly1 |   |   | X |
| Poly2 |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O |   |
| PMOS1 | O | S |
| PMOS2 |   |   |
