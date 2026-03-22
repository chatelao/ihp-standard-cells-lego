# Design Documentation for sg13g2_dlhrq_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2 G G G G             G G
1 G G G G             G G
0 G G G G             G G
9 G G G G             G G
8 G G G G             G G
7 G G G G             G G
6 GGG GGG             GGG
5 G G G G             G G
4 G G G G             G G
3 G G G G             G G
2 G G G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +      +       +   +
2    +&     & cCcC  &   &
1  C +      + C  C  + C + OO
0  cCcCcCccCc cCcC  c c & oO
9  CCC CC C C CC C CCCC + OO
8    c cCcc c cCcCcCc C   oO
7  I CIICCC CCC C   C CI   O
6  I cIICcc c c cCc   cI CcO
5  CCC  C CCCCC CC   CCCCC O
4  c   cCccCcC CcC  cCc   oO
3     - C     C  C - C  - OO
2    _-     - cCcC _   _-
1     -     -      -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Internal1 | Q | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 | X | X |   | X |
| PMOS1 | X | X | X |   |
| PMOS2 |   |   | X |   |
| Poly2 |   |   | X |   |
| Poly3 | X |   | X |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS2 | Poly1 |
| NMOS2 | Poly2 |
| NMOS2 | Poly3 |
| PMOS1 | Poly1 |
| PMOS1 | Poly2 |
| PMOS1 | Poly3 |
