n = int(input())
INF = 1000000000000

x, y, z  = [], [], []
a_ = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    x.append(a_[i][0])
    y.append(a_[i][1])
    z.append(a_[i][2])

z_to_win = sum(z) // 2 + 1

dp = [INF] * (z_to_win + 1)

dp[0] = 0

for i in range(n):
    kuragae = 0 if x[i] > y[i] else (y[i] - x[i]) // 2 + 1
    for j in reversed(range(z_to_win)):
        dp[min(j + z[i], z_to_win)] = min(dp[min(j + z[i], z_to_win)], dp[j] + kuragae)
print(dp[z_to_win])
# dp[i]: 高橋がちょうどi議席獲得するために必要な最小鞍替え人数
# INF >= 10^9 * 100 = 10^11