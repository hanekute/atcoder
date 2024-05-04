# DP
n, m = map(int, input().split())
p = [0, 0] + [int(x) for x in input().split()]
x, y  = [], []
a_ = [list(map(int,input().split())) for _ in range(m)]
for i in range(m):
    x.append(a_[i][0])
    y.append(a_[i][1])

dp = [-1] * (n + 1)

for i in range(m):
    dp[x[i]] = max(dp[x[i]], y[i])

for i in range(n + 1):
    dp[i] = max(dp[i], dp[p[i]] - 1)

ans = sum(i >= 0 for i in dp)
print(ans)
# dp[i]: 人iは最大で何代先まで補償対象者か
# 答えはdp[i] >= 0を満たすiの個数