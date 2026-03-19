# Design Documentation for sg13g2_decap_8

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012
4 ppppppppppppp
3 NNNNNNNNNNNNN
2 NpppppppppppN
1 NpppppppppppN
0 NpppppppppppN
9 NpppppppppppN
8 NpppppppppppN
7 SSSSSSSSSSSSS
6 SSSSSSSSSSSSS
5 SSSSSSSSSSSSS
4 SnnnnnnnnnnnS
3 SnnnnnnnnnnnS
2 SnnnnnnnnnnnS
1 SSSSSSSSSSSSS
0 nnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012
4
3
2  GGGGG GGGGG
1  GGGGG GGGGG
0  GGGGG GGGGG
9  GGGGG GGGGG
8  GGGGG GGGGG
7  G         G
6  G   GGG   G
5      G G
4  GGGGG GGGGG
3  GGGGG GGGGG
2  GGGGG GGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012
4 &+&+&+&+&+&+&
3  +   +++   +
2  +   +++   +
1  &   +&+   &
0  +   +++   +
9  &   +&+   &
8  +   +++   +
7  &   +&+   &
6   _  +++  _
5   -       -
4   -       -
3  _-   _   -_
2  --   -   --
1  --   -   --
0 _-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)
