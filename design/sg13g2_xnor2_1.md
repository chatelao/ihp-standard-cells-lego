# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 NNNNNNNNNNNNNN
2 NppppppppppppN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SnnnnnnnnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2     G G G
1     G G G
0     G G G
9     G G G
8     GGGGG
7     G G G
6     GGGGG   G
5     G G G
4     G G G
3     G G G
2     G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +    +     +
2  +&   &     &
1  +  C +   O +
0  + cC &   o &
9  + CC     O
8    c iIiiIoOoO
7    C III I   O
6    c IIIiIcCoO
5  - CCCCCCCCC O
4  _ cCcCccCc oO
3  -    CC  C OO
2  _      -
1  -      -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Internal3 | Internal1 | VDD | Internal2 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   | X | X |   | X |
| PMOS1 | X | X | X | X |   |
| PMOS2 |   |   |   | X |   |
| Poly1 | X | X |   | X |   |
| Poly2 |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS2 | Poly1 |
| PMOS1 | Poly1 |
