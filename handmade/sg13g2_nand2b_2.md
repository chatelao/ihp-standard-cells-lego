# Design Documentation for sg13g2_nand2b_2

## Substrate
GOLDEN STANDARD

```
  012345678901234
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
GOLDEN STANDARD

```
  012345678901234
4 ppppppppppppppp
3 NNNNNNNNNNNNNNN
2 NpppppppppppppN
1 NpppppppppppppN
0 NpppppppppppppN
9 NpppppppppppppN
8 NpppppppppppppN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
GOLDEN STANDARD

```
  012345678901234
4
3     G G  G G
2 G   G G  G G
1 G   G G  G G
0 G   G G  G G
9 G   G G  G G
8 G   G G  G G
7 G   G G  G G
6 G  GGGG  GGG
5 G   G G  G G
4 G   G G  G G
3 G   G G  G G
2 G   G G  G G
1     G G  G G
0
```
Legend: G=Polysilicon

## Metal 1
GOLDEN STANDARD

```
  012345678901234
4 &+&+&+&+&+&+&+&
3 +   +    +   +
2 +   & o  & o &
1 &   + O  + O +
0 + c & o  & o &
9 & C + OOOOOO +
8   c &      o &
7   C        O
6  iCc     IiO
5    C       O
4  _ c cCcCc o c
3  -   C   C   C
2  -   c _ cCCCc
1  -     -
0  _ _ _ _ _ _ _
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)
