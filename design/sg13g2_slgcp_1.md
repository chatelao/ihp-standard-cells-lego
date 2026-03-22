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
2 pppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
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
8 G GGGGG             G G
7 G G G G             G G
6 GGG G G             GGG     G
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
2 &+    &+        &         &
1  +   C +        + CCCCC C + O
0  +   cCccCcC C    c c c c & o
9       C    C C    CCC  CC + O
8    iIICccC  cCcCcCcCc cCcC  o
7  I    C CCCCCC    CC I C C  O
6  I  CcCcc c cCcCc cCcIcCcCcCo
5     C  CCCC C CCC CC     C  O
4  _ cCc c  c c c cCcCc_  cC- o
3  - CCCCCCCCCC C-C  C -  CC- O
2  _   _  c cCcCC_cCcC _    -_
1  -   -         -     -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | GATE | GCLK | SCE | Int1 | Int2 | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   | X |
| NMOS2 |   |   | X |   | X | X |   | X |
| PMOS1 |   | X | X |   | X | X | X |   |
| PMOS2 |   |   |   |   |   |   | X |   |
| Poly1 |   | X |   |   |   |   | X |   |
| Poly2 |   |   |   |   | X | X |   |   |
| Poly3 |   |   | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS | Polysilicon |
| PMOS | Polysilicon |
