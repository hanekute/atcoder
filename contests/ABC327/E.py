n = int(input())
p = [int(x) for x in input().split()]
c = 0.9
dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = c * dp[i] + p[i]


'''
【kを固定して考える】
選ぶコンテストを変えて変化するのは1項目の分子のみ→1次関数
各kについて求めて最大値を取ればいい.

【動的計画法】
dp[i][j] (1≤j≤i≤N) 
「1 回目から i 回目までのコンテストのうち j 個を選んだ時の分子の最大値」
とすれば，dp[i-1][j]とdp[i-1][j-1]が分かればdp[i][j]が求められる．
jに関しては直前の値(つまり最大値)があればいいから1次元配列でいい

求めるのは1 <= k <= n におけるdp[n]のmaxのmax

【誤差が10^-6以内とかいう文言】
特殊な計算方法が必要な訳じゃない．
'''