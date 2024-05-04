Q = int(input())

L = []

for _ in range(Q):
    N, M = map(int, input().split())
    
    if N == 1:
        L.append(M)
    else:
        print(L[-M])
