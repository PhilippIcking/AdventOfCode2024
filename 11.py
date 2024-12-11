with open("input11.txt") as f:
    stones = {x: 1 for x in f.read().split()}


def check_dict(name, curr_cou):
    if name not in new_stones:
        new_stones[name] = curr_cou
    else:
        new_stones[name] += curr_cou


for x in range(75):
    new_stones = {}
    for stone, cou in stones.items():
        if stone == "0":
            check_dict("1", cou)
        elif (len(stone) % 2) == 0:
            check_dict(stone[:int(len(stone) / 2)], cou)
            if stone[int(len(stone) / 2):].lstrip("0"):
                check_dict(stone[int(len(stone) / 2):].lstrip("0"), cou)
            else:
                check_dict("0", cou)
        else:
            check_dict(str(int(stone) * 2024), cou)
    stones = new_stones
    if x == 24:
        print(sum(i for _, i in stones.items()))

print(sum(i for _, i in stones.items()))
