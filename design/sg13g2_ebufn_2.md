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
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNpppppppN
1 NNNNNNNNNNpppppppN
0 NNNpNNNNNNpppppppN
9 NNNNNNNNNNpppppppN
8 NNNNNNNNNNpppppppN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSnSSSSSSnnnnnnnS
3 SSSSSSSSSSnnnnnnnS
2 SSSSSSSnSSnnnnnnnS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3
2            G   G
1            G   G
0            G G G
9            G G G
8            G G G
7            G G G
6            GGGGG
5            G G G
4            G   G
3            G   G
2            G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3        +     +
2  cCcCc +c    +&
1  C   CCCCC   + CC
0  c o c ccCCCCCCCC
9    O C   C     CC
8    O    cCCC   CC
7    O     CC     C
6    OCcCccCc I I c
5    O      C     C
4  c o cCcc CC - CC
3  C   C -C  C - CC
2  cCcCc _c    -
1        -     -
0 -_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Z | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS4 | X |   |   |
| PMOS1 |   | X |   |
| PMOS2 | X |   |   |
| PMOS3 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 |   |
| NMOS3 | O |
| NMOS4 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
