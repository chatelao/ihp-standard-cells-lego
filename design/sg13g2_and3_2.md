# Design Documentation for sg13g2_and3_2

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
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NppppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 Snnnnnnnnnnn
3 SnnnnnnnnnnS
2 Snnnnnnnnnnn
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2     GGGG
1     GGGG
0     GGGG
9     GGGG
8     GGGG
7     GGGG
6     GGGG  G
5     GGGG
4     GGGG
3     GGGG
2  G GGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +   +   +
2    +&  +& &+
1   C+ C + O +
0  cC+ c +oOo
9   C  C    O
8  cCcCcCcc o
7   C IIIIC O
6  cC IIIi  o
5   C      OO
4      I _ Oo_
3      I - O -
2  iIiIi _   _
1        -   -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Input | Internal | Output | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS | X |   | X |   | X |
| PMOS |   | X | X | X |   |
| Polysilicon | X | X | X | X | X |
