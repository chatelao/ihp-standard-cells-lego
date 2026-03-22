# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2   G G G             G G
1   G G G             G G
0   G G G             G G
9   G G G             G G
8   G G G             G G
7   G G G             G G
6   GGGGG             GGG       G
5   G G G             G G
4   G G G             G G
3   G G G             G G
2   G G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +      +++   +    +
2     &     & CCcC +&+  &+    &
1     +     + C  C +++ C +OOC + O
0  cCcCcCccCc cCcC    cC +oOc & o
9  C        C C CC CCCCC  OOC + O
8  c   cCCcCc c c  CcCcCcCoOc   o
7  C I I C CCCC CCCCC C  C OC   O
6  c I I ccCcCc c c c cI CcOcCcCo
5  C     CCCCCCCC     CI   OC   O
4  c _-cCCcCc  Cc  _ Cc - oOc - o
3    --CCCCCCCC    - CC - O C - O
2    _-   c   cCcC _ CC_- o c_- o
1    --     -      -    -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | GATE | Q | Q_N | RESET_B | Int1 | Int2 | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   | X |
| NMOS2 |   |   | X | X |   | X | X |   | X |
| PMOS1 |   |   |   |   |   |   |   | X |   |
| PMOS2 |   |   | X | X |   | X | X | X |   |
| Poly1 |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   |   |   | X |   | X |   |
| Poly3 |   |   |   | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS | Polysilicon |
| PMOS | Polysilicon |
