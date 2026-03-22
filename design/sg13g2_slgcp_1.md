# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 ppppppppNNNNNNNNpNNpppppNNpNNN
1 ppppppppNNNNNNNNNNNpppppNNNNNN
0 ppppppppNNNNNNNNNNNpppppNNpNpN
9 ppppppppNNNNNNNNNNNpppppNNNNNN
8 ppppppppNNNNNNNNNNNpppppNNNNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnnnnnSSSSSSSSSSSnnnnnSSSSnS
3 nnnnnnnnSSSSSSSSSSSnnnnnSSSSSS
2 nnnnnnnnSSSSSSSnSSSnnnnnSSSnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2 G G G G             G G
1 G G G G             G G
0 G G G G             G G
9 G G G G             G G
8 G G GGG             G G
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
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +        +         +
2  +     +        &         &
1  +   C +        + CCCCC C + O
0  +   CCCcCcC C    c   C c & o
9       C    C C    CCC  CC + O
8    IIIC cC  cCcCcCcC   CcC  o
7  I    C CCCCCC    CC I C C  O
6  I cCiCcc c cCcCc cC I CcCcCO
5     C  CCCC C CCC CC     C  O
4  _ CC   c c c c cCcC _  cC- o
3  - CCCCCCCCCC C-C  C -  CC- O
2  _   _  c cCcCC_cCcC _    -_
1  -   -         -     -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Input1 | GCLK | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   | X |   |   |
| PMOS3 |   | X |   |   |
| PMOS4 |   |   | X |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| NMOS3 |   |   |   |
| NMOS4 |   |   | O |
| NMOS5 |   |   |   |
| NMOS6 |   |   |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   | O |
| PMOS3 |   |   |   |
| PMOS4 |   |   |   |
| PMOS5 |   |   |   |
| PMOS6 |   |   |   |
| PMOS7 |   |   |   |
| PMOS8 |   |   |   |
