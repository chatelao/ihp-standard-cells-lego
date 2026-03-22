# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppNNpNNNNNNNpppppppNNNpNNN
1 NpppppppNNNNNNNNNNNpppppNNNNNNNN
0 NpppppppNNNNNNNNNNNppppppNNNpNpN
9 NpppppppNNNNNNNNNNNpppppNNNNNNNN
8 NpppppppNNNNNNNNNNNppppppNNNNNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnSSSSSSSSSnSnnnnnnSSSSSnS
3 SnnnnnnnSSSSSSSSSSSnnnnnSSSSSSSS
2 SnnnnnnnSSSSSSSSSnSnnnnnnSSnSSnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2   G   G             G G
1   G   G             G G
0   G G G             G G
9   G G G             G G
8   G G G             G G
7   G G G             G G
6   GGGGG             GGG
5   G G G             G G
4   G   G             G
3   G   G             G
2   G   G             G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +      +++   +    +
2     +     & CCcC +&+   +&   &
1     +     + C  C +++ C +OOC + O
0  CCCCCCCcCc cCcC  c  C +oOc & o
9  C        C C CC CCCCC  OOC + O
8  C    CCcCc c c  CcCCCCCoOc   o
7  C I I C CCCC CCCCC C  C OC   O
6  c I I ccCcCc c c c CI CcOcCcCO
5  C     CCCCCCCC     CI   OC   O
4  C _-CCCcCc  Cc  _cCC - oOc - o
3    --CCCCCCCC    - CC - O C - O
2    _-   c   cCcC _ CC_- o c_- o
1    --     -      -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 | X |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   | X |   |   |
| NMOS7 |   |   |   | X |
| NMOS8 |   | X |   |   |
| PMOS2 | X |   | X |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   |   | X |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   |   |
| NMOS4 |   | O |
| NMOS5 |   |   |
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
