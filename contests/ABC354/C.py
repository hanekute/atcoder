N = int(input())
A, C  = [], []
A_ = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    A.append(A_[i][0])
    C.append(A_[i][1])

