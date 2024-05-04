H, W, N = map(int, input().split())

direc = ((-1, 0), (0, 1), (1, 0), (0, -1))

grid = [['.' for _ in range(W)] for _ in range(H)]

x, y, d = 0, 0, 0

for i in range(N):
    if grid[x][y] == '.':
        grid[x][y] = '#'
        d = (d + 1) % 4
        (dx, dy) = direc[d]
        x = (x + dx) % H
        y = (y + dy) % W
    elif grid[x][y] == '#':
        grid[x][y] = '.'
        d = (d - 1) % 4
        (dx, dy) = direc[d]
        x = (x + dx) % H
        y = (y + dy) % W

for i in range(H):
    print(''.join(p for p in grid[i]))
