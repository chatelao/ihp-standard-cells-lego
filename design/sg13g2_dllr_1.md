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
2  GG G GGGG  G G G G   G     G
1  GG G GGGGG G G G G   G     G
0  GG G GGGGG G G G G G G     G
9  GG G GGGGG G G G G G G     G
8  GG G GGGGG G G G G G G G   G
7  GG G GGGGG G G G G G G G   G G
6  GGGGGGGGGG G G G G G G G   G G
5  GG G GGGGG G G G G G G G   G G
4  GG   GGGGG G G G   G G     G
3  GG   GGGG  G G G   G G     G
2  GG   GGGG  G G G   G G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +      +        ++   +     +
2    &   c  & cCcCc  +&   &     &
1  C + CCCCCCCC C C  ++ C + O C + O
0  c   cCc   Cc c c     c & o c & o
9  CCCCCCCCCCCC C C CCCCC + O C + O
8  c c  C c cCcCc c    CcCc oOc & o
7  C I IC C CCCCCCCCC  C  C  OC   O
6  c i iC iCc cCcCcCcCcCiIcCoOcCcCo
5  C    C CCCCCCCCCC   C     OC   O
4  c  -cC cCcCcCcCcC_ cC  _Oo c _ o
3     - C C -   CCCC- CC  -OO C - O
2     -     _     c _ cC  _Oo   _ o
1     -     -       -     -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | GATE_N | Input1 | RESET_B | D | Internal1 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   | X | X | X | X |
| PMOS1 | X |   |   |   |   | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X | X |   | X |   |   |   |
| Poly10 |   |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   |   | X |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   | X |   |   |   |
| Poly5 |   |   |   |   |   | X |   |   |   |
| Poly6 |   |   |   |   | X | X |   |   |   |
| Poly7 |   |   |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   |   | X |   |   |   |
| Poly9 |   |   |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | N | N | N |
| PMOS1 | O | O | O | O | O | O | O | O | O | S |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |
