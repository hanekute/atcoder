N = int(input())
S = [input() for _ in range(N)]

row, col = [0]*N, [0]*N

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            row[i] += 1
            col[j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            ans += (row[i] - 1) * (col[j] - 1)

print(ans)

'''
N <= 2000
Lみたいな形のoを探す
'''