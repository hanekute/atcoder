n = int(input())
d = [int(x) for x in input().split()]

ans = 0
for i in range(1, n + 1):
    if i >= 10 and i % 10 != i // 10:
        continue
    for j in range(1, d[i - 1] + 1):
        if j < 10:
            if i % 10 == j:
                ans += 1
        else:
            if i % 10 == j % 10 == j // 10:
                ans += 1

print(ans) 