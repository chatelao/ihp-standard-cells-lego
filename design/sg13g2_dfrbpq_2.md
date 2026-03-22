# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3
2 G G     G G            G G
1 G G     G G            G G
0 G G     G G            G G
9 G G     G G            G G
8 G G     G G            G G
7 G G     G G            G G
6 GGG     GGG            GGG                    G G
5 G G     G G            G G
4 G G     G G            G G
3 G G     G G            G G
2 G G     G G            G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +   +
2 &+ cCcCccC&+ CcCC cCcCcCcCcCcCcCcCcCcC&+    &   &
1  + C      C+ C  C                      + C  + O +
0  + cCcC c cCcCc c   cCcCcCcCcCc        + C  & o &
9  + CC   C     C C   C        CCC     C   C  + O +
8    cCcCccCcCcCc c  Cc cCcCcCcCcCcCcCcCcCcC    o
7    CC C II C  C C  C  C II   CC  CC    C C    O
6  I cC   iIcCcCc cCcCcCc II CcCcCcC  c cC CcC  oOo
5    CCCCCCCCC CCCCC C  C II C  CCCCCCCCCC  C   O
4    c  Cc  c   c  Cc   cCcCcCcCcCCC     C- c - o -
3  CCC-   - C CCCCCC         C      C-  CC- C - O -
2  c  -_  -_cCcCcCcCcCcCcCcCcCcCcCc c_  c -_  -_ _-
1     -   -                          -    -   -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | D | Q | RESET_B | Int1 | Int2 | Int3 | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   | X |
| NMOS2 |   |   | X |   | X |   | X |   | X |
| PMOS1 |   |   | X |   | X | X |   | X |   |
| PMOS2 |   |   |   |   |   |   |   | X |   |
| Poly1 |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   | X | X |   |   | X |   |
| Poly3 |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS | Polysilicon |
| PMOS | Polysilicon |
