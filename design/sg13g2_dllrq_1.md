# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567
4
3   G G G               G G
2   G G G               G G
1   G G G               G G
0   G G G               G G
9   G G G               G G
8   G G G               G G
7   G G G               G G
6   GGGGG               GGG
5   G G G               G G
4   G G G               G G
3   G G G               G G
2   G G G               G G
1   G G G               G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +       +++   +
2     &     &       &+&   &
1     +             +++ C + OO
0  Cc & cCcCcCcCcCc &+& c & oO
9  CC + CC     CC C CCCCCCCCOO
8  Cc & cCcCcCcCc c cCcC   CoO
7  C I I C C  CCCCCCCC C I C O
6  C i i C CCCCC     CCC i C O
5  CC    C CCCCCCCC  C C I   O
4  cC   CcCcCc   cCcCc c  - OO
3  CCCCCCCCCCC   C     C  - OO
2                    _ c  - OO
1     -     ---      -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

