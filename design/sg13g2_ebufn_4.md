# Design Documentation for sg13g2_ebufn_4

## Substrate
```
  012345678901234567890123456
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3
2
1  ppppp   ppppppppppppppppp
0  ppppp   ppppppppppppppppp
9  ppppp   ppppppppppppppppp
8  ppppp   ppppppppppppppppp
7
6
5
4  nnnnn   nnnnnnnnnnnnnnnnn
3  nnnnn   nnnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
4
3
2     G         G G G G G
1     G         G G G G G
0     G         G G G G G
9     G         G G G G G
8     G         G G G G G
7     GGGGGGGGGGGGG G G G
6   G GGG           GGGGGG
5   G G   G     G G G G G
4   G G   G     G G G G G
3   G G   G     G G G G G
2   G G   G     G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +       +   +
2  c &      c+c c+cCcCcCCCcC
1  C +     C + C + C   C   C
0  cCCCCCC CCCCCc+cCcIcCcIcC
9  C     C     C   C I   I C
8  CII c     C CcCCCcIIIiIc
7  CI  CCCC  C           I
6  CIc iI C         cCcC I
5  C   I  CCCCCCCCCC IIIII
4  c _ I  cCc-cCc-cCcI  cIcC
3  C - CCCCC - C - C   C   C
2  c _ c  c c-c c-cCcCcCCCcC
1    -       -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Internal1 | Internal2 | Internal3 | Internal5 | Internal6 | Internal7 | Internal8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   | X |   |   |   |   |   |
| NMOS3 |   | X |   | X | X |   |   |   |   |   |   |
| PMOS1 |   |   |   |   | X | X |   |   |   |   |   |
| PMOS2 | X |   |   | X |   |   |   | X | X |   |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 | X |   | X |   |   |   |   | X |   |   | X |
| Poly3 |   |   |   |   | X |   |   |   |   |   |   |
| Poly4 |   |   |   |   | X |   |   |   |   | X |   |
| Poly5 |   | X |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   | X | X |   | X | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 | O | O |   |   |   |   |
| NMOS3 |   |   | W | O | O | O |
| PMOS1 |   | O |   |   |   |   |
| PMOS2 |   | O |   |   |   | O |
| PMOS3 |   |   |   |   |   |   |
