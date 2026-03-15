# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppN
1 NpppppppppppppppppppN
0 NpppppppppppppppppppN
9 NpppppppppppppppppppN
8 NpppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890
4
3  G G   G G G GG G
2  G G   G G G GG G
1  G G   G G G GG G
0  G G   G G G GG G
9  G G   G G G GG G
8  G G   G G G GG G
7  G G   G G G GG G
6  GGG   GGG GGGGGG
5  G G   G G G GG G
4  G G   G G G GG G
3  G G   G G G GG G
2  G G   G G G GG G
1  G G   G G G GG G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3  +   +
2  &   & xCxCxCxC CxCxC
1  + C + C  C   C C   C
0  & x & xC C C C C O C
9  + CCCCCC C CCCCC O C
8                   O C
7                   O
6   iI    iI  iI iI OO
5    OOOOOOOOOOOOOOOO
4  - O    o   o     o -
3  - O ---O - O --- O -
2  -   -_-  _   _-_   -
1  -   ---  -   ---   -
0 -_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  012345678901234567890
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
