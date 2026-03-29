import re
import json

def extract():
    mapping = {}
    with open('specifications/sg13g2_stdcell.md', 'r') as f:
        for line in f:
            match = re.search(r'\[(sg13g2_[a-z0-9_]+)\]\(https://skywater-pdk\.readthedocs\.io/en/main/contents/libraries/sky130_fd_sc_hd/cells/([^/]+)/README\.html\)', line)
            if match:
                cell_name = match.group(1)
                pdk_type = match.group(2)
                mapping[cell_name] = pdk_type

    # Special cases if any (e.g. from the list, we saw dfrbpq mapping to dfrbp)
    # The regex should handle it.

    print(json.dumps(mapping, indent=2))

if __name__ == "__main__":
    extract()
