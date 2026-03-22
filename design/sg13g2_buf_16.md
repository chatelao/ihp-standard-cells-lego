# Design Documentation for sg13g2_buf_16

## Substrate
```
  01234567890123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pNNNpNNNpNNNpNNNpNNNpNNNpNNNpNNNpNpNNppppppN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNpppppNN
0 NNNpNNNppNpNpNpNpNpNpNpNpNpNNNpNNNNNNppppppN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNpppppNN
8 NNNpNpNppNpNNNpNNNpNpNpNNNNNNNNNNNNNNpppppNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnSnSnSnSnnSSSnSSSnSSSnSnSnSnSnSSSSSSnnnnnSn
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnSS
2 SnSSSnSSSnSSSnSSSnSnSSSnSSSnSSSnSSSnSnnnnnSn
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2                                       G G
1                                       G G
0                                       G G
9                                       G G
8                                       G G
7                                       G G
6                                       GGG
5                                       G G
4                                       G G
3                                       G G
2                                       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +   +  ++  +   +   +   +  +   +   +   +  ++
2 &+  &+  &+  &   &   &   &  +&  +& &+   +  &+
1  + O + O++O + O + O + O + O+ O + C + C + C++
0  + o + o&+o & o & o & o & o+ Oo+ Cc+cC + C&+
9  + OOOOO++OOOOOOOOOOOOOOOOOOOO CCCCCCCCCCC++
8    o o oo o   o   o o o        C    c     c
7    O   O  O   O   O   O        C
6    O   OOOO   O   O   O cCcCcCcC      iIiI
5    O   O  O   O   O   O        C
4  _ o _ o-_o - o - o - oOoOoOoOoCcCcCcCCCCC__
3  - O - O--O - O - O - O - O- O - C - C - C--
2  _   _  -_  -_  -_ _-  _-  _   _   _   _  -_
1  -   -  --  -   -   -   -  -   -   -   -  --
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | X | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS10 |   |   |   | X |
| NMOS11 |   |   |   | X |
| NMOS12 |   |   |   | X |
| NMOS13 |   |   |   | X |
| NMOS14 |   |   |   | X |
| NMOS15 |   | X |   |   |
| NMOS16 |   |   |   | X |
| NMOS17 |   | X |   |   |
| NMOS18 |   | X |   | X |
| NMOS19 |   | X |   |   |
| NMOS2 |   |   |   | X |
| NMOS20 |   | X |   |   |
| NMOS21 |   | X |   |   |
| NMOS22 |   | X |   |   |
| NMOS23 |   | X |   |   |
| NMOS24 |   | X |   |   |
| NMOS25 |   | X |   |   |
| NMOS26 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS5 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   |   |   | X |
| NMOS8 |   |   |   | X |
| NMOS9 |   |   |   | X |
| PMOS1 |   | X |   |   |
| PMOS10 |   | X |   |   |
| PMOS11 |   | X | X |   |
| PMOS12 |   | X |   |   |
| PMOS13 |   |   | X |   |
| PMOS14 |   | X |   |   |
| PMOS15 |   |   | X |   |
| PMOS16 |   | X |   |   |
| PMOS17 |   |   | X |   |
| PMOS18 |   | X |   |   |
| PMOS19 |   |   | X |   |
| PMOS2 |   | X |   |   |
| PMOS20 |   | X |   |   |
| PMOS21 |   | X |   |   |
| PMOS22 |   |   | X |   |
| PMOS23 |   |   | X |   |
| PMOS24 |   |   | X |   |
| PMOS25 |   |   | X |   |
| PMOS26 |   |   | X |   |
| PMOS27 |   |   | X |   |
| PMOS28 |   |   | X |   |
| PMOS29 |   |   | X |   |
| PMOS3 |   | X |   |   |
| PMOS30 |   |   | X |   |
| PMOS31 |   |   | X |   |
| PMOS32 |   |   | X |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   | X |   |   |
| PMOS7 |   | X |   |   |
| PMOS8 |   | X |   |   |
| PMOS9 |   |   | X |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 |   |
| NMOS3 |   |
| NMOS4 |   |
| NMOS5 |   |
| NMOS6 |   |
| NMOS7 |   |
| NMOS8 |   |
| NMOS9 |   |
| NMOS10 |   |
| NMOS11 |   |
| NMOS12 | O |
| NMOS13 |   |
| NMOS14 |   |
| NMOS15 |   |
| NMOS16 |   |
| NMOS17 |   |
| NMOS18 |   |
| NMOS19 |   |
| NMOS20 |   |
| NMOS21 |   |
| NMOS22 |   |
| NMOS23 |   |
| NMOS24 |   |
| NMOS25 |   |
| NMOS26 |   |
| PMOS1 |   |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
| PMOS5 |   |
| PMOS6 |   |
| PMOS7 |   |
| PMOS8 |   |
| PMOS9 | O |
| PMOS10 |   |
| PMOS11 |   |
| PMOS12 |   |
| PMOS13 |   |
| PMOS14 |   |
| PMOS15 |   |
| PMOS16 |   |
| PMOS17 |   |
| PMOS18 |   |
| PMOS19 |   |
| PMOS20 |   |
| PMOS21 |   |
| PMOS22 |   |
| PMOS23 |   |
| PMOS24 |   |
| PMOS25 |   |
| PMOS26 |   |
| PMOS27 |   |
| PMOS28 |   |
| PMOS29 |   |
| PMOS30 |   |
| PMOS31 |   |
| PMOS32 |   |
