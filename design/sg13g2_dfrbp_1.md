# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 ppppNNNppppppNNNNNNNNNpppppNNNNNNNNNNNNNpNNNNNpNNNNN
1 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNNNN
0 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNpNpNNNNNpNNN
9 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNNNN
8 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNpNNNNNNNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSnSSSSnnSSS
3 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSSSSSSSS
2 nnnnSnSnnnnnSSSSSSSSSSnnnnnSSSSSSSSnSSSSSnSSSSSnSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
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
  0123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                            +      +
2  + CCcCCCC +&CcCc cCcCCCCCCCcCcCcCcCcC  &     &+
1  + C      C+C   C                       + O  C + O
0  + CCcC C CCc c c    CCCCCCCcCc         & o  C +oO
9  + CC   C     C C    C       CCCCC   C    O  C + O
8    CCcCCCCCCcCc c cCcCCCCCCCcCc cCcCcCcCc o  C + Oo
7  I CC C II C  C C  C  C      CC  CC     C O  C   O
6  I cC  ciI CcCc cCcCcCc IIcCcCcCcCCCcCc c O cCcCcO
5  I CCCCCCCCC CCCC CC  C    C  CCCC      C O  C   O
4  I C cC   C c c   cCcCCCCC CcCcCcC    cCc o  C _oO
3  CCC-   - C CCCCCCC        C      C-  CC- O  C - O
2     -_  -_CCcCcCcCcCcCCCCCCCcCcCc c_  c -_     _
1     -   -                          -    -      -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | RESET_B | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS10 |   | X |   |   | X |
| NMOS3 |   |   |   |   | X |
| NMOS4 |   |   |   |   | X |
| NMOS6 |   |   |   |   | X |
| NMOS7 |   |   |   |   | X |
| NMOS8 |   |   |   |   | X |
| NMOS9 |   |   | X |   |   |
| PMOS10 |   |   |   | X |   |
| PMOS11 |   |   |   | X |   |
| PMOS2 |   |   |   | X |   |
| PMOS4 |   |   | X |   |   |
| PMOS5 |   | X |   |   |   |
| PMOS6 |   |   |   | X |   |
| PMOS7 |   |   | X |   |   |
| PMOS8 |   | X |   |   |   |
| PMOS9 |   |   |   | X |   |
| Poly2 | X |   |   |   |   |

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
