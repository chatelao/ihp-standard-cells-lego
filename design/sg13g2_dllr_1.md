# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppNNpNNNNNNNNNppppppNNNNpNNN
1 NpppppppNNNNNNNNNNNNNpppppNNNNNNNN
0 NpppppppNNNNNNNNNNNNNppppppNNNpNpN
9 NpppppppNNNNNNNNNNNNNpppppNNNNNNNN
8 NpppppppNNNNNNNNNNNNNppppppNNNpNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnSSSSSSSSSSSSSnnnnnnSSSSSnS
3 SnnnnnnnSSSSSSSSSSSSSnnnnnSSSSSSSS
2 SnnnnnnnSSSnSSSSSSSnSnnnnnnSSnSSnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2   G G G               G
1   G G G               G
0   G G G               G
9   G G G               G G
8   G G G               G G
7   G G G               G G
6   GGGGG               GGG
5   G G G               G G
4   G   G               G
3   G   G               G
2   G   G               G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +      +        ++   +     +
2    +    c &  CcCc  +&   +     &
1  C + CCCCCCC C  C  ++ C + O   + O
0  C   CCCcCcCcCc c   c C + o c & o
9  CCCCCCC  CC CC C CCCCC   O C + O
8  C     Cc cCcCc c   cCCCCCoOc & o
7  C I I CC CC CCCCCC  C   C OC   O
6  c I I ccCcCcCcCcCcCcC I CcOcCcCO
5  C     CC      CCC   C     OC   O
4  C _- CCcCcCcCcCcCc-cC  - o c - o
3     - CCC -   CCCC -CC  - O C - O
2    _-     -_    c  _   _- o  _- o
1     -     -        -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 | X |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   | X |   |   |
| NMOS8 |   | X |   |   |
| PMOS2 | X |   | X |   |
| PMOS3 |   |   | X |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   |   | X |   |
| PMOS6 |   | X |   |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |
| PMOS9 |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   |   |
| NMOS4 |   |   |
| NMOS5 |   | O |
| NMOS6 |   |   |
| NMOS7 |   |   |
| NMOS8 |   |   |
| PMOS1 | O |   |
| PMOS2 |   | O |
| PMOS3 |   |   |
| PMOS4 |   |   |
| PMOS5 |   |   |
| PMOS6 |   |   |
| PMOS7 |   |   |
| PMOS8 |   |   |
| PMOS9 |   |   |
