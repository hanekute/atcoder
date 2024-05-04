from collections import deque

n, m = map(int, input().split())
a, b, x, y  = [], [], [], []
a_ = [list(map(int,input().split())) for _ in range(m)]
for i in range(m):
    a.append(a_[i][0])
    b.append(a_[i][1])
    x.append(a_[i][2])
    y.append(a_[i][3])

nodes = [set() for _ in range(n + 1)]

for i in range(m):
    nodes[a[i]].add((b[i], x[i], y[i]))
    nodes[b[i]].add((a[i], -x[i], -y[i]))

positions = [False] * (n + 1)
positions[0] = (0, 0)
positions[1] = (0, 0)

decided = [False] * (n + 1)
decided[0] = True
decided[1] = True

stack = deque()
stack.append(1)
while stack:
    i = stack.pop()
    nx, ny = positions[i]
    for j, dx, dy in nodes[i]:
        if decided[j]:
            continue
        positions[j] = (nx + dx, ny + dy)
        stack.append(j)
        decided[j] = True

for i in range(1, n + 1):
    if decided[i]:
        print(f'{positions[i][0]} {positions[i][1]}')
    else:
        print('undecidable')