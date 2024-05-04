from collections import deque

S = deque(input())
T = deque(input())

L = len(S)
ans = []

num = 1

while len(ans) < L:
    s = S.popleft()
    t = T.popleft()
    while s != t:
        t = T.popleft()
        num += 1
    ans.append(num)
    num += 1
    

print(' '.join(str(i) for i in ans))