n, k = map(int, input().split())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

ab.sort()
med = 0
for i in range(n):
    med += ab[i][1]

if med <= k:
    print(1)

else:
    for i in range(n):
        if med <= k:
            print(ab[i -1][0] + 1)
            exit()
        else:
            med -= ab[i][1]
    print(ab[-1][0] + 1)