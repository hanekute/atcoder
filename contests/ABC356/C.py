from itertools import combinations
N, M, K = map(int, input().split())
C = []
A = []
R = []

for i in range(M):
    tmp = [x for x in input().split()]
    C.append(int(tmp[0]))
    A.append(set(int(x) for x in tmp[1:-1]))
    R.append(tmp[-1])

ans = 0
member = []
for i in range(K, N + 1):
    member += list(combinations(range(1, N + 1), i))

for V in member:
    v = set(V)
    flag = True
    for m in range(M):
        if len(v & A[m]) >= K:
            if R[m] == "x":
                flag = False
                break
        else:
            if R[m] == "o":
                flag = False
                break
    if flag:
        ans += 1

print(ans)


        # vとA[m]の共通部分の要素数がK以上 and R[m] == "o"
        # そうでない and R[m] == "x"
        # これらがみたされればans += 1
# 15本しかない→ 2^15 = 32768通りしかないから総当たりOK
# 2^N * M < 400万