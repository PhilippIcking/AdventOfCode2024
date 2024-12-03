with open("input02.txt") as f:
    data = f.read().splitlines()


def isSafe(plan):
    for y in range(len(plan) - 2):

        if not (int(plan[y]) < int(plan[y + 1]) < int(plan[y + 2]) or int(plan[y]) > int(
                plan[y + 1]) > int(plan[y + 2])):
            return False
        if not (abs(int(plan[y + 2]) - int(plan[y + 1])) < 4 and abs(int(plan[y + 1]) - int(plan[y])) < 4):
            return False
    return True


cou1 = 0

for x in data:
    entry = x.split()
    if isSafe(entry):
        cou1 += 1

print(cou1)

cou2 = 0

for x in data:
    trigger_2 = False
    cou1 = 0

    for z in range(len(x.split())):
        entry = x.split()
        entry.__delitem__(z)
        if isSafe(entry):
            trigger_2 = True
    if trigger_2:
        cou2 += 1

print(cou2)
