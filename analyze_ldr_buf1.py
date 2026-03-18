import sys
import re

def analyze_ldr(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines:
        match = re.match(r'^1\s+(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+.*?\s+(\w+\.dat)', line)
        if match:
            color = int(match.group(1))
            x = float(match.group(2))
            y = float(match.group(3))
            z = float(match.group(4))
            part = match.group(5)
            stud_x = int(x // 20)
            stud_z = int(z // 20)
            if y == -56: # Metal 1
                print(f"Metal1: Stud({stud_x}, {stud_z}) Color={color} X={x} Z={z} Part={part}")
            if y == -48: # Contact
                print(f"Contact: Stud({stud_x}, {stud_z}) Color={color} X={x} Z={z} Part={part}")

analyze_ldr('models/sg13g2_buf_1.ldr')
