# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 NNNNNNNNNNNNNN
2 NNppppppppNNpN
1 NNNpppppppNNNN
0 NNNppppppppNpN
9 NNNpppppppNNNN
8 NNNppppppppNpN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnSnnnnnnnSSnS
3 SSSnnnnnnnSSSS
2 SnSnnnnnnnSSSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2     G   G
1     G   G
0     G   G
9     G G G
8     G G G
7     G G G
6     GGGGG
5     G G G
4     G G G
3     G G G
2     G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +    +     +
2  +&   +     &
1  +  C +   O +
0  &  C +   o &
9  + CC     O
8    C IIIIIoOoO
7    C III I   O
6    c IIiiIcC O
5  - CCCCCCCCC O
4  _ CC CCCCc oO
3  -    CC  C OO
2  _      -
1  -      -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | B | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   | X |   |   |
| PMOS1 |   | X | X |   |
| PMOS2 |   | X |   |   |
| PMOS3 |   |   | X |   |
| PMOS4 |   |   | X |   |
| PMOS5 |   |   | X |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 |   |
| NMOS3 | O |
| NMOS4 |   |
| NMOS5 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
| PMOS5 |   |
