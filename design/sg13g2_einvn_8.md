# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4 ppppppppppppppppppppppppppppppppppppppp
3
2
1  ppp ppppppppppppppppppppppppppppppppp
0  ppp ppppppppppppppppppppppppppppppppp
9  ppp ppppppppppppppppppppppppppppppppp
8  ppp ppppppppppppppppppppppppppppppppp
7
6
5       nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnn  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnn  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678
4
3
2   G   G G G G           G G G G
1   G   G G G G           G G G G
0   G   G G G G           G G G G
9   G   G G G G           G G G G
8   G   G G G G           G G G G
7  GGGGGGGGGGGGGGGGGGG    G G G G
6  GG                    GGGGGGGGGGGGGG
5      G G G G G          G G G G
4      G G G G G          G G G G
3      G G G G G          G G G G
2      G G G G G          G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&++
3  +     +   +   +  +
2  & c c &c c+c c+c &  CcCCCcCcCCCcCCCc
1  + C C + C + C + C+  C   C   C   C  C
0  & c c &cCc+cCc+cC&  CcIcCcIcCcIcCcIc
9  + C C + C + C + C   C I   I   I   IC
8  & c c ccCc cCc c     cIiIiIIIiIIIiIc
7    C CCCCCCCCCCCC      III
6  i C cCCCCCCCCCCCCCCCC III IiIiIiIiIc
5    CCCC   C   C   C  C III
4  _ cCcCc_ c _ c _ c-cCcIc cI  cI  cIc
3  - CCCC - C - C - C- C   C   C   C  C
2  _ c c c_ c _ c _ c-c c   c cCCCcCCCc
1  -      -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | Input1 | Input2 | Input3 | Input4 | Input5 | Input6 | Internal1 | Internal10 | Internal12 | Internal2 | Internal4 | Internal5 | Internal6 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   | X |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   |   |   | X | X | X | X | X |   |   | X |   |   | X |   |   |   |   |   |
| PMOS1 | X |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS2 | X | X | X |   | X |   |   |   |   |   |   |   |   | X | X | X | X |   |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   | X | X | X |   |   | X | X |   | X |   |   | X |   |   |   |
| Poly7 | X |   | X |   |   |   |   |   | X |   |   |   |   | X |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |
| NMOS3 | W | O | O | O | O | O |   |
| PMOS1 |   |   |   |   |   |   | O |
| PMOS2 |   |   |   |   |   | O | O |
| PMOS3 |   |   |   |   |   |   |   |
