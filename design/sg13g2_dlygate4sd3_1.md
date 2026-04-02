# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  0123456789012345
4 SSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3
2
1  pppppp ppppppp
0  pppppp ppppppp
9    pppp ppppppp
8         ppppppp
7
6
5
4         nnnnnnn
3  nnnnnn     nnn
2
1
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3
2     GG   GG
1   G GG   GG
0   G GG   GG
9   G GG   GG
8   G GG   GG
7   G GG   GG
6   G GG   GG G
5   G GG   GG
4   G GG   GG
3   G GG   GG
2   G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3    +        +
2    +   c    & c
1    +  C C   + O
0  c &  Ccc   & o
9  CCCC C C     O
8     C CccCCC  o
7  II C C       O
6  IIcCcCCcCc c O
5     C C       O
4  CCCC C cCCC Oo
3  C -  C     -OO
2  c _   c    _ c
1    -        -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Internal2 | Internal3 | Output1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |
| NMOS3 |   |   |   | X |   | X |
| PMOS1 | X |   | X |   |   | X |
| PMOS2 | X |   | X |   |   |   |
| PMOS3 | X |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |
| Poly2 |   |   | X |   |   |   |
| Poly3 |   |   | X |   |   |   |
| Poly4 |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O |   |   |
| NMOS3 |   |   | O |   |
| PMOS1 |   |   | O |   |
| PMOS2 | O | O |   |   |
| PMOS3 |   |   |   |   |
