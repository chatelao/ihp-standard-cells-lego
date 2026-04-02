# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 SSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4 pppppppppppppppppppp
3
2
1    pppppppppppppppp
0  pppppppppppppppppp
9  pppppppppppppppppp
8  pppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789
4
3
2                  G
1   G              G
0   G              G
9   G              G
8   G              G
7   GGG            G
6   GGG G G G  G GGG
5   G              G
4   G              G
3   G              G
2                  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 &+&+&+&+&+&+&+&+&+&+
3     +        +    +
2     +CCCCCCCC+  c +
1     +C      C+ OO +
0  c c C  c   C+cOo &
9  C     CC   C+ OO +
8  c   CC     C+cOo &
7  CII        C
6  CIi  Ici i cCcC
5  C    I   I
4  c _  IIIII     o _
3    - CCCCCCC -  O -
2    _   c     -c c _
1    -         -    -
0 _-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Internal2 | Internal5 | Output1 | Output2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |
| NMOS2 |   |   | X |   |   | X |   | X |   |
| PMOS1 | X | X |   |   |   | X | X |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   |   |   |
| Poly5 |   |   |   | X |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 | O | O |   |   |   |   |
| PMOS1 | O | O |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |
