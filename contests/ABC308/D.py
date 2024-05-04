h, w = map(int, input().split())
s = [input() for _ in range(h)]

turn = {'s': 'n', 'n': 'u', 'u': 'k', 'k': 'e', 'e': 's'}
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if s[0][0] not in 'snuke':
    print('No')
    exit()

stack = [(0,0)]
checked = [[False]* w for i in range(h)]
checked[0][0] = True

while stack:
    x, y = stack.pop()
    
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:
            if s[nx][ny] == turn[s[x][y]]:
                if (nx, ny) == (h-1, w-1):
                    print('Yes')
                    exit()
                if not checked[nx][ny]:
                    stack.append((nx, ny))
                    checked[nx][ny] = True

print('No')