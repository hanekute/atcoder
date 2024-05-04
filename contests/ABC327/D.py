from collections import deque
n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

nodes = [set() for _ in range(n + 1)]

for i in range(m):
    nodes[a[i]].add(b[i])
    nodes[b[i]].add(a[i])

num = [0]*(n + 1)
num[a[0]] = 1

stack = deque()
stack.appendleft(a[0])
checked = [False]*(n + 1)
checked[a[0]] = True

while stack:
    x = stack.pop()
    for next in nodes[x]:
        if checked[next]:
            if num[next] != 0 and (num[next] + num[x]) % 2 == 0:
                print('No')
                exit()
        else:
            num[next] = num[x] + 1
            stack.append(next)
            checked[next] = True
    if len(stack) == 0:
        for s in nodes:
            for i in s:
                if not checked[i]:
                    stack.append(i)
print('Yes')