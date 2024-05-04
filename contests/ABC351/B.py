N = int(input())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(str(i+1) + " " + str(j+1))
            break