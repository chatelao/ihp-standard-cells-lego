# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4
3  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4   G G G       G               G            G       G
3   G G G       G               G            G       G
2   G G G       G               G            G       G
1   G G G       G               G            G       G
0   G G G       G               G            G       G
9   G G G       G               G            G       G
8   G G G       G               G            G       G
7   G G G       G               G            G       G
6   G G G       G               G            G       G
5   G G G       G               G            G       G
4   G G G       G               G            G       G
3   G G G       G               G            G       G
2   G G G       G               G            G       G
1   G G G       G               G            G       G
0   G G G       G               G            G       G
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 ++++++++++++++++++++++++++++++x+++++++++++++++++++++++++++++++
3    x       x    ++        +      +      +x+    x    x     +
2    + CCCCC +    x+        x IIxI xIIxIII+++    +    +     x
1  C + C   C + C C++C       + I  x +x    x    C  +    + xxC + x
0  CCCCC C   CCC C++C  CCC  + xC I +I CCCxCCCCCCCCCCCCC OOC + O
9        CC  C   C  CC C  C + IC IxII CCCICC  CCC      COOC   O
8   I x   C CC CCCCC C CC CCC ICCCCCC   CIIxIx  C  CC  COOC   O
7   x I xIC  C C   C C  C C C x     C C C    x  C  C   C OCC  O
6   I   IIC  C CxI CCCCCC CCC   C C C C CCCCCCCCC CC x C OCC  O
5      CCCCCCC CII  CCCCC CCCCCCC   C C CC      C  C     xC   x
4      C  - CC CCCCCCCC CCCCCCCCCCCCC-C CC  - C C CCC - xxC - x
3  -      - C   C     C C            -C  C  - C   C   - xxC - x
2  x      x CCCCC -         -  CCCCC xCCCC  x CCCCC   x     x
1  -      -       x         x        -      -         -     -
0 ------------------------------x-------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2
1
0
9
8
7
6       xM
5
4
3
2
1
0
```
Legend: M=Metal 2, x=Connection (upper side)
