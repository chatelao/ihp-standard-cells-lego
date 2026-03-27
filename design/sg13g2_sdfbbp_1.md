# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2 G G G GGGG   G G G         G G
1 G G G GGGG   G G G         G G
0 G G G GGGG   G GGG         GGGG       G
9 G G G GGGG   G G G         G G
8 G G GGGGGG   G G G         GGG  G       G G
7 G G G GGGG   G G G         G G
6 GGG GGGGGG   GGG G         GGG            G       G   G     G
5 G G G GGGG   G G G         G G
4 G G G GGGG   G G G         G G
3 G G G GGGG   G G G         G G
2 G G G GGGG   G G G         G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2    &      &+    &+       +&     &+      &+&    +&   &     &
1  C + C   C + CC ++ CCC   ++ I   ++     I    C  ++   + OO  + OO
0  cC Cc c    cCc &+ CcCcC +& i i &+  c iI CcCcCc  CcC  oO  & oO
9        CCC CCCCC  CCCCCC ++ I  I  I CC I C  CCCCCCCCC OO  + OO
8   I Ii  cCcC C  cCcCcCc c   i c i   c  Ii iI Cc  Cc c oO    oO
7   I I Ii C C  II CCCCCC C C      CC C  IIIII  C CC  C OO C  OO
6  iI   Ii C Cc iI CcCcCc cCc i c cCc c c   i cCc c iI  oO C  oO
5   I  C   CCC  II CCCCCC CCCC CC CC  C CCCC CCCC CC I  OO    OO
4  _   c  _ cCcC    c c c cC CcCcCcC -  cCc _ cCcCcCc _ oO  _ oO
3  -   C  - C  CCC CCCC CCC - CCCCCC -   CC - CCCCC   - OO  - OO
2  _      _       _         _       _-      _         _     _
1 --------------------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | RESET_B | SCD | SCE | SET_B | CLK | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   |   |   | X | X | X |
| PMOS1 | X |   |   |   |   | X | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   | X |   |   |   |
| Poly11 |   |   |   |   |   |   | X |   |   |   |
| Poly12 |   |   |   |   |   |   | X |   |   |   |
| Poly2 |   | X | X |   |   | X |   | X |   |   |
| Poly3 | X |   |   |   |   |   |   | X |   |   |
| Poly4 |   |   |   | X |   |   | X |   |   |   |
| Poly5 |   |   |   |   |   |   | X |   |   |   |
| Poly6 |   |   |   | X |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   | X |
| Poly8 |   |   |   |   |   |   |   |   | X |   |
| Poly9 |   |   |   |   |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O |   |   |   |   | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |
