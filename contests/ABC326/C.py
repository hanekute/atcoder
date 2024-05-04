n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
ans = 0

for i in range(n):
    l = i
    r = n
    mid = (l + r) // 2
    while r - l > 1:
        if a[mid] >= a[i] + m:
            r = mid
        else:
            l = mid
    ans = min(ans, r - i)
print(ans)