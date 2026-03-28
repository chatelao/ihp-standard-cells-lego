# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2  GG   GGGG  G G G       G G
1  GG   GGGG  G G G       G G
0  GG G GGGGG G G G G     G G
9  GG G GGGGG G G G G   G G G
8  GG G GGGGG G G G G   G G G G
7  GG G GGGGG G G G G   G G G G
6  GGGGGGGGGG G G G G   G G G G
5  GG G GGGGG G G G G   G G G G
4  GG   GGGGG G G G G     G G
3  GG   GGGGG G G G G     G G
2  GG   GGGG  G G G G     G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +      +++  +     +
2     +     & cCcC +&+  &     &
1     +     +C   C +++ C+ OOC + O
0  cCcCcCccCcCcC C    cC& oOc & o
9  C      C CC C C CCCCC  OOC + O
8  c   cC c cCcCcC CcCcCcCoOc   o
7  C I ICCC CCCCCCCCCC I CCOC   O
6  c i iCci cCc c c cC IiCcOcCcCo
5  C    C CCCCCCC    C I   OC   O
4  c _-cC c c  Cc  - Cc _ oOc _ o
3    --CCCCCCC     - C  - O C - O
2    _-   c _CcCcC - C  _ o c _ o
1    --     -      -    -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | GATE | RESET_B | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   |   | X | X |
| PMOS1 | X |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X | X | X |   | X |
| Poly2 |   |   |   |   |   |   | X |
| Poly3 |   |   |   |   |   |   | X |
| Poly4 |   |   |   |   |   |   | X |
| Poly5 |   |   |   |   |   |   | X |
| Poly6 |   |   |   |   |   | X | X |
| Poly7 |   |   |   |   |   |   | X |
| Poly8 |   |   |   |   | X |   | X |
| Poly9 |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | N | N |
| PMOS1 | O | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |
