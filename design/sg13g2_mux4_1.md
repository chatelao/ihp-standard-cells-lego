# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3     G        G         G       G
2     G        G         G       G
1     G        G         G       G
0     G        G         G       G
9     G        G         G       G
8     G        G         G       G
7     G        G         G       G
6    GGG      GGG       GG       GG
5     G        G         G       G
4     G        G         G       G
3     G        G         G       G
2     G        G         G       G
1     G        G         G       G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     +        & xCxCxCx+   CxCxCxC +
1  CC +        + C     C+ C C     C + O
0  xC +   CxCxCxCx xCx xCxC C C CxC + O
9  CC +   CC       CCCCC  C C C CCCCC O
8  xC +   Cx  I I      x  C C C C   C O
7  C I I  C   I I   CC CIIC C CCC I C O
6  C i iCCC C i i C C  CiIC C C C i C O
5  C    C C C     C CCCCCCC C CCCC   OO
4  CxCxCx x xCxCxCxCxC   CxCxCxCxC - OO
3  C  - C   C  -   CCC - C     CCC - OO
2     _ xCxCx  -       - CxCxCxC   -
1     -        -       -           -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456
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
