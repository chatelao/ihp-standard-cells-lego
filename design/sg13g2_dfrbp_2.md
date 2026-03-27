# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3
2 G G    G G             G G
1 G G    G G             G G
0 G G    G G             G G
9 G G    G G             G G
8 G G    G G             G G
7 G G    G G             G G
6 GGG    GGG             GGG              G G       G
5 G G    G G             G G
4 G G    G G             G G
3 G G    G G             G G
2 G G    G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++++++++++++++++++++++++++++
2  &        &+                          &+  &+  &+  &+
1  + CCCC CC + CCCC C                 C ++  ++  ++  ++
0  & cCcC cCc cCc c   cCcCcCcCcCc       &+  &+  &+  &+
9  + CC   C     C C CCCCCCCCCCCCCC    C ++  ++  ++  ++
8  & cCcCc  cCcCc c cCcCc   cCcCcCc cCcC  o &+  &+  &+
7   I C C II C  C C  C C III  CCC C C     OO   C   O
6  iI C   iI CcCc cCcCcC IiI CcCcCc c cCc oOoO CcC Oo
5  II CCCC  CCCCCCCC C   III  CCCCCCCCCCCC  OO  C   OOO
4    c  Cc  c   c  CcC  c   c cCcCc      C  oO  c _ o
3  CC - C -- CCCCCCC    CCCCC CCCCCC -- C --  - C -  --
2     -   _-                         -_   _-  _   _  -_
1 -----------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | RESET_B | CLK | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   | X | X | X |
| PMOS1 | X |   |   |   | X |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |
| Poly2 |   |   |   | X | X |   |   |
| Poly3 |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   |   | X |
| Poly5 |   |   |   |   |   |   | X |
| Poly6 |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 | O | O | O |   |   |   |
| PMOS1 | O | O | O |   |   |   |
| PMOS2 |   |   |   |   |   |   |
