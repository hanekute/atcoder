from collections import deque
n = int(input())
c, p = [], [[0]]
for i in range(n):
    c_and_p = list(map(int, input().split()))
    c.append(c_and_p[0])
    if c_and_p[0] == 0:
        p.append([0])
    else:
        p.append(c_and_p[1:])

#BFS
qu = deque() 

checked = [False] * (n + 1)
checked[0] = True
qu.append(1)

ans = deque()

while qu:
    i = qu.popleft()
    for j in p[i]:
        if j in ans:
            ans.remove(j)
        else:
            qu.append(j)
        ans.appendleft(j)

ans.remove(0)

print(' '.join(str(i) for i in ans))