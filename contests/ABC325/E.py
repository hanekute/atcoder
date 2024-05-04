def shortest(d, start):
    INF = 1000000000000000
    dist = [0 if i == start else INF for i in range(N)]
    used = [False] * N
    while True:
        v = -1
        for i in range(N):
            if not used[i] and (v == -1 or dist[i] < dist[v]):
                v = i
        if v == -1:
            break
        used[v] = True
        for i in range(N):
            dist[i] = min(dist[i], dist[v] + d[v][i])
    return dist

N, A, B, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]

D_car = [[x * A if x > 0 else 0 for x in r] for r in D]
D_train = [[x * B + C if x > 0 else 0 for x in r] for r in D]
d1 = shortest(D_car, 0)
d2 = shortest(D_train, N - 1)
print(min(d1[i] + d2[i] for i in range(N)))



'''
【戻る場合はDijkstra】
shortest(d, start)
    距離を持つ二次元配列dとスタート地点startが引数
    各点までの最短距離のリストを返す
【誤った解法:DP】
dp[i][0]: 都市1から都市iに「社用車のみで」移動する最短時間
dp[i][1]: 都市1から都市iに「途中から電車で」移動する最短時間
番号が若い都市に進む場合が抜けてしまう

d[i][j] = d[j][i]を見落としてます
'''