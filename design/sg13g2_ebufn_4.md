# Design Documentation for sg13g2_ebufn_4

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
2 NpppppppNNNNpNNNpNNNNNNNNNN
1 NpppppppNNNNNNNNNNNNNNNNNNN
0 NpppppppNNNNNNNNNNpNNNpNNNN
9 NpppppppNNNNNNNNNNNNNNNNNNN
8 NpppppppNNNNNNNNNNNNpNpNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnSSSnSSSnSSnSnSnSSSS
3 SnnnnnnnSSSSSSSSSSSSSSSSSSS
2 SnnnnnnnSSSnSSSnSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2   G G G
1   G G G
0   G G G
9   G G G
8   GGG G
7   G G G
6   GGGGG
5   G G G
4   G G G
3   G G G
2   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +       +   +
2    +       +&  +&CcCcCcCcC
1  C +      C+ C + C   C   C
0  CCCCCCCc cCcCc+cCoOcCoOcC
9  C     CCCCC C   C O   O C
8  CII CCCc cCcCcCcC OoOoO
7  CI     C  CCCCCCCCCCC O
6  cIi IIcc     c c cCcC O
5  C   I  C CCCCCCCC OOOOO
4  C _ I  c c_ Cc_cCoOo oOcC
3  C - CCCC C- C - C   C   C
2    _    c  _   _ CcCcCcCcC
1    -       -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Z | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   | X |   |   |
| NMOS8 |   | X |   |   |
| NMOS9 |   | X |   |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 |   |
| NMOS4 |   |
| NMOS5 |   |
| NMOS6 |   |
| NMOS7 |   |
| NMOS8 |   |
| NMOS9 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
| PMOS5 |   |
| PMOS6 |   |
| PMOS7 |   |
| PMOS8 |   |
