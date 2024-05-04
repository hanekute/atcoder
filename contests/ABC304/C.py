from collections import deque
n, d = map(int, input().split())

xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

kansen =[False] * n
kansen[0] = True

qu = deque()
qu.append(xy[0])
while qu:
    a = qu.popleft()
    for i in range(n):
        if (a[0] - xy[i][0]) ** 2 + (a[1] - xy[i][1]) ** 2 <= d ** 2:
            if not kansen[i]:
                qu.append(xy[i])
                kansen[i] = True
                
for i in range(n):
    print('Yes' if kansen[i] else 'No')