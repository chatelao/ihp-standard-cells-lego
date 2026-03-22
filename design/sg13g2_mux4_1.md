# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 ppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppNNpppppppNNNpppppNNNNNpppppNN
1 NpppppppNNpppppppNNNpppppNNNNNpppppNN
0 NpppppppNNpppppppNNNpppppNNNNNpppppNp
9 NpppppppNNpppppppNNNpppppNNNNNpppppNN
8 NpppppppNNpppppppNNNpppppNNNNNpppppNp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnSSnnnnnnnSSSnnnnnSSSSSnnnnnSn
3 SnnnnnnnSSnnnnnnnSSSnnnnnSSSSSnnnnnSS
2 SnnnnnnnSSnnnnnnnSSSnnnnnSSSSSnnnnnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3
2   G   G    G   G     G G       G G
1   G   G    G   G     G G       G G
0   G   G    G G G     G G       G G
9   G   G    G G G     G G       G G
8   G   G    G G G     G G       G G
7   G G G    G G G     G G       G G
6   GGGGG    GGGGG     GGG       GGG
5   G G G    G G G     G G       G G
4   G G G    G G G     G G       G
3   G   G    G   G       G       G
2   G   G    G   G       G       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     +        +&CCCcCCC&   cCcCCCC &
1  CC +        + C     C+ C C     C + O
0  CC +   cCCCCCCC CcC CCCC c c CCC & o
9  CC +   CC       CCCCC  C C C CCCCC O
8  CC +   cC  I I   c  C  C c c C   C o
7  C I I  C   I I   CC CIIC C CCC I C O
6  c I ICcc c I I c c cCIIc c C c I c O
5  C    C C C     C CCCCCCC C CCCC   OO
4  CCCCCC c CCCCCCCCcC   CCCcCcCCC - Oo
3  C  - C   C  -   CCC - C     CCC - OO
2    _- CCcCC  -    c  - CCCcCcC   -
1     -        -       -           -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | X | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS6 | X |   |   |
| PMOS2 |   | X |   |
| PMOS3 |   | X |   |
| PMOS4 |   | X |   |
| PMOS5 | X |   |   |
| PMOS6 | X |   |   |
| PMOS7 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O |   |   |   |
| NMOS3 |   | O |   |   |
| NMOS4 |   |   | O |   |
| NMOS5 |   |   |   | O |
| NMOS6 |   |   |   |   |
| PMOS1 | O |   |   |   |
| PMOS2 |   | O |   |   |
| PMOS3 |   |   | O |   |
| PMOS4 |   |   |   | O |
| PMOS5 |   |   |   |   |
| PMOS6 |   |   |   |   |
| PMOS7 |   |   |   |   |
