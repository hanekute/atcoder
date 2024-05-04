from itertools import combinations

n, m, k = map(int, input().split())
g = [[] * n for _ in range(n)]

for i in range(m):
    u, v, w = map(int, input().split())
    g[u - 1].append([v - 1, w, i])
    g[v - 1].append([u - 1, w, i])

ans = k

for comb in combinations(range(m), n - 1):
    comb = set(comb)
    stack = []
    stack.append(0)
    seen = set()
    seen.add(0)
    val = 0
    while stack:
        v = stack.pop()
    for child, w, e in g[v]:
        if e not in comb:
            continue
        if child in seen:
            continue
        seen.add(child)
        val += w
        stack.append(child)
    if len(seen) == n:
        ans = min(ans, val % v)
print(ans)
'''
n少ないから全探索できるかチェック
今回の「全探索」とは，
    M本の辺のうちN-1本を選ぶ全ての組み合わせについて，
    全域木だったらコストを調べる
N=8, M=28で最大28C8 < 2.5e7より余裕
解説ではUnion-Findを使っているが，無しでもACできる
'''