n = int(input())
x = []
y = []
a_ = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    x.append(a_[i][0])
    y.append(a_[i][1])

dp = [[0,0] for _ in range(n + 1)]

for i in range(n):
    if x[i] == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][0] + y[i], dp[i][1] +y[i])
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][0] + y[i], dp[i][1])

print(max(dp[n]))