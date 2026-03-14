# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4
3
2  pppppppppppppppppppppppppppp
1  pppppppppppppppppppppppppppp
0  pppppppppppppppppppppppppppp
9  pppppppppppppppppppppppppppp
8  pppppppppppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789
4
3   G G
2   G G
1   G G
0   G G
9   G G
8   G G
7   G G
6  GG GG
5   G G
4   G G
3   G G
2   G G
1   G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +           +      +
2  +     + CC CCC    +      +
1  + CCCCCCC  C CCCCCCCCCCC + o
0  + CCC  CCCCC C       CCC + o
9  + CCC  C  CC CCCCCCCCCCC + o
8     C     CC CCC CC  CCC    o
7     C     CCC  C  C  CCC    O
6  i  CiCCCCC   CC  C  CCC  CCO
5     C C  CCCCCCCC C  C C  C O
4    CC C- CCCCCC C C  C    C o
3  - CCCC-          CCCCCCCCC o
2  -     - CCCCCCCCCC
1  -     -            -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789
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
