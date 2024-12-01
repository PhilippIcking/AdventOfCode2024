with open("input01.txt") as f:
    inp = f.read().splitlines()

loc_ID_1 = []
loc_ID_2 = []

for x in inp:
    a, b = x.split("   ")
    loc_ID_1.append(int(a))
    loc_ID_2.append(int(b))

# Part 1
part1_sum = 0
for x in range(len(loc_ID_1)):
    part1_sum += abs(sorted(loc_ID_1)[x]-sorted(loc_ID_2)[x])

print(part1_sum)

# Part 2
part2_sum = 0
for x in loc_ID_1:
    part2_sum += x*loc_ID_2.count(x)

print(part2_sum)
