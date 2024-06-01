N, L, R = map(int, input().split())

ans = []
for i in range(N):
    if L - 1 <= i < R:
        ans.append(R + L - 1 - i)
    else:
        ans.append(i + 1)
        
print(' '.join(str(i) for i in ans))