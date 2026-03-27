# Design Documentation for sg13g2_ebufn_8

## Substrate
```
  01234567890123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2                                    G G G G
1                                    G G G G
0                                    G G G G
9                                    G G G G
8                                    G G G G
7                                    G G G G
6    G                               GGGGGGG
5                                    G G G G
4                                    G G G G
3                                    G G G G
2                                    G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3                  ++  ++  +   +         +  ++
2 CcCcCcCccCcCcCcCc+&  +&  +&  +  c     &+  &+
1 CC  CC  C   C   C++CC++C + CCCCC       + C++
0 CcOoCcO c o c o cCcCcCcCcCcCc c cCcCcCcCcC&+
9 CCOO  O   O   O CCCCCCCCCCCCCCCCC        CCC
8 CcOoOoOooOoOoOo c       c         cCcC    cC
7    O  CCCCCCCCCCC                 C        C
6    o  CccCcCcCc  CcCcCcCcCcCcCcC  c iIi iIcC
5 CCOOOOOOOOOOOOO CCCCC  CC  C   C  C        C
4 CcOo  Ooo o   o c _ c-_Cc-_C - Cc c cC -cCcC
3 CC  CC  C   C   C - C--CC--C - C CCCCC - C--
2 CcCcCcCccCcCcCcCc _  -_  -_  -_   c   _-  _-
1                   -  --  --  -         -  --
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | VSS4 | VSS5 | A | TE_B | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X | X | X | X |   |   |   | X |
| PMOS1 | X |   |   | X | X | X |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   | X | X |   |
| Poly2 |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
