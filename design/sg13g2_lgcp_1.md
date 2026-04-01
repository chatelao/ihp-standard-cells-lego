# Design Documentation for sg13g2_lgcp_1

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
7 NNNNNNNNNNSSSSSNNNNNNNNNNNN
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
3            pp
2            pp
1  pppppppppppppp ppppppppp
0  ppppppp    ppp ppppppppp
9  ppppppp    ppp ppppppppp
8  ppp                  ppp
7
6
5             nnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnn       nnnnnnnnnnn
2    n
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
4
3
2   G  G   G             G
1   G  G   G             G
0   G  G   G             G
9   G  G   G G           G
8   G  G     G           G
7   G  G   G GGG   GG    G
6   GG G G G G        G GG
5   G  G   G G
4   G  G   G
3   G  G   G
2   G  G     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +        +    +    +
2  c &        &    +    & c
1  C +  CCC       C+ C  + I
0  c    C c   CCCCc cCc & i
9  C CCCCCCCCC  C C  C  + I
8  c C I Cc     c CI    c i
7  C C I C C  CCC  II     I
6  C c c c Cc c c c c  Cc I
5  C CCCC       C  -  CC  I
4  cCCC CCc  -_ c  -c cCc-i
3  C          -    -     -I
2  c _ CCCCCcC-    -    c-c
1    -        -    -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Internal2 | Internal3 | Internal4 | Internal6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |
| NMOS2 |   |   | X | X |   | X | X | X |   |
| PMOS1 | X |   |   |   |   | X |   |   |   |
| PMOS2 | X | X |   | X |   |   | X |   | X |
| Poly1 |   |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   | X |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   | X |   |
| Poly9 |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O |   | O | NW |   | N |   |   |   |
| PMOS1 | O | O |   |   | W |   |   |   |   | O |
| PMOS2 |   |   |   |   |   |   |   | O |   |   |
