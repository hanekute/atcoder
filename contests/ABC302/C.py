import itertools


def diff(A, B):
    res = 0
    for a, b in zip(A, B):
        if a != b:
            res += 1
    return res

n, m = map(int, input().split())
s = [input() for _ in range(n)]

finish = True

for t in itertools.permutations(s):
    finish = True
    for i in range(n-1):
        if diff(t[i], t[i+1]) != 1:
            finish = False
    if finish: break

if finish: print('Yes')
else: print('No')