# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
012345678901234567890123456789012345678901234567890123456789012345678901234567

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```

## Active
```
012345678901234567890123456789012345678901234567890123456789012345678901234567


 ppXppppppppppXpppppXppppppppppXpppppppppppppppppppppppppppppppXpppXpppXppppXp
 ppXppppppppppXpppppXppppppppppXpppppppppppppppppppppppppppppppXpppXpppXppppXp
 ppXppppppppppXpppppXppppppppppXpppppppppppppppppppppppppppppppXpXpXpppXpXXpXp
              X     X                                          X X X   X XX X
              X     X                                          X X X   X XX X


   X     X                   X                X
      X    X
 nnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnXnnnnnnnnnnXnnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnXnXnnnXnXnX
 nnXnnnnnnnnnnXnnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnXnXnnnXnXnX
 nnXnnnnnnnnnnXnnnnnnnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnnXnnnXnnnX


```

## Polysilicon
```
012345678901234567890123456789012345678901234567890123456789012345678901234567


  GXG   G G G X     X       G GX             G G               X   X   X    X
  GXG   G G G X     X       G GX             G G               X   X   X    X
  GXG   G G G X     X       G GX             G G               X X X   X XX X
  G G   G G G X     X       G G              G G               X X X   X XX X
  G G   G G G X     X       G G              G G               X X X   X XX X
  G G   G G G               G G              G G
  G G   G G G               G G              G G
  GXG   GXG G               GXG              GXG
  G G X GGGXG               G G              GGG
  G G X G G G               G G              G G
  G G   GXG G               G G              G G
  GXG   G G G X         X   X G              G G           X    X  X X   X X X
  GXG   G G G X         X   X G              G G           X    X  X X   X X X
  GXG   G G G X         X   X G              G G           X    X    X   X   X


```

## Metal 1
```
012345678901234567890123456789012345678901234567890123456789012345678901234567
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   x          x     x          x                               x   x   x    x
   x CCCCCCCCCx     x CCCCCCCCCx       CCCCCCCCCCCCCCCCCCCCCC  x   x   x    x
   x C       Cx CC  x C       Cx CCCCC                         x x x   x xx x
C    C   C   Cx CC  x C CCC C C  C C C    CCCCCCCCCCCC         x x x CCx xx x
CCCCCC CCC   Cx CC  x C C   C CCCC C C    C          C         x x x CCx xx x
C   CCCC     C+ CC  + C C CCCCCCCCCC C  CCC CCCCCC C CCCCCCCCCCC O + CC+ OO +
C   C        C  CC    C C C        C C   C  C      C C  CC     C O + CC   O
C IxC   IxII CCCCC    C C C Ix C   C C   C CCIxI   C C  CC     C O    CCC O
C IIC x IIIx CCCCCCCC C C   II C C C CCC C CCIII CCC CC C    C C OOO  CCC OO
C   C x   II   C C    C CCCCCCCC CCCCC C C  C    C  CCCCCCCCCC C  OO   C   OOO
C  -C IIIxIICCCC C    C   C   C        C    CCCC CC            C  OO   C - OOO
C  xCCCCCCCCC x  C  CCC x C x C CCCCCCCC       C CCCCCCCCC x  CCx  x x C x x x
   x          x  C      x   x CCCCCCCCCCCCCCCCCCCCCCCCCC   x    x  x x C x x x
   x          x         x   x                              x    x    x   x   x
------------------------------------------------------------------------------
------------------------------------------------------------------------------
```

## Metal 2
```
012345678901234567890123456789012345678901234567890123456789012345678901234567


















```
