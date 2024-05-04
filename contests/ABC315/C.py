n = int(input())
res = 0

fs = [[] for _ in range(n + 1)]
for i in range(n):
    f, s = map(int, input().split())
    fs[f].append(s)

best = []
for i in range(1, n + 1):
    fs[i].sort(reverse=True)
    if len(fs[i]) >= 2:
        res = max(res, fs[i][0] + fs[i][1] // 2)
    if len(fs[i]) >= 1:
        best.append(fs[i][0])

best.sort(reverse=True)
if len(best) >= 2:
    res = max(res, best[0] + best[1])
elif len(best) == 1:
    res = max(res, best[0])

print(res)