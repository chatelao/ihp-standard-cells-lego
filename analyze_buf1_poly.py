
def parse_grid(grid_text):
    lines = grid_text.strip('\n').split('\n')
    scale_line = lines[0]
    width = len(scale_line[2:])
    grid_lines = lines[1:]
    parsed_grid = []
    for line in grid_lines:
        chars = line[2:].ljust(width)
        parsed_grid.append(list(chars))
    parsed_grid.reverse()
    return parsed_grid

with open('design/sg13g2_buf_1.md', 'r') as f:
    content = f.read()

import re
pattern = r'## Polysilicon\n```\n(.*?)\n```'
match = re.search(pattern, content, re.DOTALL)
if match:
    grid = parse_grid(match.group(1))
    for z in range(len(grid)-1, -1, -1):
        print(f"Z={z:2}: " + "".join(grid[z]))
