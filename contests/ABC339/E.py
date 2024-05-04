import bisect

N, D = map(int, input().split())
A = [int(x) for x in input().split()]

INF = 1000000000000000

dp = [INF] * N

LIS = [A[0]]
for i in range(len(A)):
    if abs(A[i] - LIS[-1]) <= D:
        LIS.append(A[i])
    else:
        LIS[bisect.bisect_left(LIS, A[i])] = A[i]

print(len(LIS))