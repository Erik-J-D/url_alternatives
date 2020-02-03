import sys

from collections import defaultdict
from itertools import product

if len(sys.argv) < 2:
    print(
        "Missing arguments. Usage:  $ url_generator.py mydomain.com domain2.org etc.net"
    )


# Read in confusables.txt, turn into dictionary lookup
with open("confusables.txt", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()
clean_lines = [l.strip() for l in lines if not l.startswith("#") and l.strip()]
lookup = defaultdict(list)
for line in clean_lines:
    sketch, reg = (s.strip() for s in line.split(";")[:2])
    # some of the characters are multiple code points, only really care about english here
    if " " in sketch or " " in reg:
        continue
    sketch, reg = (chr(int(s.strip(), 16)) for s in (sketch, reg))
    lookup[reg].append(sketch)

# print out substitute urls
for url in sys.argv[1:]:
    segments = url.split(".")
    iterables = []
    for letter in segments[0]:
        iterables.append(lookup[letter] or [letter])
    for permutation in product(*iterables):
        domain = "".join(permutation)
        if segments[1:]:
            domain += "." + ".".join(segments[1:])
        print(domain)
