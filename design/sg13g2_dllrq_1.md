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
4
3
2  pppppppppppppppppppppppppp
1  pppppppppppppppppppppppppp
0  pppppppppppppppppppppppppp
9  pppppppppppppppppppppppppp
8  pppppppppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567
4
3   G G G
2   G G G
1   G G G
0   G G G
9   G G G
8   G G G
7   G G G
6  GG GGG
5   G G G
4   G G G
3   G G G
2   G G G
1   G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +     +       +++   +
2     +     +       +++   +
1     +             +++ C + oO
0  CC + CCCCCCCCCCC +++ C + oO
9  CC + CC     CC C CCCCCCCCoO
8  CC + CCCCCCCCC C CCCC   CoO
7  C     C C  CCCCCCCC C   C O
6  i   i C CCCCC     CCC   C O
5  CC    C CCCCCCCC  C C     O
4  CC   CCCCCC   CCCCC C  - oO
3  CCCCCCCCCCC   C     C  - oO
2                    - C  - oO
1     -     ---      -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567
4
3
2
1
0
9
8
7
6
5
4
3
2
1
0
```
Legend: M=Metal 2
