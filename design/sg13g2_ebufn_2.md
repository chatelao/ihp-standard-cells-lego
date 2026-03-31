# Design Documentation for sg13g2_ebufn_2

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3 pppppppppppppppppp
2 pppppppppppppppppp
1 pppppppppppppppppp
0 pppppppppppppppppp
9 pppppppppppppppppp
8 pppppppppppppppppp
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnSnnnnnSS
3 SnnnnnnnnnSnnnnnSS
2 SnnnnnnnnnSnnnnnSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901234567
4
3
2 G G GGG G G G G G
1 G G GGGGG G G G G
0 G G GGGGG G G G G
9 G G GGGGG G G G G
8 G G GGGGG G G G G
7 G G GGGGG G G G G
6 G G GGGGG G G G G
5 G G GGGGG G G G G
4 G G GGGGG G G G G
3 G G GGG G G G G G
2 G G GGG G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 ++++++++++++++++++
3        +     +
2  CcCcC&+&    +&
1  C   CCCCC   + CC
0  C OoCc  CcCcCcCc
9    O C   C     CC
8    O C  cCcC   Cc
7    O     CC     C
6    oCiCccCc i i c
5    O      C I I C
4  CoO CcCc cCc- Cc
3  C   C -C  C - CC
2 cCcCcC_-_  C -_
1        -     -
0 ------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Internal2 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   | X |   |   | X |   | X |
| NMOS3 |   | X |   |   |   | X |   |
| PMOS1 | X |   |   |   |   | X | X |
| Poly1 |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   | X | X | X |
| Poly3 | X | X |   | X | X | X | X |
| Poly4 |   |   |   |   |   | X |   |
| Poly5 |   |   |   | X |   | X |   |
| Poly6 | X | X | X |   |   | X |   |
| Poly7 |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | W | O | O | E |   |   |   |
| NMOS3 |   |   |   | W | O | O | E |
| PMOS1 | O | O | O | O | O | O | O |
