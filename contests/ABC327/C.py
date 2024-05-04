a = [input().split() for _ in range(9)]

flag = True

for r in range(9):
    if len(a[r]) != len(set(a[r])):
        flag = False

for c in range(9):
    line = []
    for r in range(9):
        line.append(a[r][c])
    if len(line) != len(set(line)):
        flag = False

for i in [0, 3, 6]:
    for j in [0, 3, 6]:
        box = []
        for x in range(3):
            for y in range(3):
                box.append(a[i + x][j + y])
        if len(box) != len(set(box)):
            flag = False

print('Yes' if flag else 'No')
