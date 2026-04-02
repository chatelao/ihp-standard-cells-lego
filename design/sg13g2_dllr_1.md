# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNSSSNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNSSSNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNSSSNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3           pp
2           pp
1  pppppp ppppppppppppppppppp ppppp
0  pppppp ppppppp     ppppppp ppppp
9  pppppp ppppppp     ppppppp ppppp
8         p           ppppppp ppppp
7
6
5
4  nnnnnn nnnnnnnnnnnnnnnnnnn nnnnn
3  nnnnnn nnnnnnnn    nnnnnnn nnnnn
2                     nnnnnnn   nnn
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2      G       G G               G
1      G       G G     G G G   G G
0      G       G G     G G G   G G
9      G       G GG G  G G G   G G
8      G       G       G G G   G G
7    G G     G   G     G G G  GG G
6    G G   G   G GG  GGG G GGGGGGG
5          G   G GG            G G
4          G   G  G            G G
3          G   G  G            G G
2          G   G                 G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +      +        ++   +     +
2  c &      &  CCCC  ++   +     & c
1  C + CCCC       C  ++ C + I   + I
0  c   C c   C  c c c c c & i c & i
9  CCCCCC   CC    C CCCCC + I C + I
8  C c c  c CC C    c  CcCC iIC & i
7  C I I  C CC C CCCC        IC   I
6  C i i  CCc cCcCcCCCc cI CcICCcCI
5  C      C      CCC         IC   I
4  c c cC cCCCCCCCCCc c   _ i c _ i
3       C C -   CCCC  C   - I C - I
2    c c  c _   c     c   _ i   _ c
1           -             -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS3 | VSS4 | Input1 | Input2 | Input3 | Input4 | Input5 | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X |   | X |   |   |   |   |   | X | X |   |   |   |   |
| NMOS3 |   | X |   |   |   | X |   |   |   |   |   |   | X |   |   |   |
| NMOS4 |   |   |   | X |   |   |   |   |   | X |   |   |   | X |   |   |
| PMOS1 | X |   |   |   |   |   | X |   |   |   | X |   |   |   |   | X |
| PMOS2 | X |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O |   | O |   |   |   |   |   |   |   |   |
| NMOS3 |   |   | O |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 |   |   | O |   |   |   | O | O |   | O | O |   |
| PMOS2 |   |   | O |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   | O |   |   |   |   |   |   |
