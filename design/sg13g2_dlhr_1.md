# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3   G G G             G G
2   G G G             G G
1   G G G             G G
0   G G G             G G
9   G G G             G G
8   G G G             G G
7   G G G             G G
6   GGGGG             GGG
5   G G G             G G
4   G G G             G G
3   G G G             G G
2   G G G             G G
1   G G G             G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     &     +      +++   +    +
2     +     & cccc +&+   +    &
1     +     & c  c +&+ c +ooc & o
0  cccccccccc cccc     c +ooc & o
9  c        c c cc ccccc  ooc & o
8  c    ccccc c c  ccccccc oc   o
7  C I I C CCCC CCCCC c  C OC   O
6  C i i C CCCC C   C ci C OCCCCO
5  C     CCCCCCCC     cI   OC   O
4  c --ccccc   cc  - cc - ooc _ o
3    --cccccccc    - cc - o c _ o
2    --       cccc - cc - o c _ o
1    -_     -      -    _     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

