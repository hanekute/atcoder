from collections import deque

n1, n2, m = map(int, input().split())
a = []
b = []
a_ = [list(map(int,input().split())) for _ in range(m)]
for i in range(m):
    a.append(a_[i][0])
    b.append(a_[i][1])

n = n1 + n2

g = [[] for _ in range(n)]
for i in range(m):
    g[a[i]-1].append(b[i]-1)
    g[b[i]-1].append(a[i]-1)

dist = [-1]*n

qu = deque()

dist[0] = 0
qu.append(0)
while qu:
    x = qu.popleft()
    for i in g[x]:
        if dist[i] == -1:
            dist[i] = dist[x] + 1
            qu.append(i)

dist[n - 1] = 0
qu.append(n - 1)

while qu:
    x = qu.popleft()
    for i in g[x]:
        if dist[i] == -1:
            dist[i] = dist[x] + 1
            qu.append(i)

print(max(dist[:n1]) + max(dist[n1:]) + 1)