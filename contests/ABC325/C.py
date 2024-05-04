h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

def dfs(x, y):
    t = [(x, y)]
    while t:
        x, y = t.pop()
        s[x][y] = '.'
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < h and 0 <= y2 < w:
                    if s[x2][y2] == '#':
                        t.append((x2, y2))

count = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            dfs(i,j)
            count += 1

print(count)
