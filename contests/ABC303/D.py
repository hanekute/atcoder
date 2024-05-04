x, y, z = map(int, input().split())
s = input()

def chmin(a, b):
    if a > b:
        a = b
        return True
    else:
        return 0


inf = 10**15
dp = [[inf, inf] for _ in range(len(s)+1)]

dp[0][0] = 0
for i in range(len(s)):
    dp[i][0] = min(dp[i][0], dp[i][1] + z)
    dp[i][1] = min(dp[i][1], dp[i][0] + z)
    
    if s[i] == 'a':
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + x)
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + y)
    else:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + y)
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + x)

print(min(dp[len(s)][0], dp[len(s)][1]))