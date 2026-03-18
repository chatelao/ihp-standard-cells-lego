def get_block(name, legend, grid):
    lines = [f"{(14-i)%10} {line}" for i, line in enumerate(grid)]
    return [f"## {name}", "GOLDEN STANDARD", "", "```", "  012345678901234"] + lines + ["```", f"Legend: {legend}", ""]

substrate = ["NNNNNNNNNNNNNNN"] * 7 + ["SSSSSSSSSSSSSSS"] * 8
active = [
    "ppppppppppppppp",
    "NNNNNNNNNNNNNNN",
    "NpppppppppppppN",
    "NpppppppppppppN",
    "NpppppppppppppN",
    "NpppppppppppppN",
    "NpppppppppppppN",
    "SSSSSSSSSSSSSSS",
    "SSSSSSSSSSSSSSS",
    "SSSSSSSSSSSSSSS",
    "SnnnnnnnnnnnnnS",
    "SnnnnnnnnnnnnnS",
    "SnnnnnnnnnnnnnS",
    "SSSSSSSSSSSSSSS",
    "nnnnnnnnnnnnnnn",
]
poly = ["               "] * 15
for z in range(1, 14):
    line = list("               ")
    line[0] = 'G'; line[2] = 'G'
    line[9] = 'G'; line[11] = 'G'
    if z == 6:
        line[1] = 'G'; line[10] = 'G'
    poly[14-z] = "".join(line)

m1 = [
    "&+&+&+&+&+&+&+&", # 14
    "  +      +     ", # 13
    "  &      +     ", # 12
    "    +  C C + C O", # 11
    "    &  C CcCcC O", # 10
    "    + CCCCCCCC O", # 9
    "      c       co", # 8
    "      C       CO", # 7
    " iI C      IiI o", # 6 (stud 1, 10, 14)
    "      C       OO", # 5
    " -_ c  -      oO", # 4
    " --    -    OO -", # 3
    " -_    -       _", # 2
    " --    -       -", # 1
    "-_-_-_-_-_-_-_-"  # 0
]

content = ["# Design Documentation for sg13g2_xor2_1", ""]
content += get_block("Substrate", "N=N-Well, S=Substrate", substrate)
content += get_block("Active", "n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)", active)
content += get_block("Polysilicon", "G=Polysilicon", poly)
content += get_block("Metal 1", "+/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)", m1)

with open("handmade/sg13g2_xor2_1.md", "w") as f:
    f.write("\n".join(content))
