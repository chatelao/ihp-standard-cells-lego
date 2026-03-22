# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 NNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4 pppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNN
2 NppppppppppppNpNNNpN
1 NppppppppppppNNNNNNN
0 NppppppppppppNNNpNpN
9 NppppppppppppNNNNNNN
8 NppppppppppppNNNpNpN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnSSSnSSS
3 SnnnnnnnnnnnnSSSSSSS
2 SnnnnnnnnnnnnnSSSSSn
1 SSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789
4
3
2   G    G G G
1   G    G G G
0   G G  G G G
9   G G  G G G
8   G G  G G G
7   G G  G G G
6   GGG  GGGGG
5   G G  G G G
4   G G  G G G
3   G G  G G G
2   G G  G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 &+&+&+&+&+&+&+&+&+&+
3     +        +    +
2     + CCCCCCC+&   &
1     + C     C+ OOO+
0  CCCCCC CC  C+cOoO&
9  C     CCC  C+ OOO+
8  C   CCC    C+ OoO&
7  CII C      C    O
6  cII cIii I cCcC O
5  C   CI   I CCCC O
4  C _ CIIIII C c oO-
3    - CCCCCCCC-  OO-
2    _         _    -_
1    -         -    -
0 -_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A0 | X | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   | X |   |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   |   | X |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   |   | X |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| NMOS3 |   |   |
| NMOS4 |   |   |
| PMOS1 | O | O |
| PMOS2 |   |   |
| PMOS3 |   |   |
| PMOS4 |   |   |
| PMOS5 |   |   |
| PMOS6 |   |   |
| PMOS7 |   |   |
| PMOS8 |   |   |
