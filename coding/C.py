N = int(input())
A, B, D  = [], [], []
A_ = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    A.append(A_[i][0])
    B.append(A_[i][1])
    D.append(A_[i][1] - A_[i][0])

ans = sum(A) + max(D)
print(ans)