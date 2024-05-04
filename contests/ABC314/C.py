n, m = map(int, input().split())
s = list(input())
c = [int(x) for x in input().split()]

cnum = [[] for _ in range(m)]
for i in range(n):
    cnum[c[i] - 1].append(i)

ans = [''] * n
for i in range(m):
    for j in range(len(cnum[i])):
        ans[cnum[i][j]] = s[cnum[i][j - 1]]

print(''.join(i for i in ans))
