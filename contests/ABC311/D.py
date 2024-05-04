from collections import deque

n, m = map(int, input().split())
s = [input() for _ in range(n)]

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

q = deque()
# fl[i][j][k]: (i,j)の，直前の状態がkの場合
# 上下左右停止が01234にあたる
fl = [[[False] * 5 for __ in range(m)] for _ in range(n)]

fl[1][1][4] = True
q.append((1, 1, 4))
while q:
    x, y, d = q.popleft()
    # 直前が「停止」なら，各方向に動く
    if d == 4:
        for i in range(4):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy
            nd = i
            if s[nx][ny] == '.':
                fl[nx][ny][nd] = True
                q.append((nx, ny, nd))
    # 移動で来たなら，止まるか続けるかの二択
    else:
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        nd = d
        if s[nx][ny] == '.':
            if not fl[nx][ny][nd]:
                fl[nx][ny][nd] = True
                q.append((nx, ny, nd))
        else:
            if not fl[x][y][4]:
                fl[x][y][4] = True
                q.append((x, y, 4))

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(5):
            if fl[i][j][k]:
                ans += 1
                break

print(ans)