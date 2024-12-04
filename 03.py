import re

with open("input03.txt") as f:
    data = f.read().splitlines()

# Part 1
pattern = "mul\(([0-9]+),([0-9]+)\)"

cou1 = 0

for x in data:
    matches = re.findall(pattern, x)
    for match in matches:
        a, b = match
        cou1 += int(a) * int(b)
print(cou1)

# Part 2
pattern = "mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don't\(\))"

cou2 = 0

trigger = True
for x in data:
    matches = re.findall(pattern, x)
    for match in matches:
        a, b, c, d = match
        if c == "do()":
            trigger = True
        elif d == "don't()":
            trigger = False
        else:
            if trigger:
                cou2 += int(a) * int(b)
print(cou2)
