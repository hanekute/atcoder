N, M = map(int, input().split())
A = [int(x) for x in input().split()]

for i in range(N):
    X = [int(x) for x in input().split()]
    for j in range(M):
        A[j] = A[j] - X[j]

joken = True
for a in A:
    if a > 0:
        joken = False
        break
print('Yes' if joken else 'No')