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
2 NppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2   G G G               G G
1   G G G               G G
0   G G G               G G
9   G G G               G G
8   G G G               G G
7   G G G               G G
6   GGGGG               GGG G     G
5   G G G               G G
4   G G G               G G
3   G G G               G G
2   G G G               G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +      +        ++   +     +
2    +&  c  &  CcCc  +&   &     &
1  C + CCCCCCC C  C  ++ C + O   + O
0  c   cCccCcCcCc c     c & o c & o
9  CCCCCCC  CC CC C CCCCC   O C + O
8  c c   Cc cCcCc c   cCcCcCoOc & o
7  C I I CC CC CCCCCC  C   C OC   O
6  c I I ccCcCcCcCcCcCcC IcCoOcCcCo
5  C     CC      CCC   C     OC   O
4  c _-cCCcCcCcCcCcCc-cC  - o c - o
3     - CCC -   CCCC -CC  - O C - O
2    _-     -_    c  _   _- o  _- o
1     -     -        -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | GATE_N | Q1 | Q2 | Q_N | RESET_B | Int1 | Int2 | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   | X |
| NMOS2 |   |   | X |   | X |   | X | X |   | X |
| PMOS1 |   |   |   |   |   |   |   |   | X |   |
| PMOS2 |   |   |   | X | X |   | X | X | X |   |
| Poly1 |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   |   |   |   | X |   | X |   |
| Poly3 |   |   |   | X |   |   |   |   |   |   |
| Poly4 |   |   |   |   | X |   |   |   |   |   |
