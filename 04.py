with open("input04.txt") as f:
    data = f.read().splitlines()

directions = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

cou1 = 0
cou2 = 0


def find_xmas(y_koor, x_koor, dir_y, dir_x):
    new_str = ""
    for z in range(4):
        if y_koor + z * dir_y < 0 or x_koor + z * dir_x < 0:
            return False
        new_str += data[y_koor + z * dir_y][x_koor + z * dir_x]
    if new_str == "XMAS":
        return True
    return False


def find_X_mas(y_koor, x_koor):
    new_str_1 = ""
    new_str_2 = ""
    if y_koor == 0 or x_koor == 0:
        return False
    for offset_y, offset_x in [(-1, -1), (0, 0), (1, 1)]:
        new_str_1 += data[y_koor + offset_y][x_koor + offset_x]
    for offset_y, offset_x in [(1, -1), (0, 0), (-1, 1)]:
        new_str_2 += data[y_koor + offset_y][x_koor + offset_x]
    if (new_str_1 in ["MAS", "SAM"]) and (new_str_2 in ["MAS", "SAM"]):
        return True
    return False


for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "X":
            for d_x, d_y in directions:
                try:
                    if find_xmas(y, x, d_y, d_x):
                        cou1 += 1
                except IndexError:
                    pass
        if data[y][x] == "A":
            try:
                if find_X_mas(y, x):
                    cou2 += 1
            except IndexError:
                pass
print(cou1)
print(cou2)
