# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate, N=N-Well

## Polysilicon
```
  012345678901234567890123456789012345678
4
3   G                       G
2   G                       G
1   G                       G
0   G                       G
9   G                       G
8   G                       G
7   G                       G
6  GG                       GG
5   G                       G
4   G                       G
3   G                       G
2   G                       G
1   G                       G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +     +   +   +  +
2  &     &   &   &  +  xCxCxCxCxCxCxCxC
1  + C C + C + C + C+  C   C   C   C  C
0  & x x & x & x & x+  x o x o x o x oC
9  + C C + C + C + CCCCC O   O   O   OC
8  & x xCxCxCxCxCxCx     oOoOoOoOoOoOo
7    C                   OOO
6  i C  CCCCCCCCCCCCCCCC OOO xIIIIIIII
5    CCCC   C   C   C  C OOOOOOOOOOOOO
4  - CxCx _ x _ x _ x- C O   O   O   Ox
3  - CCCC - C - C - C- CCCCCCCCC   C  C
2  -      _   _   _  -         CxCxCxCx
1  -      -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678
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
