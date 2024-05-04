N, K = map(int, input().split())
P = [int(x) for x in input().split()]

Q = [0] * N
for i in range(N):
    Q[P[i] - 1] = i + 1

if K * 2 > N:
    print(K - 1)

if K == 1:
    print(0)

else:
    ans = K - 1

    QQ = [Q[i:i+K] for i in range(N - K + 1)]
    for i in range(len(QQ)):
        q = QQ[i]
        m = max(q) - min(q)
        ans = min(ans, m)

    print(ans)