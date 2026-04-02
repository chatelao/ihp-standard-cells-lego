# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3     p     p
2     p     p
1     p   ppppppppppppppppp ppppp
0  pppppp pppppp     pppppp ppppp
9  pppppp pppppp     pppppp ppppp
8  pppppp            pppppp   ppp
7
6
5  nnnnn  nn
4  nnnnn  nnnnnnnnnn nnnnnn   nnn
3    nnn  nnnnnnnnnn nnnnnn nnnnn
2           nnnn     nnnnnn nnnnn
1           n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901
4
3
2            GG G            G G
1          G GG G            G G
0          G GG G            G G
9          G GG GG G         G G
8          G GG    G         G G
7    G G   GGGGGG            G G
6    G G GGGGG      GGGGGGGGGG G
5            GGG  G   GG G   G G
4            GG   G   GG G   G G
3            GG   G   GG G   G G
2            GG G     GG G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +      +++        +
2    c+     &      +&+  c c   &
1     +     +    C +++    IIC + I
0  cCCCCCCCCC  CcC    c c iIc & i
9  C        C  C C CCCC   IIC + I
8  C   c  c C CCc cCCCcCCC IC   i
7  C I I    CCCCCCCCC    C IC   I
6  C i i c  c c C   c  IcCcICCcCI
5  C      CCCCCCC      I   IC   I
4  c _-cC c    Cc c-cC  _ iIC _ i
3    --CCCCCCC     - C  - I C - I
2    _-c    _ CCcC -cC  _ i c _ i
1    --     -      -    -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Input3 | Input4 | Input5 | Internal1 | Internal3 | Internal4 | Internal5 | Internal7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |   | X |   |   |
| NMOS2 |   |   | X | X |   |   |   |   |   |   |   |   |   |
| NMOS3 |   |   | X |   | X |   |   |   |   | X |   |   |   |
| NMOS4 |   |   | X |   |   |   |   |   |   |   | X |   |   |
| PMOS1 | X | X |   | X |   |   |   |   |   |   | X |   | X |
| PMOS2 | X |   |   |   | X |   |   |   |   | X |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   | X | X |   |
| Poly2 |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | SE |   |   | O |   |   |   |   |
| NMOS2 |   |   | O |   |   |   |   |   |   |
| NMOS3 |   |   | O | O |   |   |   |   |   |
| NMOS4 |   |   |   |   |   | N | N |   |   |
| PMOS1 | O |   |   |   |   | S | S |   | O |
| PMOS2 |   |   | O | O |   |   |   |   |   |
