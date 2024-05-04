n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

left = 0
right = max(b) + 1
while left + 1 < right:
    mid = (left + right) // 2
    sell = sum(x <= mid for x in a)
    buy = sum(x >= mid for x in b)
    if sell >= buy:
        right = mid
    else:
        left = mid

print(right)