# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 ppppNNNppppppNNNNNNNNNpppppNNNNNNNNNNNpNNNNNpNNNpN
1 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNN
0 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNpNpNpN
9 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNN
8 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNpNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSSnSSS
3 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSSSSSS
2 nnnnSnSnnnnnSSSSSSSSSSnnnnnSSSSSSSSnSSSSSnSSSnSnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3
2 G G     G G            G G
1 G G     G G            G G
0 G G     G G            G G
9 G G     G G            G G
8 G G     G G            G G
7 G G     G G            G G
6 GGG     GGG            GGG
5 G G     G G            G G
4 G G     G G            G G
3 G G       G            G G
2 G G       G            G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +   +
2  + CCcCCCC +&CcCC cCcCCCCCCCcCcCcCcCcC&+    &   &
1  + C      C+ C  C                      + C  + O +
0  + CCcC C CCcCc c   cCCCCCCCcCc        + C  & o &
9  + CC   C     C C   C        CCC     C   C  + O +
8    CCcCCCCCCcCc c  Cc CCCCCCcCcCcCcCcCcCcC    o
7    CC C II C  C C  C  C II   CC  CC    C C    O
6  I cC  ciI CcCc cCcCcCc IIcCcCcCcC  c cC CcC  OOO
5    CCCCCCCCC CCCCC C  C II C  CCCCCCCCCC  C   O
4    C cC   C c c  Cc c CCCC CcCcCCC     C- c - o -
3  CCC-   - C CCCCCC         C      C-  CC- C - O -
2     -_  -_CCcCcCcCcCcCCCCCCCcCcCc c_  c -_  -_ _-
1     -   -                          -    -   -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | RESET_B | Q | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS10 |   | X |   |   |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   |   |   | X |
| NMOS8 |   |   |   | X |
| NMOS9 |   |   |   | X |
| PMOS10 |   |   | X |   |
| PMOS11 |   |   | X |   |
| PMOS2 |   |   | X |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   |   | X |   |
| PMOS6 |   | X |   |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   |   | X |   |
| PMOS9 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   |   |   |
| NMOS4 |   | O |   |
| NMOS5 |   |   | O |
| NMOS6 |   |   |   |
| NMOS7 |   |   |   |
| NMOS8 |   |   |   |
| NMOS9 |   |   |   |
| NMOS10 |   |   |   |
| PMOS1 | O |   |   |
| PMOS2 |   | O |   |
| PMOS3 |   |   | O |
| PMOS4 |   |   |   |
| PMOS5 |   |   |   |
| PMOS6 |   |   |   |
| PMOS7 |   |   |   |
| PMOS8 |   |   |   |
| PMOS9 |   |   |   |
| PMOS10 |   |   |   |
| PMOS11 |   |   |   |
