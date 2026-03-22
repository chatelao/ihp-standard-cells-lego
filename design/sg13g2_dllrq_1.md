# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppNNpNNNNNNNpNppppppNN
1 NpppppppNNNNNNNNNNNNNpppppNN
0 NpppppppNNNNNNNNNNpNpppppppN
9 NpppppppNNNNNNNNNNNNNpppppNN
8 NpppppppNNNNNNNNNNNNNppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnSSSSSSSSSSSSSnnnnnnS
3 SnnnnnnnSSSSSSSSSSSSSnnnnnSS
2 SnnnnnnnSSSSSSSSSSSnSnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567
4
3
2   G   G               G
1   G   G               G
0   G   G               G
9   G   G               G G
8   G   G               G G
7   G G G               G G
6   GGGGG               GGG
5   G G G               G G
4   G G G               G
3   G G G               G
2   G G G               G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +       +++   +
2     +     &       &+&   +
1     +             +++ C + OO
0  CC + CCcCcCcCcCc &+& C + oO
9  CC + CC     CC C CCCCCCCCOO
8  CC + CCcCcCCCc c cCcC   CoO
7  C I I C C  CCCCCCCC C I C O
6  c I I ccCcCcCc c  CcC I CcO
5  CC    C CCCCCCCC  C C I   O
4  CC   CCcCcC   CcCcCcC  - oO
3  CCCCCCCCCCC   C     C  - OO
2         c          _ C _- oO
1     -     ---      -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Q | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS3 |   |   | X |
| NMOS4 | X |   | X |
| PMOS2 | X | X |   |
| PMOS3 |   | X |   |
| PMOS4 |   | X |   |
| PMOS5 |   | X |   |
| PMOS6 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   |   |
| NMOS4 |   | O |
| PMOS1 | O |   |
| PMOS2 |   | O |
| PMOS3 |   |   |
| PMOS4 |   |   |
| PMOS5 |   |   |
| PMOS6 |   |   |
