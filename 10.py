with open("input10.txt") as f:
    data = f.read().splitlines()

hp_list = [[]]
slope_cou = 0


def calculate_path(y_c, x_c):
    curr_height = int(data[y_c][x_c])
    if (y_c < 0) or (y_c > len(data)):
        return
    if (x_c < 0) or (x_c > len(data[0])):
        return
    if data[y_c][x_c] == "9":
        hp_list[-1].append((y_c, x_c))
        return
    if y_c > 0:
        if int(data[y_c-1][x_c]) == curr_height+1:
            calculate_path(y_c - 1, x_c)
    if x_c > 0:
        if int(data[y_c][x_c-1]) == curr_height+1:
            calculate_path(y_c, x_c - 1)
    if y_c < (len(data)-1):
        if int(data[y_c+1][x_c]) == curr_height+1:
            calculate_path(y_c + 1, x_c)
    if x_c < (len(data[0])-1):
        if int(data[y_c][x_c+1]) == curr_height+1:
            calculate_path(y_c, x_c + 1)


for y, line in enumerate(data):
    for x, _ in enumerate(line):
        if data[y][x] == "0":
            calculate_path(y, x)
            hp_list.append([])

cou_1 = 0
cou_2 = 0
for i in hp_list:
    cou_2 += len(i)
    cou_1 += len(set(i))
print(cou_1)
print(cou_2)



