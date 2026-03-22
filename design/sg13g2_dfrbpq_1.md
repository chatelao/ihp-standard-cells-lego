# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 ppppNNNppppppNNNNNNNNNpppppNNNNNNNNNNNNNpNNNpNNN
1 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNN
0 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNpNpN
9 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNN
8 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNpNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSSnS
3 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSSSS
2 nnnnSnSnnnnnSSSSSSSSSSnnnnnSSSSSSSSnSSSSSSSnSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
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
  012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +
2  + CCcCCCC +&CcCc cCcCCCCCCCcCcCcCcCcC +&   &
1  + C      C+C   C                      +  C + O
0  + CCcC C CCc c c    CCCCCCCcCc        +  c & o
9  + CC   C     C C    C       CCCCC   C +  C + O
8    CCcCCCCCCcCc c cCcCCCCCCCcCc cC  cCc   c & o
7  I CC C II C  C C  C  C      CC  CCCCCCCC C   O
6  I cC  ciI CcCc cCcCcCc IIcCcCcCcCcCcCc c cCcCO
5  I CCCCCCCCC CCCC CC  C    C  CCCC      C C   O
4  I C cC   C c c   cCcCCCCC CcCcCcC    cCC c -Oo
3  CCC-   - C CCCCCCC        C      C-  CC  C -OO
2     -_  -_CCcCcCcCcCcCCCCCCCcCcCc c_  c    _-
1     -   -                          -        -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | RESET_B | Q | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   |   |   | X |
| NMOS8 |   | X |   |   |
| PMOS10 |   |   | X |   |
| PMOS2 |   |   | X |   |
| PMOS4 |   |   | X |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   | X |   |   |
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
