MOD = 998244353

s = input()

n = len(s)

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(n):
        if s[i - 1] == '(':
            dp[i][j + 1] += dp[i - 1][j]
            dp[i][j + 1] %= MOD
        elif s[i - 1] == ')':
            dp[i][j - 1] += dp[i - 1][j]
            dp[i][j - 1] %= MOD
        else:
            dp[i][j + 1] += dp[i - 1][j]
            dp[i][j - 1] += dp[i - 1][j]
            dp[i][j + 1] %= MOD
            dp[i][j - 1] %= MOD

print(dp[n][0])

# DPによる数え上げ
# dp[i][j]: i文字目までで，(の数が)の数以上で，その差がjとなる場合の数
# 答えはdp[n][0] ※1-indexed
