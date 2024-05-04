n = int(input())
D = [list(map(int, input().split())) for _ in range(n - 1)]

# twoの要素のタプル
# 「iとjが立っていることを示すビット」，その時の重み
two = []
for i in range(n):
    for j in range(i + 1, n):
        two.append(((1 << i) | (1 << j), D[i][j - i - 1]))

# bit DP
dp = [0] * (1 << n)

for bit in range(1 << n):
    for dbit, d in two:
        # twoの二本とも消えていたら，dを足したやつとの大小比較
        if bit & dbit == 0:
            dp[bit | dbit] = max(dp[bit | dbit], dp[bit] + d)

print(max(dp))