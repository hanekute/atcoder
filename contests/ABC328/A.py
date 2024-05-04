n, x = map(int, input().split())
a = [int(x) for x in input().split()]

ans = 0
for i in range(n):
    if a[i] <= x:
        ans += a[i]
print(ans)